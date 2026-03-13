void MakeCovMat(){

  std::vector<TString> VariableNames = {
"MuonCos",
"MuonProtonCos",
"deltaPT",
"deltaalphaT",
  };

  std::vector<int> NBins = {
8,
10,
7,
6
  };

  TRandom3 my_rand(1);
  
  double Log10Strength_min = -1.20;
  double Log10Strength_max = 1.00;
  double Log10Strength_d = 0.001;
  vector<double> Log10Strengths;
  double tmp_Log10Strength = Log10Strength_min;
  while(tmp_Log10Strength<=Log10Strength_max+0.5*Log10Strength_d){
    Log10Strengths.push_back(tmp_Log10Strength);
    tmp_Log10Strength += Log10Strength_d;
  }
  std::cout << "@ Number of lambda = " << Log10Strengths.size() << std::endl;
  
  for(int i_var=0; i_var<VariableNames.size(); i_var++){

    TString VariableName = VariableNames[i_var];
    int NBin = NBins[i_var];

    TFile *out = new TFile("SumRegCovMat_"+VariableName+".root", "RECREATE");

    for(int i_s=0; i_s<Log10Strengths.size(); i_s++){

      double Log10Strength = Log10Strengths[i_s];
      double Strength = pow(10., Log10Strength);

      TString RegStrName = TString::Format("%1.3f", Log10Strength);

      TMatrixTSym<double> xsec_cov(NBin);
      for(int ix=0; ix<NBin; ix++){
        for(int iy=0; iy<NBin; iy++){
          xsec_cov(ix, iy) = Strength;
          if(ix==iy){
            xsec_cov(ix, iy) *= (1 + my_rand.Rndm()*1E-3);
          }
        }
      }
      xsec_cov.Invert();
      xsec_cov.SetTol(1E-20);
      out->cd();
      xsec_cov.Write("SumRegCovMat_Log10Strength"+RegStrName);

    }
    // Prior vector
    TVectorD param_prior(NBin);
    for(int j=0; j<NBin; j++) param_prior[j] = 0;
    param_prior.Write("PriorVals");

    out->Close();

  }

}
