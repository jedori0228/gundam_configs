def GetRecoDatasetList(DatasetType):
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
def GetParametersetList_IndvFit(IndvFit_XsecVariable, PSetName=''):
    if PSetName=='':
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_ParameterSetList/parameterSetList_{IndvFit_XsecVariable}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_ParameterSetList/{PSetName}/parameterSetList_{IndvFit_XsecVariable}.yaml"'''
def GetRecoFitSampleSet_IndvFit(IndvFit_XsecVariable, FitSampleName=''):
    if FitSampleName=='':
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/fitSamples_Reco{IndvFit_XsecVariable}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/{FitSampleName}/fitSamples_Reco{IndvFit_XsecVariable}.yaml"'''
def GetTrueFitSampleSet_IndvFit(IndvFit_XsecVariable, FitSampleName=''):
    if FitSampleName=='':
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/fitSamples_True{IndvFit_XsecVariable}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/{FitSampleName}/fitSamples_True{IndvFit_XsecVariable}.yaml"'''
def GetRecoPlotGenerator_IndvFit(IndvFit_XsecVariable, PlotConfigName=''):
    if PlotConfigName=='':
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/plotConfigs_Reco{IndvFit_XsecVariable}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/{PlotConfigName}/plotConfigs_Reco{IndvFit_XsecVariable}.yaml"'''
def GetTruePlotGenerator_IndvFit(IndvFit_XsecVariable, PlotConfigName=''):
    if PlotConfigName=='':
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/plotConfigs_True{IndvFit_XsecVariable}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/{PlotConfigName}/plotConfigs_True{IndvFit_XsecVariable}.yaml"'''

# SimFit
def GetParametersetList_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, PSetName=''):
    if PSetName=='':
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_ParameterSetList/parameterSetList_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_ParameterSetList/{PSetName}/parameterSetList_{SimFit_XsecVariable_X}_and_{SimFit_XsecVariable_Y}.yaml"'''
def GetFitSampleSet_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco):
    if IsReco:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/fitSamples_Reco{SimFit_XsecVariable_X}_and_Reco{SimFit_XsecVariable_Y}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_FitSampleSet/fitSamples_True{SimFit_XsecVariable_X}_and_True{SimFit_XsecVariable_Y}.yaml"'''
def GetPlotGenerator_SimFit(SimFit_XsecVariable_X, SimFit_XsecVariable_Y, IsReco):
    if IsReco:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/plotConfigs_Reco{SimFit_XsecVariable_X}_and_Reco{SimFit_XsecVariable_Y}.yaml"'''
    else:
        return f'''"${{GUNDAM_CONFIG_DIR}}/Configs_PlotGenerator/plotConfigs_True{SimFit_XsecVariable_X}_and_True{SimFit_XsecVariable_Y}.yaml"'''