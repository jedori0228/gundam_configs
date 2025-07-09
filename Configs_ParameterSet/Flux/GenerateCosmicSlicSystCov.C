void GenerateCosmicSlicSystCov()
{

  // Make the covariance matrix: ((0,1), (1,0))
  TFile *file = new TFile("gundaminput_cosmicslicesyst.root","RECREATE");
  file->cd();

  TMatrixTSym<double> cosmicslicesyst_cov(1);
  double one_sig_rel_unct = 0.5;
  cosmicslicesyst_cov(0, 0) = one_sig_rel_unct*one_sig_rel_unct;
  cosmicslicesyst_cov.Write("cosmicslicesyst_cov");

  TObjArray cosmicslicesyst_param_names;
  std::string name = "CosmicSlice";
  cosmicslicesyst_param_names.Add( new TObjString(name.c_str()) );
  file->WriteObjectAny( &cosmicslicesyst_param_names, "TObjArray", "cosmicslicesyst_param_names" );

  TVectorD cosmicslicesyst_param_prior(1);
  TVectorD cosmicslicesyst_param_lb(1);
  TVectorD cosmicslicesyst_param_ub(1);

  cosmicslicesyst_param_prior[0] = 0.;
  cosmicslicesyst_param_lb[0] = -3.;
  cosmicslicesyst_param_ub[0] = +3.;

  cosmicslicesyst_param_prior.Write("cosmicslicesyst_param_prior");
  cosmicslicesyst_param_lb.Write("cosmicslicesyst_param_lb");
  cosmicslicesyst_param_ub.Write("cosmicslicesyst_param_ub");

  file->Close();
}

