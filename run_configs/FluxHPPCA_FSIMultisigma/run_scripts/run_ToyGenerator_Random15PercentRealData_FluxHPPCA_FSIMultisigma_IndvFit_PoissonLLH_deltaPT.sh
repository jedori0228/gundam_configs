# ToyGenerator, preFit
gundamToyGenerator -c /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/configs/ToyGenerator/config_ToyGenerator_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaPT.yaml \
-f /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/output/241111_PreparingSignalUnboxing/Fitter/output_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaPT.root \
-o /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/output/241111_PreparingSignalUnboxing/ToyGenerator/output_preFit_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaPT.root \
-s 1  -t 8 \
--use-prefit \
--use-data-entry Random15PercentRealData \
-n 10000
# ToyGenerator, preFit
gundamToyGenerator -c /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/configs/ToyGenerator/config_ToyGenerator_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaPT.yaml \
-f /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/output/241111_PreparingSignalUnboxing/Fitter/output_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaPT.root \
-o /Users/jskim/Documents/Neutrino/ICARUS/GUNDAM-1.9.X/work/run_configs/FluxHPPCA_FSIMultisigma/output/241111_PreparingSignalUnboxing/ToyGenerator/output_postFit_Random15PercentRealData_FluxHPPCA_FSIMultisigma_IndvFit_PoissonLLH_deltaPT.root \
-s 1  -t 8 \
--use-bf \
--use-data-entry Random15PercentRealData \
-n 10000
