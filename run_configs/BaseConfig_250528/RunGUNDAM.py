import os
import ConfigHelper

# Config
JobName = '250528_BeamWidthCorrection'
JobName = '250627_BadRegionRejection'


ConfigType = 'BaseConfig_250528'

# Base directories
GUNDAMDIR = os.environ['GUNDAM_CONFIG_DIR']
WD = f'{GUNDAMDIR}/run_configs/{ConfigType}'

# Number of toys
NToys = 1000
NToyFits = 1000

# Config directory
FitterConfigDir = f'{WD}/configs/Fitter'
ToyGeneratorConfigDir = f'{WD}/configs/ToyGenerator'
CalcXsecConfigDir = f'{WD}/configs/CalcXsec'
os.system(f'mkdir -p {FitterConfigDir}')
os.system(f'mkdir -p {ToyGeneratorConfigDir}')
os.system(f'mkdir -p {CalcXsecConfigDir}')

# Logging
WriteLog = False
LogBasedir = f'{WD}/logs'

# Define output directories
GUNDAMOutputBasedir = f'{WD}/output/{JobName}'

FitterOutputDir = f'{GUNDAMOutputBasedir}/Fitter'
ToyGeneratorOutputDir = f'{GUNDAMOutputBasedir}/ToyGenerator'
CalcXsecOutputDir = f'{GUNDAMOutputBasedir}/CalcXsec'
ToyFitOutputDir = f'{GUNDAMOutputBasedir}/ToyFit'
RunScriptDir = f'{WD}/run_scripts'
os.system(f'mkdir -p {FitterOutputDir}')
os.system(f'mkdir -p {ToyGeneratorOutputDir}')
os.system(f'mkdir -p {CalcXsecOutputDir}')
os.system(f'mkdir -p {ToyFitOutputDir}')
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
# LLH_METHOD_ForSimFit = 'PoissonLLH'
# LLH_METHOD_ForSimFit = 'BarlowLLH'

# Datasets

# - Fake data
# DatasetType = 'FakeData'
# DataEntries = [
#     'Asimov',
#     # 'FakeDataFromMCSubset',
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
]

DatasetListConfig = ConfigHelper.GetDatasetList(DatasetType) 

BaseConfig_Fitter = f'{WD}/base_configs/config_Fitter_FluxHPPCA_FSIMultisigma_BackgroundFit.yaml'
BaseConfig_CalcXsec = f'{WD}/base_configs/config_CalcXsec_FluxHPPCA_FSIMultisigma_BackgroundFit.yaml'

RunScripts = []

