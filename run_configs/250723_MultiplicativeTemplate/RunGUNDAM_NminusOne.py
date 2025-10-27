import os
import ConfigHelper

# Config
JobName = '250627_BadRegionRejection'


ConfigType = '250723_MultiplicativeTemplate'

# Base directories
GUNDAMDIR = os.environ['GUNDAM_CONFIG_DIR']
WD = f'{GUNDAMDIR}/run_configs/{ConfigType}'

###########################################
# CalcXsec use best-fit vs use mean
UseBestFit = True
###########################################

# Number of toys
NToys = 100000

# Config directory
FitterConfigDir = f'{WD}/configs/Fitter'
CalcXsecConfigDir = f'{WD}/configs/CalcXsec'
os.system(f'mkdir -p {FitterConfigDir}')
os.system(f'mkdir -p {CalcXsecConfigDir}')

# Number of thread
NThread = 8

# Logging
WriteLog = False
LogBasedir = f'{WD}/logs'

# Run on background
RunOnBackground = False

# Define output directories
GUNDAMOutputBasedir = f'{WD}/output/{JobName}'

FitterOutputDir = f'{GUNDAMOutputBasedir}/Fitter'
CalcXsecOutputDir = f'{GUNDAMOutputBasedir}/CalcXsec'
RunScriptDir = f'{WD}/run_scripts'
os.system(f'mkdir -p {FitterOutputDir}')
os.system(f'mkdir -p {CalcXsecOutputDir}')
os.system(f'mkdir -p {RunScriptDir}')


######################
# 1) Require pmu<0.8 for reco in the fit
# - Need to pick separate fitsample
# - Need to pick separate plot config to use IsSignalWithMuonP
ApplyRecoMuonPLT0p8 = False 
######################

######################
# Here, this corresponds to X in N-X
# - X will not be included
# - For the CalcXsec, flux should not be smeared when X=Flux
ParamSetNames = [
    'FullSyst',
    'DetectorAndGEANT4',
    'xsecBkgd',
    'xsecSignal',
    'Flux',
    'NoSyst',
]
######################

# Do Indv fit?
DoIndvFit = False
IndvFit_XsecVariables = [
    'MuonCos',
    'MuonProtonCos',
    # 'deltaPT',
    # 'deltaalphaT',
]
LLH_METHOD_ForIndvFit = 'BarlowLLH'

# Do Sim fit?
DoSimFit = True
SimFit_XsecVariablePairs = [
    ['MuonCos', 'MuonProtonCos'],
    ['deltaPT', 'deltaalphaT'],
]
LLH_METHOD_ForSimFit = 'StatCovariance'

# Datasets

# - Real data, 100%
DatasetType = 'RealData'
DataEntry = 'Asimov'

RunScripts = []

