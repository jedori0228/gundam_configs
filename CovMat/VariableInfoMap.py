from VariableInfo import VariableInfo

VariableInfos = dict()

VariableInfos['RecoMuonCos'] = VariableInfo(
    Name = 'RecoMuonCos',
    Expr = 'RecoMuonCos',
    Latex = r'$\cos{\theta_{\mu}}$',
    xMin = -1.,
    xMax = 1.,
    dx = 0.1,
    BinNormWidth=0.1,
    ytitle='Events/(0.1)',
    Unit = '',
)
VariableInfos['TrueMuonCos'] = VariableInfo(
    Name = 'TrueMuonCos',
    Expr = 'TrueMuonCos',
    Latex = r'True $\cos{\theta_{\mu}}$',
    xMin = -1.,
    xMax = 1.,
    dx = 0.1,
    Unit = ''
)

VariableInfos['RecoMuonProtonCos'] = VariableInfo(
    Name = 'RecoMuonProtonCos',
    Expr = 'RecoMuonProtonCos',
    Latex = r'$\cos{\theta_{\mu,p}}$',
    xMin = -1.,
    xMax = 1.,
    dx = 0.10,
    BinNormWidth=0.1,
    ytitle='Events/(0.1)',
    Unit = '',
)
VariableInfos['TrueMuonProtonCos'] = VariableInfo(
    Name = 'TrueMuonProtonCos',
    Expr = 'TrueMuonProtonCos',
    Latex = r'True $\cos{\theta_{\mu,p}}$',
    xMin = -1.,
    xMax = 1.,
    dx = 0.10,
    ytitle='events/(0.1)',
    Unit = '',
)

VariableInfos['RecodeltaPT'] = VariableInfo(
    Name = 'RecodeltaPT',
    Latex = r'$\delta p_{T}$',
    xMin = 0.,
    xMax = 0.8,
    dx = 0.1,
    Unit = 'GeV',
    BinNormWidth = 0.1,
)
VariableInfos['TruedeltaPT'] = VariableInfo(
    Name = 'TruedeltaPT',
    Expr = 'TruedeltaPT',
    Latex = r'True $\delta P_{T}$',
    #xMin = 0.,
    #xMax = 1.2,
    #dx = 0.05,
    CustomBinning=[0., 0.08, 0.17, 0.25, 0.35, 0.55, 0.8],
    BinNormWidth=0.1,
    Unit = 'GeV/c'
)

VariableInfos['RecodeltaalphaT'] = VariableInfo(
    Name = 'RecodeltaalphaT',
    Latex = r'$\delta \alpha_{T}$',
    xMin = 0.,
    xMax = 180.,
    dx = 1.,
    Unit = 'degree',
    BinNormWidth = 1.,
    # ytitle = 'Events/degree',
)
VariableInfos['TruedeltaalphaT'] = VariableInfo(
    Name = 'TruedeltaalphaT',
    Latex = r'$\delta \alpha_{T}$',
    xMin = 0.,
    xMax = 180.,
    dx = 1.,
    Unit = 'degree',
    # BinNormWidth = 1.,
    # ytitle = 'Events/degree',
)