if DoIndvFit:

    LLH_METHOD = LLH_METHOD_ForIndvFit

    # Run scripts
    print('# Now writing run scripts to:')

    RunScript_Fitter = f'{RunScriptDir}/run_Fitter_{DatasetType}_IndvFit_{LLH_METHOD}.sh'
    out_RunScript_Fitter = open(RunScript_Fitter, 'w')

    RunScript_ToyGenerator = f'{RunScriptDir}/run_ToyGenerator_{DatasetType}_IndvFit_{LLH_METHOD}.sh'
    out_RunScript_ToyGenerator = open(RunScript_ToyGenerator, 'w')

    RunScript_CalcXsec = f'{RunScriptDir}/run_CalcXsec_{DatasetType}_IndvFit_{LLH_METHOD}.sh'
    out_RunScript_CalcXsec = open(RunScript_CalcXsec, 'w')

    RunScript_ToyFit = f'{RunScriptDir}/run_ToyFit_{DatasetType}_IndvFit_{LLH_METHOD}.sh'
    out_RunScript_ToyFit = open(RunScript_ToyFit, 'w')
    out_RunScript_ToyFit.write(f'NToyFits={NToyFits}\n')

    for IndvFit_XsecVariable in IndvFit_XsecVariables:

        # Writting config yamls

        # - Fitter
        outname_Fitter = f'{FitterConfigDir}/config_Fitter_{DatasetType}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
        out_Fitter = open(outname_Fitter, 'w')
        ParameterSetListConfig = ConfigHelper.GetParametersetList_IndvFit(IndvFit_XsecVariable)
        FitSampleSetConfig_Reco = ConfigHelper.GetFitSampleSet_IndvFit(IndvFit_XsecVariable, IsReco=True)
        PlotGeneratorConfig_Reco = ConfigHelper.GetPlotGenerator_IndvFit(IndvFit_XsecVariable, IsReco=True)
        for l in open(BaseConfig_Fitter):
            this_line = l
            if '<LLH_METHOD>' in l:
                this_line = l.replace('<LLH_METHOD>', LLH_METHOD)
            elif '<DATASETLIST_CONFIG>' in l:
                this_line = l.replace('<DATASETLIST_CONFIG>', DatasetListConfig)
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
        outname_ToyGenerator = f'{ToyGeneratorConfigDir}/config_ToyGenerator_{DatasetType}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
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
        outname_CalcXsec = f'{CalcXsecConfigDir}/config_CalcXsec_{DatasetType}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
        out_CalcXsec = open(outname_CalcXsec, 'w')
        FitSampleSetConfig_True = ConfigHelper.GetFitSampleSet_IndvFit(IndvFit_XsecVariable, IsReco=False)
        PlotGeneratorConfig_True = ConfigHelper.GetPlotGenerator_IndvFit(IndvFit_XsecVariable, IsReco=False)

        for l in open(BaseConfig_CalcXsec):
            this_line = l
            if '<LLH_METHOD>' in l:
                this_line = l.replace('<LLH_METHOD>', LLH_METHOD)
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

        # Loop over DataEntry defined in DatasetListConfig
        for DataEntry in DataEntries:

            print(f'# - DataEntry = {DataEntry}')

            # Fitter
            Fitter_OutputFile = f'{FitterOutputDir}/output_{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
            Fitter_LogFile = f'{LogBasedir}/log_Fitter_{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.log'
            cmd_Fitter = f'''gundamFitter -c {outname_Fitter} \\
-o {Fitter_OutputFile} \\
-t 8 --pca \\
--use-data-entry {DataEntry}'''
            if WriteLog:
                cmd_Fitter += f''' &> {Fitter_LogFile}\n'''
            out_RunScript_Fitter.write(f'# Fitter, {DataEntry}, {IndvFit_XsecVariable}\n')
            out_RunScript_Fitter.write(cmd_Fitter+'\n')

            # ToyGenerator
            # - preFit
            ToyGenerator_OutputFile = f'{ToyGeneratorOutputDir}/output_preFit_{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
            ToyGenerator_LogFile = f'{LogBasedir}/log_ToyGenerator_preFit_{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.log'

            cmd_ToyGenerator = f'''gundamToyGenerator -c {outname_ToyGenerator} \\
-f {Fitter_OutputFile} \\
-o {ToyGenerator_OutputFile} \\
-s 1  -t 8 \\
--use-prefit \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_ToyGenerator += f''' &> {ToyGenerator_LogFile}\n'''
            out_RunScript_ToyGenerator.write(f'# ToyGenerator, {DataEntry}, {IndvFit_XsecVariable}, preFit\n')
            out_RunScript_ToyGenerator.write(cmd_ToyGenerator+'\n')

            # - postFit
            ToyGenerator_OutputFile = f'{ToyGeneratorOutputDir}/output_postFit_{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
            ToyGenerator_LogFile = f'{LogBasedir}/log_ToyGenerator_postFit_{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.log'

            cmd_ToyGenerator = f'''gundamToyGenerator -c {outname_ToyGenerator} \\
-f {Fitter_OutputFile} \\
-o {ToyGenerator_OutputFile} \\
-s 1  -t 8 \\
--use-bf \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_ToyGenerator += f''' &> {ToyGenerator_LogFile}\n'''
            out_RunScript_ToyGenerator.write(f'# ToyGenerator, {DataEntry}, {IndvFit_XsecVariable}, postFit\n')
            out_RunScript_ToyGenerator.write(cmd_ToyGenerator+'\n')

            # CalcXsec
            CalcXsec_OutputFile = f'{CalcXsecOutputDir}/output_{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
            CalcXsec_LogFile = f'{LogBasedir}/log_CalcXsec_{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}.log'
            cmd_CalcXsec = f'''gundamCalcXsec -c {outname_CalcXsec} \\
-f {Fitter_OutputFile} \\
-o {CalcXsec_OutputFile} \\
-s 1 -t 8 \\
--use-bf-as-xsec \\
--TurnRecoOnlyOff \\
--fitsample-config {FitSampleSetConfig_True} \\
--plot-config {PlotGeneratorConfig_True} \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_CalcXsec += f''' &> {CalcXsec_LogFile}\n'''
            out_RunScript_CalcXsec.write(f'# CalcXsec, {DataEntry}, {IndvFit_XsecVariable}\n')
            out_RunScript_CalcXsec.write(cmd_CalcXsec+'\n')

            # ToyFit
            out_RunScript_ToyFit.write(f'# ToyFit, {DataEntry}, {IndvFit_XsecVariable}\n')
            ThisToyFitOutputDir = f'{ToyFitOutputDir}/{DataEntry}_IndvFit_{LLH_METHOD}_{IndvFit_XsecVariable}'
            os.system(f'mkdir -p {ThisToyFitOutputDir}')
            cmd_ToyFit = f'''for ((i_toy=0; i_toy<NToyFits; i_toy++))