if DoIndvFit:

    RecoDatasetListConfig = ConfigHelper.GetRecoDatasetList(DatasetType)
    TrueDatasetListConfig = ConfigHelper.GetTrueDatasetList()

    BaseConfig_Fitter = f'{WD}/base_configs/config_Fitter.yaml'
    BaseConfig_CalcXsec = f'{WD}/base_configs/config_CalcXsec.yaml'

    LLH_METHOD = LLH_METHOD_ForIndvFit

    FitSampleName = ''
    PlotConfigName = ''
    if ApplyRecoMuonPLT0p8:
        FitSampleName = 'MuonPLT0p8'
        PlotConfigName = 'MuonPLT0p8'

    # Run scripts
    print('# Now writing run scripts to:')

    RunScript_Fitter = f'{RunScriptDir}/run_Fitter_{DatasetType}_IndvFit_NminusOne_{LLH_METHOD}.sh'
    out_RunScript_Fitter = open(RunScript_Fitter, 'w')

    RunScript_CalcXsec = f'{RunScriptDir}/run_CalcXsec_{DatasetType}_IndvFit_NminusOne_{LLH_METHOD}.sh'
    out_RunScript_CalcXsec = open(RunScript_CalcXsec, 'w')

    for IndvFit_XsecVariable in IndvFit_XsecVariables:

        for ParamSetName in ParamSetNames:

            FitConfigName = f'Nminus{ParamSetName}_IndvFit'
            if ParamSetName=='FullSyst':
                FitConfigName = ParamSetName+f'_IndvFit'
            if ParamSetName=='NoSyst':
                FitConfigName = ParamSetName+f'_IndvFit'

            if ApplyRecoMuonPLT0p8:
                FitConfigName += '_MuonPLT0p8'

            # Writting config yamls

            # - Fitter
            outname_Fitter = f'{FitterConfigDir}/config_Fitter_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
            out_Fitter = open(outname_Fitter, 'w')
            ParameterSetListConfig = ConfigHelper.GetParametersetList_IndvFit(IndvFit_XsecVariable, 'NminusOne/'+ParamSetName)
            FitSampleSetConfig_Reco = ConfigHelper.GetRecoFitSampleSet_IndvFit(IndvFit_XsecVariable, FitSampleName)
            PlotGeneratorConfig_Reco = ConfigHelper.GetRecoPlotGenerator_IndvFit(IndvFit_XsecVariable, PlotConfigName)
            for l in open(BaseConfig_Fitter):
                this_line = l
                if '<LLH_METHOD>' in l:
                    this_line = l.replace('<LLH_METHOD>', LLH_METHOD)
                elif '<DATASETLIST_CONFIG>' in l:
                    this_line = l.replace('<DATASETLIST_CONFIG>', RecoDatasetListConfig)
                elif '<PARAMETERSETLIST_CONFIG>' in l:
                    this_line = l.replace('<PARAMETERSETLIST_CONFIG>', ParameterSetListConfig)
                elif '<FITSAMPLESET_CONFIG>' in l:
                    this_line = l.replace('<FITSAMPLESET_CONFIG>', FitSampleSetConfig_Reco)
                elif '<PLOTGENERATOR_CONFIG>' in l:
                    this_line = l.replace('<PLOTGENERATOR_CONFIG>', PlotGeneratorConfig_Reco)
                else:
                    this_line = l
                
                out_Fitter.write(this_line)
            out_Fitter.close()
            print(f'# Fitter config wrote:\n{outname_Fitter}')

            # - CalcXsec
            outname_CalcXsec = f'{CalcXsecConfigDir}/config_CalcXsec_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
            out_CalcXsec = open(outname_CalcXsec, 'w')

            TruthFitSampleDir = 'NoNormSmearing' if ParamSetName=='Flux' else 'SmearFlux'
            if ApplyRecoMuonPLT0p8:
                TruthFitSampleDir += '/MuonPLT0p8'
            FitSampleSetConfig_True = f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/PerSourceStudy/{TruthFitSampleDir}/fitSamples_True{IndvFit_XsecVariable}.yaml"'''
            PlotGeneratorConfig_True = ConfigHelper.GetTruePlotGenerator_IndvFit(IndvFit_XsecVariable)

            for l in open(BaseConfig_CalcXsec):
                this_line = l
                if '<LLH_METHOD>' in l:
                    this_line = l.replace('<LLH_METHOD>', LLH_METHOD)
                elif '<DATASETLIST_CONFIG>' in l:
                    this_line = l.replace('<DATASETLIST_CONFIG>', TrueDatasetListConfig)
                elif '<PARAMETERSETLIST_CONFIG>' in l:
                    this_line = l.replace('<PARAMETERSETLIST_CONFIG>', ParameterSetListConfig)
                elif '<FITSAMPLESET_CONFIG>' in l:
                    this_line = l.replace('<FITSAMPLESET_CONFIG>', FitSampleSetConfig_True)
                elif '<PLOTGENERATOR_CONFIG>' in l:
                    this_line = l.replace('<PLOTGENERATOR_CONFIG>', PlotGeneratorConfig_True)
                elif '<TOY_THROW_CONFIG>' in l:
                    this_line = '''    enableStatThrowINToys: true
    enableEventMcThrow: false
    throwAsimovFitParameters: true
'''
                else:
                    this_line = l
                
                out_CalcXsec.write(this_line)
            out_CalcXsec.close()
            print(f'# CalcXsec config wrote:\n{outname_CalcXsec}')

            # Writing bash script with GUNDAM commands

            print(f'# - DataEntry = {DataEntry}')

            # Fitter
            Fitter_OutputFile = f'{FitterOutputDir}/output_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
            Fitter_LogFile = f'{LogBasedir}/log_Fitter_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.log'
            cmd_Fitter = f'''gundamFitter -c {outname_Fitter} \\
-o {Fitter_OutputFile} \\
-t {NThread} --pca \\
--use-data-entry {DataEntry}'''
            if WriteLog:
                cmd_Fitter += f''' &> {Fitter_LogFile}'''
            if RunOnBackground:
                cmd_Fitter += ' &'
            out_RunScript_Fitter.write(f'# Fitter, {DataEntry}, {IndvFit_XsecVariable}\n')
            out_RunScript_Fitter.write(cmd_Fitter+'\n')

            # CalcXsec
            CalcXsec_OutputFile = f'{CalcXsecOutputDir}/output_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
            CalcXsec_LogFile = f'{LogBasedir}/log_CalcXsec_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.log'
            cmd_CalcXsec = f'''gundamCalcXsec -c {outname_CalcXsec} \\
-f {Fitter_OutputFile} \\
-o {CalcXsec_OutputFile} \\
-s 1 -t {NThread} \\
--TurnRecoOnlyOff \\
--fitsample-config {FitSampleSetConfig_True} \\
--plot-config {PlotGeneratorConfig_True} \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if UseBestFit:
                cmd_CalcXsec += ' \\\n--use-bf-as-xsec'
            
            if WriteLog:
                cmd_CalcXsec += f''' &> {CalcXsec_LogFile}'''
            if RunOnBackground:
                cmd_CalcXsec += ' &'
            out_RunScript_CalcXsec.write(f'# CalcXsec, {DataEntry}, {IndvFit_XsecVariable}\n')
            out_RunScript_CalcXsec.write(cmd_CalcXsec+'\n')

    # Close
    out_RunScript_Fitter.close()
    out_RunScript_CalcXsec.close()

    RunScripts.append(RunScript_Fitter)
    RunScripts.append(RunScript_CalcXsec)
            


    print('# Printing all run scripts that are generated..')
    for RunScript in RunScripts:
        print(f'source {RunScript}')

if DoSimFit:

    RecoDatasetListConfig = ConfigHelper.GetRecoDatasetList(DatasetType)
    TrueDatasetListConfig = ConfigHelper.GetTrueDatasetList()

    BaseConfig_Fitter = f'{WD}/base_configs/config_Fitter.yaml'
    BaseConfig_CalcXsec = f'{WD}/base_configs/config_CalcXsec.yaml'

    LLH_METHOD = LLH_METHOD_ForSimFit

    FitSampleName = ''
    PlotConfigName = ''

    if ApplyRecoMuonPLT0p8:
        FitSampleName = 'MuonPLT0p8'
        PlotConfigName = 'MuonPLT0p8'

    # Run scripts
    print('# Now writing run scripts to:')

    RunScript_Fitter = f'{RunScriptDir}/run_Fitter_{DatasetType}_SimFit_NminusOne_{LLH_METHOD}.sh'
    out_RunScript_Fitter = open(RunScript_Fitter, 'w')

    RunScript_CalcXsec = f'{RunScriptDir}/run_CalcXsec_{DatasetType}_SimFit_NminusOne_{LLH_METHOD}.sh'
    out_RunScript_CalcXsec = open(RunScript_CalcXsec, 'w')

    for SimFit_XsecVariablePair in SimFit_XsecVariablePairs:

        SimFit_XsecVariable_X = SimFit_XsecVariablePair[0]
        SimFit_XsecVariable_Y = SimFit_XsecVariablePair[1]

        for ParamSetName in ParamSetNames:

            FitConfigName = f'Nminus{ParamSetName}_SimFit'
            if ParamSetName=='FullSyst':
                FitConfigName = ParamSetName+f'_SimFit'
            if ParamSetName=='NoSyst':
                FitConfigName = ParamSetName+f'_SimFit'

            if ApplyRecoMuonPLT0p8:
                FitConfigName += '_MuonPLT0p8'

            # Writting config yamls

            # - Fitter
            outname_Fitter = f'{FitterConfigDir}/config_Fitter_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml'
            out_Fitter = open(outname_Fitter, 'w')
            ParameterSetListConfig = ConfigHelper.GetParametersetList_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, 'NminusOne/'+ParamSetName)
            FitSampleSetConfig_Reco = ConfigHelper.GetRecoFitSampleSet_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, FitSampleName)
            PlotGeneratorConfig_Reco = ConfigHelper.GetRecoPlotGenerator_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, FitSampleName)
            for l in open(BaseConfig_Fitter):
                this_line = l
                if '<LLH_METHOD>' in l:
                    this_line = l.replace('<LLH_METHOD>', LLH_METHOD)
                elif '<DATASETLIST_CONFIG>' in l:
                    this_line = l.replace('<DATASETLIST_CONFIG>', RecoDatasetListConfig)
                elif '<PARAMETERSETLIST_CONFIG>' in l:
                    this_line = l.replace('<PARAMETERSETLIST_CONFIG>', ParameterSetListConfig)
                elif '<FITSAMPLESET_CONFIG>' in l:
                    this_line = l.replace('<FITSAMPLESET_CONFIG>', FitSampleSetConfig_Reco)
                elif '<PLOTGENERATOR_CONFIG>' in l:
                    this_line = l.replace('<PLOTGENERATOR_CONFIG>', PlotGeneratorConfig_Reco)
                else:
                    this_line = l

                out_Fitter.write(this_line)
            out_Fitter.close()
            print(f'# Fitter config wrote:\n{outname_Fitter}')

            # - CalcXsec

            outname_CalcXsec = f'{CalcXsecConfigDir}/config_CalcXsec_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml'
            out_CalcXsec = open(outname_CalcXsec, 'w')

            TruthFitSampleDir = 'NoNormSmearing' if ParamSetName=='Flux' else 'SmearFlux'
            if ApplyRecoMuonPLT0p8:
                TruthFitSampleDir += '/MuonPLT0p8'
            FitSampleSetConfig_True = f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/PerSourceStudy/{TruthFitSampleDir}/fitSamples_True{SimFit_XsecVariable_X}_and_True{SimFit_XsecVariable_Y}.yaml"'''
            PlotGeneratorConfig_True = ConfigHelper.GetTruePlotGenerator_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y)

            for l in open(BaseConfig_CalcXsec):
                this_line = l
                if '<LLH_METHOD>' in l:
                    this_line = l.replace('<LLH_METHOD>', LLH_METHOD)
                elif '<DATASETLIST_CONFIG>' in l:
                    this_line = l.replace('<DATASETLIST_CONFIG>', TrueDatasetListConfig)
                elif '<PARAMETERSETLIST_CONFIG>' in l:
                    this_line = l.replace('<PARAMETERSETLIST_CONFIG>', ParameterSetListConfig)
                elif '<FITSAMPLESET_CONFIG>' in l:
                    this_line = l.replace('<FITSAMPLESET_CONFIG>', FitSampleSetConfig_True)
                elif '<PLOTGENERATOR_CONFIG>' in l:
                    this_line = l.replace('<PLOTGENERATOR_CONFIG>', PlotGeneratorConfig_True)
                else:
                    this_line = l
                
                out_CalcXsec.write(this_line)
            out_CalcXsec.close()
            print(f'# CalcXsec config wrote:\n{outname_CalcXsec}')

            # Writing bash script with GUNDAM commands

            print(f'# - DataEntry = {DataEntry}')

            # Fitter
            Fitter_OutputFile = f'{FitterOutputDir}/output_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.root'
            Fitter_LogFile = f'{LogBasedir}/log_Fitter_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.log'
            cmd_Fitter = f'''gundamFitter -c {outname_Fitter} \\
-o {Fitter_OutputFile} \\
-t {NThread} --pca \\
--use-data-entry {DataEntry}'''
            if WriteLog:
                cmd_Fitter += f''' &> {Fitter_LogFile}'''
            if RunOnBackground:
                cmd_Fitter += ' &'
            out_RunScript_Fitter.write(f'# Fitter\n')
            out_RunScript_Fitter.write(cmd_Fitter+'\n')

            # CalcXsec
            outname_CalcXsec = f'{CalcXsecConfigDir}/config_CalcXsec_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml'
            
            CalcXsec_OutputFile = f'{CalcXsecOutputDir}/output_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.root'
            CalcXsec_LogFile = f'{LogBasedir}/log_CalcXsec_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.log'
            cmd_CalcXsec = f'''gundamCalcXsec -c {outname_CalcXsec} \\
-f {Fitter_OutputFile} \\
-o {CalcXsec_OutputFile} \\
-s 1 -t {NThread} \\
--TurnRecoOnlyOff \\
--fitsample-config {FitSampleSetConfig_True} \\
--plot-config {PlotGeneratorConfig_True} \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if UseBestFit:
                cmd_CalcXsec += ' \\\n--use-bf-as-xsec'

            if WriteLog:
                cmd_CalcXsec += f''' &> {CalcXsec_LogFile}'''
            if RunOnBackground:
                cmd_CalcXsec += ' &'
            out_RunScript_CalcXsec.write(f'# CalcXsec\n')
            out_RunScript_CalcXsec.write(cmd_CalcXsec+'\n')

    # Close
    out_RunScript_Fitter.close()
    out_RunScript_CalcXsec.close()

    RunScripts.append(RunScript_Fitter)
    RunScripts.append(RunScript_CalcXsec)


    print('# Printing all run scripts that are generated..')
    for RunScript in RunScripts:
        print(f'source {RunScript}')