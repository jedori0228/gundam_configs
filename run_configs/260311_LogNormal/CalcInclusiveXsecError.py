import uproot
import awkward as ak
import pandas as pd
import numpy as np

def CalcInclusiveXsecError(GUNDAMCalcXsecOutputPath, Binnings_Extraction, BranchName):

    with uproot.open(GUNDAMCalcXsecOutputPath) as f:
        df_Throws = f['calcXsec/throws/xsecThrow_TTree'].arrays(library='pd')
        col = df_Throws[BranchName]
        del df_Throws
        df_Throws = pd.DataFrame(col.tolist())
        del col

    BinWidth_Extraction = np.diff(Binnings_Extraction)

    SumExpr = ''
    for i_bin in range(len(BinWidth_Extraction)):
        df_Throws[f'bin_{i_bin}_BinWidthMult'] = df_Throws[f'bin_{i_bin}'] * BinWidth_Extraction[i_bin]
        if i_bin==0:
            SumExpr += f'bin_{i_bin}_BinWidthMult'
        else:
            SumExpr += f'+bin_{i_bin}_BinWidthMult'

    df_Throws = df_Throws.eval('xsec_sum = '+SumExpr)

    xsec_mean = np.mean(df_Throws['xsec_sum'])
    xsec_std = np.std(df_Throws['xsec_sum'])

    return xsec_mean, xsec_std