do
  gundamFitter -c {outname_Fitter} \\
  -o {ThisToyFitOutputDir}/output_Toy_${{i_toy}}.root \\
  -t 8 --pca \\
  --toy ${{i_toy}}
done'''
            out_RunScript_ToyFit.write(cmd_ToyFit+'\n')

    # Close
    out_RunScript_Fitter.close()
    out_RunScript_ToyGenerator.close()
    out_RunScript_CalcXsec.close()
    out_RunScript_ToyFit.close()

    RunScripts.append(RunScript_Fitter)
    RunScripts.append(RunScript_ToyGenerator)
    RunScripts.append(RunScript_CalcXsec)
    RunScripts.append(RunScript_ToyFit)
        

if DoSimFit:

    LLH_METHOD = LLH_METHOD_ForSimFit

    # Run scripts
    print('# Now writing run scripts to:')

    RunScript_Fitter = f'{RunScriptDir}/run_Fitter_{DatasetType}_SimFit_{LLH_METHOD}.sh'
    out_RunScript_Fitter = open(RunScript_Fitter, 'w')

    RunScript_ToyGenerator = f'{RunScriptDir}/run_ToyGenerator_{DatasetType}_SimFit_{LLH_METHOD}.sh'
    out_RunScript_ToyGenerator = open(RunScript_ToyGenerator, 'w')

    RunScript_CalcXsec = f'{RunScriptDir}/run_CalcXsec_{DatasetType}_SimFit_{LLH_METHOD}.sh'
    out_RunScript_CalcXsec = open(RunScript_CalcXsec, 'w')


    for SimFit_XsecVariablePair in SimFit_XsecVariablePairs:

        SimFit_XsecVariable_X = SimFit_XsecVariablePair[0]
        SimFit_XsecVariable_Y = SimFit_XsecVariablePair[1]

        # Writting config yamls

        # - Fitter
        outname_Fitter = f'{FitterConfigDir}/config_Fitter_{DatasetType}_SimFit_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml'
        out_Fitter = open(outname_Fitter, 'w')
        ParameterSetListConfig = ConfigHelper.GetParametersetList_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y)
        FitSampleSetConfig_Reco = ConfigHelper.GetFitSampleSet_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco=True)
        PlotGeneratorConfig_Reco = ConfigHelper.GetPlotGenerator_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco=True)
        for l in open(BaseConfig_Fitter):
            this_line = l
            if '<LLH_METHOD>' in l:
                this_line = l.replace('<LLH_METHOD>', LLH_METHOD)
            elif '<DATASETLIST_CONFIG>' in l:
                this_line = l.replace('<DATASETLIST_CONFIG>', DatasetListConfig)
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
        outname_ToyGenerator = f'{ToyGeneratorConfigDir}/config_ToyGenerator_{DatasetType}_SimFit_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml'
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
        #   - This should be done per-variable but using sim parameter set
        for IndvFit_XsecVariable in SimFit_XsecVariablePair:
            outname_CalcXsec = f'{CalcXsecConfigDir}/config_CalcXsec_{DatasetType}_SimFit_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
            out_CalcXsec = open(outname_CalcXsec, 'w')
            FitSampleSetConfig_True = ConfigHelper.GetFitSampleSet_IndvFit(IndvFit_XsecVariable, IsReco=False)
            PlotGeneratorConfig_True = ConfigHelper.GetPlotGenerator_IndvFit(IndvFit_XsecVariable, IsReco=False)

            for l in open(BaseConfig_CalcXsec):
                this_line = l
                if '<LLH_METHOD>' in l:
                    this_line = l.replace('<LLH_METHOD>', LLH_METHOD)
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
            Fitter_OutputFile = f'{FitterOutputDir}/output_{DataEntry}_SimFit_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.root'
            Fitter_LogFile = f'{LogBasedir}/log_Fitter_{DataEntry}_SimFit_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.log'
            cmd_Fitter = f'''gundamFitter -c {outname_Fitter} \\
