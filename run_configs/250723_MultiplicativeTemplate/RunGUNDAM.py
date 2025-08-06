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
NToys = 1000

# Config directory
FitterConfigDir = f'{WD}/configs/Fitter'
ToyGeneratorConfigDir = f'{WD}/configs/ToyGenerator'
CalcXsecConfigDir = f'{WD}/configs/CalcXsec'
os.system(f'mkdir -p {FitterConfigDir}')
os.system(f'mkdir -p {ToyGeneratorConfigDir}')
os.system(f'mkdir -p {CalcXsecConfigDir}')

# Number of thread
NThread = 1

# Logging
WriteLog = False
LogBasedir = f'{WD}/logs'

# Run on background
RunOnBackground = False

# Define output directories
GUNDAMOutputBasedir = f'{WD}/output/{JobName}'

FitterOutputDir = f'{GUNDAMOutputBasedir}/Fitter'
ToyGeneratorOutputDir = f'{GUNDAMOutputBasedir}/ToyGenerator'
CalcXsecOutputDir = f'{GUNDAMOutputBasedir}/CalcXsec'
RunScriptDir = f'{WD}/run_scripts'
os.system(f'mkdir -p {FitterOutputDir}')
os.system(f'mkdir -p {ToyGeneratorOutputDir}')
os.system(f'mkdir -p {CalcXsecOutputDir}')
os.system(f'mkdir -p {RunScriptDir}')

# Do Indv fit?
DoIndvFit = True
IndvFit_XsecVariables = [
    'MuonCos',
    'MuonProtonCos',
    'deltaPT',
    'deltaalphaT',
]
# LLH_METHOD_ForIndvFit = 'PoissonLLH'
LLH_METHOD_ForIndvFit = 'BarlowLLH'

# Do Sim fit?
DoSimFit = False
SimFit_XsecVariablePairs = [
    ['MuonCos', 'MuonProtonCos'],
    ['deltaPT', 'deltaalphaT'],
]
LLH_METHOD_ForSimFit = 'StatCovariance'

######################
ForSimFitToy = False
StatCovDiagOnly = False
######################

# Datasets

# - Fake data
# DatasetType = 'FakeData'
# DataEntries = [
#     # 'Asimov',
#     # 'FakeDataFromMCSubset',
#     'FakeDataLQCDZExpFit',
# ]

# - Real data, 15%
# DatasetType = 'Random15PercentRealData'
# DataEntries = [
#     'Random15PercentRealData',
# ]

# - Real data, 100% for the sideband + fake data for the signal
# DatasetType = 'RealDataForSideband_FakeDataForSignal'
# DataEntries = [
#     'RealDataForSideband_FakeDataForSignal',
# ]

# - Real data, 100% for the sideband + 15% data for the signal
# DatasetType = 'RealDataForSideband_Random15PercentRealDataForSignal'
# DataEntries = [
#     'RealDataForSideband_Random15PercentRealDataForSignal',
# ]

# - Real data, 100%
DatasetType = 'RealData'
DataEntries = [
    'RealData',
    # 'Asimov',
]

RunScripts = []

