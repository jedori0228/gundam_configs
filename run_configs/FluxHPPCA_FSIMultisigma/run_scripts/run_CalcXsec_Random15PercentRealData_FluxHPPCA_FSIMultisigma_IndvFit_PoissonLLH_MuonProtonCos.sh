# CalcXsec
gundamCalcXsec -c /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/configs/CalcXsec/config_CalcXsec_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_MuonProtonCos.yaml \
-f /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/output/241111_PreparingSignalUnboxing/Fitter/output_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_MuonProtonCos.root \
-o /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/output/241111_PreparingSignalUnboxing/CalcXsec/output_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_MuonProtonCos.root \
-s 1 -t 8 \
--use-bf-as-xsec \
--TurnG4Off \
--fitsample-config "${GUNDAM_INPUTS_DIR}/Configs_FitSampleSet/fitSamples_TrueMuonProtonCos.yaml" \
--plot-config "${GUNDAM_INPUTS_DIR}/Configs_PlotGenerator/plotConfigs_TrueMuonProtonCos.yaml" \
--use-data-entry Random15PercentRealData \
-n 10000
