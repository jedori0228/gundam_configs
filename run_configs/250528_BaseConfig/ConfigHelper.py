def GetDatasetList(DatasetType):
    if DatasetType=='FakeData':
        return '''"${GUNDAM_CONFIG_DIR}/Configs_DataSetList/dataSetListConfig_FakeData.yaml"'''
    elif DatasetType=='Random15PercentRealData':
        return '''"${GUNDAM_CONFIG_DIR}/Configs_DataSetList/dataSetListConfig_Random15PercentRealData.yaml"'''
    elif DatasetType=='RealDataForSideband_FakeDataForSignal':
        return '''"${GUNDAM_CONFIG_DIR}/Configs_DataSetList/dataSetListConfig_RealDataForSideband_FakeDataForSignal.yaml"'''
    elif DatasetType=='RealDataForSideband_Random15PercentRealDataForSignal':
        return '''"${GUNDAM_CONFIG_DIR}/Configs_DataSetList/dataSetListConfig_RealDataForSideband_Random15PercentRealDataForSignal.yaml"'''
    elif DatasetType=='RealData':
        return '''"${GUNDAM_CONFIG_DIR}/Configs_DataSetList/dataSetListConfig_RealData.yaml"'''

def GetTrueDatasetList():
    return '''"${GUNDAM_CONFIG_DIR}/Configs_DataSetList/dataSetListConfig_True.yaml"'''

# IndvFit
def GetParametersetList_IndvFit(IndvFit_XsecVariable):
    return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_ParameterSetList/parameterSetList_{IndvFit_XsecVariable}.yaml"'''
def GetFitSampleSet_IndvFit(IndvFit_XsecVariable, IsReco):
    if IsReco:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/fitSamples_Reco{IndvFit_XsecVariable}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/fitSamples_True{IndvFit_XsecVariable}.yaml"'''
def GetPlotGenerator_IndvFit(IndvFit_XsecVariable, IsReco):
    if IsReco:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/plotConfigs_Reco{IndvFit_XsecVariable}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/plotConfigs_True{IndvFit_XsecVariable}.yaml"'''

# SimFit
def GetParametersetList_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y):
    return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_ParameterSetList/parameterSetList_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml"'''
def GetFitSampleSet_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco):
    if IsReco:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/fitSamples_Reco{SimFit_XsecVariable_X}_and_Reco{SimFit_XsecVariable_Y}.yaml"'''
    else:
        raise ValueError('NO True GetFitSampleSet_SimFit')
def GetPlotGenerator_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco):
    if IsReco:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/plotConfigs_Reco{SimFit_XsecVariable_X}_and_Reco{SimFit_XsecVariable_Y}.yaml"'''
    else:
        raise ValueError('NO True GetPlotGenerator_SimFit')