if DoIndvFit:

    RecoDatasetListConfig = ConfigHelper.GetRecoDatasetList(DatasetType)
    TrueDatasetListConfig = ConfigHelper.GetTrueDatasetList()

    BaseConfig_Fitter = f'{WD}/base_configs/config_Fitter.yaml'
    BaseConfig_CalcXsec = f'{WD}/base_configs/config_CalcXsec.yaml'

    LLH_METHOD = LLH_METHOD_ForIndvFit

    FitConfigName = 'IndvFit'

    # Run scripts
    print('# Now writing run scripts to:')

    RunScript_Fitter = f'{RunScriptDir}/run_Fitter_{DatasetType}_{FitConfigName}_{LLH_METHOD}.sh'
    out_RunScript_Fitter = open(RunScript_Fitter, 'w')

    RunScript_ToyGenerator = f'{RunScriptDir}/run_ToyGenerator_{DatasetType}_{FitConfigName}_{LLH_METHOD}.sh'
    out_RunScript_ToyGenerator = open(RunScript_ToyGenerator, 'w')

    RunScript_CalcXsec = f'{RunScriptDir}/run_CalcXsec_{DatasetType}_{FitConfigName}_{LLH_METHOD}.sh'
    out_RunScript_CalcXsec = open(RunScript_CalcXsec, 'w')

    for IndvFit_XsecVariable in IndvFit_XsecVariables:

        # Writting config yamls

        # - Fitter
        outname_Fitter = f'{FitterConfigDir}/config_Fitter_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
        out_Fitter = open(outname_Fitter, 'w')
        ParameterSetListConfig = ConfigHelper.GetParametersetList_IndvFit(IndvFit_XsecVariable)
        FitSampleSetConfig_Reco = ConfigHelper.GetFitSampleSet_IndvFit(IndvFit_XsecVariable, IsReco=True)
        PlotGeneratorConfig_Reco = ConfigHelper.GetPlotGenerator_IndvFit(IndvFit_XsecVariable, IsReco=True)
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

        # - ToyGenerator
        #   - same as the Fitter config but with some additional lines
        outname_ToyGenerator = f'{ToyGeneratorConfigDir}/config_ToyGenerator_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
        out_ToyGenerator = open(outname_ToyGenerator, 'w')
        for line in open(outname_Fitter).readlines():
            out_ToyGenerator.write(line)
        out_ToyGenerator.write('''\n
statThrowConfig:
  enableStatThrowINToys: true
  enableEventMcThrow: true
''')
        out_ToyGenerator.close()
        print(f'# ToyGenerator config wrote:\n{outname_ToyGenerator}')

        # - CalcXsec
        outname_CalcXsec = f'{CalcXsecConfigDir}/config_CalcXsec_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
        out_CalcXsec = open(outname_CalcXsec, 'w')
        FitSampleSetConfig_True = ConfigHelper.GetFitSampleSet_IndvFit(IndvFit_XsecVariable, IsReco=False)
        PlotGeneratorConfig_True = ConfigHelper.GetPlotGenerator_IndvFit(IndvFit_XsecVariable, IsReco=False)

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

        # Loop over DataEntry defined in DatasetListConfig
        for DataEntry in DataEntries:

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

            # ToyGenerator
            # - preFit
            ToyGenerator_OutputFile = f'{ToyGeneratorOutputDir}/output_preFit_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
            ToyGenerator_LogFile = f'{LogBasedir}/log_ToyGenerator_preFit_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.log'

            cmd_ToyGenerator = f'''gundamToyGenerator -c {outname_ToyGenerator} \\
-f {Fitter_OutputFile} \\
-o {ToyGenerator_OutputFile} \\
-s 1  -t {NThread} \\
--use-prefit \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_ToyGenerator += f''' &> {ToyGenerator_LogFile}'''
            if RunOnBackground:
                cmd_ToyGenerator += ' &'
            out_RunScript_ToyGenerator.write(f'# ToyGenerator, {DataEntry}, {IndvFit_XsecVariable}, preFit\n')
            out_RunScript_ToyGenerator.write(cmd_ToyGenerator+'\n')

            # - postFit
            ToyGenerator_OutputFile = f'{ToyGeneratorOutputDir}/output_postFit_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
            ToyGenerator_LogFile = f'{LogBasedir}/log_ToyGenerator_postFit_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{IndvFit_XsecVariable}.log'

            cmd_ToyGenerator = f'''gundamToyGenerator -c {outname_ToyGenerator} \\
-f {Fitter_OutputFile} \\
-o {ToyGenerator_OutputFile} \\
-s 1  -t {NThread} \\
--use-bf \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_ToyGenerator += f''' &> {ToyGenerator_LogFile}'''
            if RunOnBackground:
                cmd_ToyGenerator += ' &'
            out_RunScript_ToyGenerator.write(f'# ToyGenerator, {DataEntry}, {IndvFit_XsecVariable}, postFit\n')
            out_RunScript_ToyGenerator.write(cmd_ToyGenerator+'\n')

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
    out_RunScript_ToyGenerator.close()
    out_RunScript_CalcXsec.close()

    RunScripts.append(RunScript_Fitter)
    RunScripts.append(RunScript_ToyGenerator)
    RunScripts.append(RunScript_CalcXsec)
        

