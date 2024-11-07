std::vector<std::string> GetGENIEMorphKnobNames();
std::vector<std::string> GetGENIEMultisigmaKnobNames();

void GenerateGENIESystCov()
{

  std::vector<std::string> genieMultisigmaNames = GetGENIEMultisigmaKnobNames();
  std::vector<std::string> genieMorphNames = GetGENIEMorphKnobNames();

  std::vector<std::string> KnobNames;
  KnobNames.insert(KnobNames.end(), genieMultisigmaNames.begin(), genieMultisigmaNames.end());
  KnobNames.insert(KnobNames.end(), genieMorphNames.begin(), genieMorphNames.end());
  const unsigned int NKnob = KnobNames.size();

  std::string outputname = "gundaminput_geniesyst.root";

  // Make the covariance matrix: ((0,1), (1,0))
  TFile *file = new TFile(outputname.c_str(),"RECREATE");
  file->cd();

  std::cout << "@@ Prefit error by covariance matrix" << std::endl;
  TMatrixTSym<double> xsec_cov(NKnob);
  for (int i = 0; i < NKnob; i++) {

    std::string this_knobname = KnobNames[i];

    double this_prefit_err = 1.0;

    if(i<genieMultisigmaNames.size()){
      this_prefit_err = 1.0;
    }
    else{
      this_prefit_err = 1.0;
    }

    std::cout << this_knobname << "\t" << this_prefit_err << std::endl;

    xsec_cov(i, i) = this_prefit_err*this_prefit_err;

  }
/*
  // Z-exp
  double ZExpCorr[4][4];
  ZExpCorr[0][0] = 1.000000;
  ZExpCorr[0][1] = 0.350000;
  ZExpCorr[0][2] = -0.678000;
  ZExpCorr[0][3] = 0.611000;
  ZExpCorr[1][0] = 0.350000;
  ZExpCorr[1][1] = 1.000000;
  ZExpCorr[1][2] = -0.898000;
  ZExpCorr[1][3] = 0.367000;
  ZExpCorr[2][0] = -0.678000;
  ZExpCorr[2][1] = -0.898000;
  ZExpCorr[2][2] = 1.000000;
  ZExpCorr[2][3] = -0.685000;
  ZExpCorr[3][0] = 0.611000;
  ZExpCorr[3][1] = 0.367000;
  ZExpCorr[3][2] = -0.685000;
  ZExpCorr[3][3] = 1.000000;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      xsec_cov(i,j) = ZExpCorr[i][j];
    }
  }
*/
  xsec_cov.Write("xsec_cov");

  TObjArray xsec_param_names;
  for(const auto& name: genieMultisigmaNames){
    xsec_param_names.Add( new TObjString(name.c_str()) );
    std::cout << "@@ Writting " << name << std::endl;
  }
  for(const auto& name: genieMorphNames){
    xsec_param_names.Add( new TObjString(name.c_str()) );
    std::cout << "@@ Writting " << name << std::endl;
  }
  file->WriteObjectAny( &xsec_param_names, "TObjArray", "xsec_param_names" );

  TVectorD xsec_param_prior(NKnob);
  TVectorD xsec_param_lb(NKnob);
  TVectorD xsec_param_ub(NKnob);
  for(int i=0; i<NKnob; i++){
    if(i<genieMultisigmaNames.size()){
      xsec_param_prior[i] = 0.;
      xsec_param_lb[i] = -3.;
      xsec_param_ub[i] = +3.;
    }
    else{
      xsec_param_prior[i] = 0.;
      xsec_param_lb[i] = -3;
      xsec_param_ub[i] = 3.;
    }
  }
  xsec_param_prior.Write("xsec_param_prior");
  xsec_param_lb.Write("xsec_param_lb");
  xsec_param_ub.Write("xsec_param_ub");

  file->Close();
}

std::vector<std::string> GetGENIEMorphKnobNames(){

  return {
"VecFFCCQEshape",
"DecayAngMEC",
"Theta_Delta2Npi",
"ThetaDelta2NRad",
  };

}

std::vector<std::string> GetGENIEMultisigmaKnobNames(){
  return {
/*
"ZExpA1CCQE",
"ZExpA2CCQE",
"ZExpA3CCQE",
"ZExpA4CCQE",
*/

"ZExpPCAB1",
"ZExpPCAB2",
"ZExpPCAB3",
"ZExpPCAB4",
"RPA_CCQE",
"CoulombCCQE",
"NormCCMEC",
"NormNCMEC",
"MaNCEL",
"EtaNCEL",
"MaCCRES",
"MvCCRES",
"MaNCRES",
"MvNCRES",
"NonRESBGvpCC1pi",
"NonRESBGvpCC2pi",
"NonRESBGvpNC1pi",
"NonRESBGvpNC2pi",
"NonRESBGvnCC1pi",
"NonRESBGvnCC2pi",
"NonRESBGvnNC1pi",
"NonRESBGvnNC2pi",
"NonRESBGvbarpCC1pi",
"NonRESBGvbarpCC2pi",
"NonRESBGvbarpNC1pi",
"NonRESBGvbarpNC2pi",
"NonRESBGvbarnCC1pi",
"NonRESBGvbarnCC2pi",
"NonRESBGvbarnNC1pi",
"NonRESBGvbarnNC2pi",
"RDecBR1gamma",
"RDecBR1eta",
"NormCCCOH",
"NormNCCOH",
"AhtBY",
"BhtBY",
"CV1uBY",
"CV2uBY",

"MFP_pi",
"FrCEx_pi",
"FrInel_pi",
"FrAbs_pi",
"FrPiProd_pi",
"MFP_N",
"FrCEx_N",
"FrInel_N",
"FrAbs_N",
"FrPiProd_N",

"CC1piTPi",
  };

}
