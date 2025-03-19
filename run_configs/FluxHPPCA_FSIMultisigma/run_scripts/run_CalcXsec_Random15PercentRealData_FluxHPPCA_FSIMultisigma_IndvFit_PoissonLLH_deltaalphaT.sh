# CalcXsec
gundamCalcXsec -c /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/configs/CalcXsec/config_CalcXsec_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaalphaT.yaml \
-f /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/output/241111_PreparingSignalUnboxing/Fitter/output_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaalphaT.root \
-o /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/output/241111_PreparingSignalUnboxing/CalcXsec/output_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaalphaT.root \
-s 1 -t 8 \
--use-bf-as-xsec \
--TurnG4Off \
--fitsample-config "${GUNDAM_INPUTS_DIR}/Configs_FitSampleSet/fitSamples_TruedeltaalphaT.yaml" \
--plot-config "${GUNDAM_INPUTS_DIR}/Configs_PlotGenerator/plotConfigs_TruedeltaalphaT.yaml" \
--use-data-entry Random15PercentRealData \
-n 10000
