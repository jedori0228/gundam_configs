std::vector<std::string> GetDetSystMultisigmaKnobNames();

void GenerateDetSystCov()
{

  std::vector<std::string> detNames = GetDetSystMultisigmaKnobNames();

  const unsigned int NKnob = detNames.size();

  // Make the covariance matrix: ((0,1), (1,0))
  TFile *file = new TFile("gundaminput_detsyst.root","RECREATE");

  file->cd();

  TMatrixTSym<double> detsyst_cov(NKnob);
  for (int i = 0; i < NKnob; i++) {
    detsyst_cov(i, i) = 1.0;
  }
  detsyst_cov.Write("detsyst_cov");

  TObjArray detsyst_param_names;
  for(const auto& name: detNames){
    detsyst_param_names.Add( new TObjString(name.c_str()) );
    std::cout << "@@ Wrigin " << name << std::endl;
  }
  file->WriteObjectAny( &detsyst_param_names, "TObjArray", "detsyst_param_names" );

  TVectorD detsyst_param_prior(NKnob);
  TVectorD detsyst_param_lb(NKnob);
  TVectorD detsyst_param_ub(NKnob);
  for(int i=0; i<NKnob; i++){
    detsyst_param_prior[i] = 0.;
    detsyst_param_lb[i] = -3.;
    detsyst_param_ub[i] = +3.;
  }
  detsyst_param_prior.Write("detsyst_param_prior");
  detsyst_param_lb.Write("detsyst_param_lb");
  detsyst_param_ub.Write("detsyst_param_ub");

  file->Close();
}

std::vector<std::string> GetDetSystMultisigmaKnobNames(){

  return {
"NuMIXSecFrontIndPlaneGainSyst",
"NuMIXSecFrontIndPlaneNoiseSyst",
"NuMIXSecFrontIndPlaneSignalShapeFittedSyst",
"NuMIXSecMiddleIndPlaneTransparencySyst",
"NuMIXSecCaloGainSyst",
"NuMIXSecLifetimeSyst",
//NEW
"NuMIXSecTrackSplitSyst",
"NuMIXSecProtonEffSyst",
  };


}