if DoSimFit:

    RecoDatasetListConfig = ConfigHelper.GetRecoDatasetList(DatasetType)
    TrueDatasetListConfig = ConfigHelper.GetTrueDatasetList()

    BaseConfig_Fitter = f'{WD}/base_configs/config_Fitter.yaml'
    BaseConfig_CalcXsec = f'{WD}/base_configs/config_CalcXsec.yaml'

    LLH_METHOD = LLH_METHOD_ForSimFit

    FitConfigName = 'SimFit'
    if StatCovDiagOnly:
        FitConfigName = 'StatCovDiagOnly_'+FitConfigName

    # Run scripts
    print('# Now writing run scripts to:')

    RunScript_Fitter = f'{RunScriptDir}/run_Fitter_{DatasetType}_{FitConfigName}_{LLH_METHOD}.sh'
    out_RunScript_Fitter = open(RunScript_Fitter, 'w')

    RunScript_ToyGenerator = f'{RunScriptDir}/run_ToyGenerator_{DatasetType}_{FitConfigName}_{LLH_METHOD}.sh'
    out_RunScript_ToyGenerator = open(RunScript_ToyGenerator, 'w')

    RunScript_CalcXsec = f'{RunScriptDir}/run_CalcXsec_{DatasetType}_{FitConfigName}_{LLH_METHOD}.sh'
    out_RunScript_CalcXsec = open(RunScript_CalcXsec, 'w')


    for SimFit_XsecVariablePair in SimFit_XsecVariablePairs:

        SimFit_XsecVariable_X = SimFit_XsecVariablePair[0]
        SimFit_XsecVariable_Y = SimFit_XsecVariablePair[1]

        # Writting config yamls

        # - Fitter
        outname_Fitter = f'{FitterConfigDir}/config_Fitter_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml'
        out_Fitter = open(outname_Fitter, 'w')
        ParameterSetListConfig = ConfigHelper.GetParametersetList_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y)
        FitSampleSetConfig_Reco = ConfigHelper.GetFitSampleSet_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco=True)
        PlotGeneratorConfig_Reco = ConfigHelper.GetPlotGenerator_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco=True)
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
            elif '<TOY_THROW_CONFIG>' in l:
                if ForSimFitToy:
                    this_line = '''    enableStatThrowInToys: true
    enableEventMcThrow: false
    throwAsimovFitParameters: true
    IsSimFitToy: true
'''
                else:
                    this_line = '\n'

                if StatCovDiagOnly:
                    this_line += '\n    StatCovDiagOnly: true\n'
            else:
                this_line = l
            
            out_Fitter.write(this_line)
        out_Fitter.close()
        print(f'# Fitter config wrote:\n{outname_Fitter}')

        # - ToyGenerator
        #   - same as the Fitter config but with some additional lines
        outname_ToyGenerator = f'{ToyGeneratorConfigDir}/config_ToyGenerator_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml'
        out_ToyGenerator = open(outname_ToyGenerator, 'w')
        for line in open(outname_Fitter).readlines():
            out_ToyGenerator.write(line)
        out_ToyGenerator.write('''\n
statThrowConfig:
  enableStatThrowInToys: true
  enableEventMcThrow: true
''')
        out_ToyGenerator.close()
        print(f'# ToyGenerator config wrote:\n{outname_ToyGenerator}')

        # - CalcXsec

        outname_CalcXsec = f'{CalcXsecConfigDir}/config_CalcXsec_{DatasetType}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml'
        out_CalcXsec = open(outname_CalcXsec, 'w')
        FitSampleSetConfig_True = ConfigHelper.GetFitSampleSet_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco=False)
        PlotGeneratorConfig_True = ConfigHelper.GetPlotGenerator_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco=False)

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

        for DataEntry in DataEntries:

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

            # ToyGenerator
            # - preFit
            ToyGenerator_OutputFile = f'{ToyGeneratorOutputDir}/output_preFit_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.root'
            ToyGenerator_LogFile = f'{LogBasedir}/log_ToyGenerator_preFit_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.log'

            cmd_ToyGenerator = f'''gundamToyGenerator -c {outname_ToyGenerator} \\
-f {Fitter_OutputFile} \\
-o {ToyGenerator_OutputFile} \\
-s 1  -t {NThread} \\
--use-prefit \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_ToyGenerator += f''' &> {ToyGenerator_LogFile}'''
            if RunOnBackground:
                cmd_ToyGenerator += ' &'
            out_RunScript_ToyGenerator.write(f'# ToyGenerator, preFit\n')
            out_RunScript_ToyGenerator.write(cmd_ToyGenerator+'\n')

            # - postFit
            ToyGenerator_OutputFile = f'{ToyGeneratorOutputDir}/output_postFit_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.root'
            ToyGenerator_LogFile = f'{LogBasedir}/log_ToyGenerator_postFit_{DataEntry}_{FitConfigName}_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.log'

            cmd_ToyGenerator = f'''gundamToyGenerator -c {outname_ToyGenerator} \\
-f {Fitter_OutputFile} \\
-o {ToyGenerator_OutputFile} \\
-s 1  -t {NThread} \\
--use-bf \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_ToyGenerator += f''' &> {ToyGenerator_LogFile}'''
            if RunOnBackground:
                cmd_ToyGenerator += ' &'
            out_RunScript_ToyGenerator.write(f'# ToyGenerator, preFit\n')
            out_RunScript_ToyGenerator.write(cmd_ToyGenerator+'\n')

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

    # Run scripts
    RunScripts.append(RunScript_Fitter)
    RunScripts.append(RunScript_ToyGenerator)
    RunScripts.append(RunScript_CalcXsec)

    # Close
    out_RunScript_Fitter.close()
    out_RunScript_ToyGenerator.close()

print('# Printing all run scripts that are generated..')
for RunScript in RunScripts:
    print(f'source {RunScript}')
