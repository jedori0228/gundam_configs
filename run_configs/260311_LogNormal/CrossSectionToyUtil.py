import numpy as np
import awkward as ak
import uproot
from scipy.optimize import curve_fit

def my_gauss(x, C, mu, sigma):
    return C * np.exp(-(x - mu)**2 / (2 * sigma**2))

def CalcXsecFromThrows(CalcXsecOutputFilepath, VarType):

    """

    Parameters
    ----------
    CalcXsecOutputFilepath : str
        Full filepath to the gundam CalcXsec output file
    VarType : str
        'Angular' or 'TKI'

    Returns
    -------
    type
        Description of the return value.


    """

    if VarType=='Angular':

        VarXName = 'MuonCos'
        VarYName = 'MuonProtonCos'
        PhaseSpaceCutName = 'AllSignal'

    elif VarType=='TKI':

        VarXName = 'deltaPT'
        VarYName = 'deltaalphaT'
        PhaseSpaceCutName = 'MuonPLT0p8'

    else:
        raise

    with uproot.open(CalcXsecOutputFilepath) as f:
        
        df = f[f'calcXsec/throws/xsecThrow_TTree'].arrays(library='ak')

        GlobalBinMasks = []

        uph_Cov = f['calcXsec/matrices/covarianceMatrix_TH2D']
        NXsecBin = uph_Cov.to_numpy()[0].shape[0]

        tmp_ColNameBase = f'TrueSignal_{PhaseSpaceCutName}_True{VarXName}'
        NToys = len(df[tmp_ColNameBase])

        # print('NXsecBin_Combined', NXsecBin)
        # print('NToys', NToys)

        NXSecBins = []
        for VarName in [VarXName, VarYName]:

            ColNameBase = f'TrueSignal_{PhaseSpaceCutName}_True{VarName}'

            this_akarr_xsec = df[ColNameBase]
            
            NToys = len(this_akarr_xsec)

            this_BinColNames = this_akarr_xsec.type.content.fields
            this_NXsecBin = len(this_BinColNames)
            NXSecBins.append(this_NXsecBin)

            this_arr_xsec = np.zeros((NToys, this_NXsecBin))
            for iBin in range(this_NXsecBin):
                this_arr_xsec[:,iBin] = this_akarr_xsec[this_BinColNames[iBin]].to_numpy()

            bf = f[f'calcXsec/histograms/TrueSignal_{PhaseSpaceCutName}_True{VarName}_TH1D'].to_numpy()[0]

            if VarName==VarXName:
                arr_xsec = this_arr_xsec
                bestfit_vals = bf
            else:
                arr_xsec = np.hstack((arr_xsec, this_arr_xsec))
                bestfit_vals = np.append(bestfit_vals, bf)

            del this_akarr_xsec
            del this_arr_xsec

        del df

        NXSecBins = np.array(NXSecBins)

        arr_xsec_log = np.log(arr_xsec)

        cov_log = np.cov(arr_xsec_log, rowvar=False)

        std_log = np.std(arr_xsec_log, axis=0)
        up_log = np.log(bestfit_vals) + std_log
        dn_log = np.log(bestfit_vals) - std_log

        up = np.exp(up_log)
        dn = np.exp(dn_log)

        final_up_err = up-bestfit_vals
        final_dn_err = bestfit_vals-dn

        NXSecBin_VarX = NXSecBins[0]
        NXSecBin_VarY = NXSecBins[1]

        SubIndices_VarX = np.arange(0, NXSecBin_VarX)
        SubIndices_VarY = np.arange(NXSecBin_VarX, NXSecBin_VarX+NXSecBin_VarY)

        return cov_log, bestfit_vals, (final_dn_err, final_up_err), NXSecBins, (SubIndices_VarX, SubIndices_VarY)