-o {Fitter_OutputFile} \\
-t 8 --pca \\
--use-data-entry {DataEntry}'''
            if WriteLog:
                cmd_Fitter += f''' &> {Fitter_LogFile}\n'''
            out_RunScript_Fitter.write(f'# Fitter\n')
            out_RunScript_Fitter.write(cmd_Fitter+'\n')

            # ToyGenerator
            # - preFit
            ToyGenerator_OutputFile = f'{ToyGeneratorOutputDir}/output_preFit_{DataEntry}_SimFit_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.root'
            ToyGenerator_LogFile = f'{LogBasedir}/log_ToyGenerator_preFit_{DataEntry}_SimFit_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.log'

            cmd_ToyGenerator = f'''gundamToyGenerator -c {outname_ToyGenerator} \\
-f {Fitter_OutputFile} \\
-o {ToyGenerator_OutputFile} \\
-s 1  -t 8 \\
--use-prefit \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_ToyGenerator += f''' &> {ToyGenerator_LogFile}\n'''
            out_RunScript_ToyGenerator.write(f'# ToyGenerator, preFit\n')
            out_RunScript_ToyGenerator.write(cmd_ToyGenerator+'\n')

            # - postFit
            ToyGenerator_OutputFile = f'{ToyGeneratorOutputDir}/output_postFit_{DataEntry}_SimFit_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.root'
            ToyGenerator_LogFile = f'{LogBasedir}/log_ToyGenerator_postFit_{DataEntry}_SimFit_{LLH_METHOD}_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.log'

            cmd_ToyGenerator = f'''gundamToyGenerator -c {outname_ToyGenerator} \\
-f {Fitter_OutputFile} \\
-o {ToyGenerator_OutputFile} \\
-s 1  -t 8 \\
--use-bf \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
            if WriteLog:
                cmd_ToyGenerator += f''' &> {ToyGenerator_LogFile}\n'''
            out_RunScript_ToyGenerator.write(f'# ToyGenerator, preFit\n')
            out_RunScript_ToyGenerator.write(cmd_ToyGenerator+'\n')

            # CalcXsec
            for IndvFit_XsecVariable in SimFit_XsecVariablePair:
                outname_CalcXsec = f'{CalcXsecConfigDir}/config_CalcXsec_{DatasetType}_SimFit_{LLH_METHOD}_{IndvFit_XsecVariable}.yaml'
                FitSampleSetConfig_True = ConfigHelper.GetFitSampleSet_IndvFit(IndvFit_XsecVariable, IsReco=False)
                PlotGeneratorConfig_True = ConfigHelper.GetPlotGenerator_IndvFit(IndvFit_XsecVariable, IsReco=False)
                
                CalcXsec_OutputFile = f'{CalcXsecOutputDir}/output_{DataEntry}_SimFit_{LLH_METHOD}_{IndvFit_XsecVariable}.root'
                CalcXsec_LogFile = f'{LogBasedir}/log_CalcXsec_{DataEntry}_SimFit_{LLH_METHOD}_{IndvFit_XsecVariable}.log'
                cmd_CalcXsec = f'''gundamCalcXsec -c {outname_CalcXsec} \\
-f {Fitter_OutputFile} \\
-o {CalcXsec_OutputFile} \\
-s 1 -t 8 \\
--use-bf-as-xsec \\
--TurnRecoOnlyOff \\
--fitsample-config {FitSampleSetConfig_True} \\
--plot-config {PlotGeneratorConfig_True} \\
--use-data-entry {DataEntry} \\
-n {NToys}'''
                if WriteLog:
                    cmd_CalcXsec += f''' &> {CalcXsec_LogFile}\n'''
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
