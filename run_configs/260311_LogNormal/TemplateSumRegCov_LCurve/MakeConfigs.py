import os

VariableNames = [
    'MuonCos_and_MuonProtonCos',
    'deltaPT_and_deltaalphaT',
]

GUNDAM_CONFIG_DIR = os.environ["GUNDAM_CONFIG_DIR"]

WD = f'{GUNDAM_CONFIG_DIR}/run_configs/260311_LogNormal/TemplateSumRegCov_LCurve'

Log10Strenght_min = -1.20
Log10Strenght_max = 1.00
Log10Strenght_d = 0.001

Log10Strenghts = []
tmp_Log10Strenght = Log10Strenght_min
while tmp_Log10Strenght<=Log10Strenght_max+0.5*Log10Strenght_d:
  Log10Strenghts.append(tmp_Log10Strenght)
  tmp_Log10Strenght += Log10Strenght_d

CommandCounter = 0

for VariableName in VariableNames:

    BaseConfig = open(f'{WD}/base_Fitter_{VariableName}.yaml').readlines()

    for Log10Strenght in Log10Strenghts:

        Strenght = pow(10., Log10Strenght)

        RegStrName = f'{Log10Strenght:1.3f}'
        CovMatHistName = f'SumRegCovMat_Log10Strength{RegStrName}'

        FitterConfigFilePath = f'{WD}/configs/config_Fitter_{VariableName}_Log10Strength{RegStrName}.yaml'
        FitterOutputFilePath = f'{WD}/outputs/output_Fitter_{VariableName}_Log10Strength{RegStrName}.root'

        out_config = open(FitterConfigFilePath, 'w')
        for line in BaseConfig:
          newline = line
          if '<TemplateSumRegCov_LCurve_COVMAT_NAME>' in line:
            newline = newline.replace('<TemplateSumRegCov_LCurve_COVMAT_NAME>', CovMatHistName)
          out_config.write(newline)
        out_config.close()

        # For grid

        grid_ConfigPath = '${GUNDAM_CONFIG_DIR}/run_configs/260311_LogNormal/TemplateSumRegCov_LCurve/configs/config_Fitter_%s_Log10Strength%s.yaml'%(VariableName, RegStrName)
        grid_OutputName = f'output_Fitter_{VariableName}_Log10Strength{RegStrName}.root'

        grid_cmd = 'gundamFitter -c %s -o ${OutputFilePath} -t 1 --pca --use-data-entry RealData'%(grid_ConfigPath)

        out_grid_command = open(f'{WD}/commands/run_{CommandCounter}.sh', 'w')
        out_grid_command.write('export OutputFileName=%s\n'%(grid_OutputName))
        out_grid_command.write('export OutputFilePath=${GUNDAM_DIR}/${OutputFileName}\n')
        out_grid_command.write('echo "@ OutputFileName: ${OutputFileName}"\n')
        out_grid_command.write('echo "@ OutputFilePath: ${OutputFilePath}"\n')
        out_grid_command.write(grid_cmd+'\n')
        out_grid_command.close()

        CommandCounter += 1
