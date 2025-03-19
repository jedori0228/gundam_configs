void GenerateNuMIHPPCASystCov()
{

  //const unsigned int NPCA = 175;
  const unsigned int NPCA = 15;

  // Make the covariance matrix: ((0,1), (1,0))
  TFile *file = new TFile("gundaminput_numihppcasyst.root","RECREATE");
  file->cd();

  TMatrixTSym<double> numihppcasyst_cov(NPCA);
  for (int i = 0; i < NPCA; i++) {
    numihppcasyst_cov(i, i) = 1.0;
  }
  numihppcasyst_cov.Write("numihppcasyst_cov");

  TObjArray numihppcasyst_param_names;
  for(int i=0; i<NPCA; i++){
    std::string name = "numi_pc_"+std::to_string(i);
    numihppcasyst_param_names.Add( new TObjString(name.c_str()) );
    std::cout << "@@ Wriging " << name << std::endl;
  }
  file->WriteObjectAny( &numihppcasyst_param_names, "TObjArray", "numihppcasyst_param_names" );

  TVectorD numihppcasyst_param_prior(NPCA);
  TVectorD numihppcasyst_param_lb(NPCA);
  TVectorD numihppcasyst_param_ub(NPCA);
  for(int i=0; i<NPCA; i++){
    numihppcasyst_param_prior[i] = 0.;
    numihppcasyst_param_lb[i] = -3.;
    numihppcasyst_param_ub[i] = +3.;
  }
  numihppcasyst_param_prior.Write("numihppcasyst_param_prior");
  numihppcasyst_param_lb.Write("numihppcasyst_param_lb");
  numihppcasyst_param_ub.Write("numihppcasyst_param_ub");

  file->Close();
}

