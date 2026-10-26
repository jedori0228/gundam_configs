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
    Latex = r'$\cos{\theta_{\mu}}$',
    # xMin = -1.,
    # xMax = 1.,
    # dx = 0.1,
    CustomBinning=[-1.0000, 0.1516, 0.5282, 0.7320, 0.8446, 0.9122, 0.9518, 0.9780, 1.0000],
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
    Latex = r'$\cos{\theta_{\mu,p}}$',
    # xMin = -1.,
    # xMax = 1.,
    # dx = 0.10,
    CustomBinning=[-1.0000, -0.5806, -0.3628, -0.1926, -0.0424, 0.0814, 0.2018, 0.3286, 0.4878, 0.7016, 1.0000],
    ytitle='events/(0.1)',
    Unit = '',
)

VariableInfos['RecoProtonP'] = VariableInfo(
    Name = 'RecoProtonP',
    Expr = 'RecoProtonP',
    Latex = r'Proton momentum',
    xMin = 0.4,
    xMax = 1.0,
    dx = 0.05,
    BinNormWidth=1.0,
    Unit = 'GeV/c',
)
VariableInfos['TrueProtonP'] = VariableInfo(
    Name = 'TrueProtonP',
    Expr = 'TrueProtonP',
    Latex = r'Proton momentum',
    xMin = 0.4,
    xMax = 1.0,
    dx = 0.05,
    Unit = 'GeV/c',
)

VariableInfos['RecodeltaPT'] = VariableInfo(
    Name = 'RecodeltaPT',
    Latex = r'$\delta p_{T}$',
    xMin = 0.,
    xMax = 0.8,
    dx = 0.1,
    Unit = 'GeV/c',
    BinNormWidth = 0.1,
)
VariableInfos['TruedeltaPT'] = VariableInfo(
    Name = 'TruedeltaPT',
    Latex = r'$\delta p_{T}$',
    # xMin = 0.,
    # xMax = 0.8,
    # dx = 0.1,
    CustomBinning=[0., 0.08, 0.17, 0.25, 0.35, 0.55, 0.8],
    Unit = 'GeV/c',
    # BinNormWidth = 0.1,
)

VariableInfos['RecodeltaalphaT'] = VariableInfo(
    Name = 'RecodeltaalphaT',
    Latex = r'$\delta \alpha_{T}$',
    xMin = 0.,
    xMax = 180.,
    dx = 1.,
    Unit = 'degree',
    BinNormWidth = 1.,
    ytitle = 'Events/degree',
)
VariableInfos['TruedeltaalphaT'] = VariableInfo(
    Name = 'TruedeltaalphaT',
    Latex = r'$\delta \alpha_{T}$',
    # xMin = 0.,
    # xMax = 180.,
    # dx = 1.,
    CustomBinning=[0, 25, 60, 100, 130, 160, 180],
    Unit = 'degree',
    # BinNormWidth = 1.,
    # ytitle = 'Events/degree',
)

# Propagation

VariableInfos['RecoProtonCos'] = VariableInfo(
    Name = 'RecoProtonCos',
    Expr = 'RecoProtonCos',
    Latex = r'$\cos{\theta_{p}}$',
    xMin = -1.,
    xMax = 1.,
    dx = 0.10,
    BinNormWidth=0.1,
    ytitle='Events/(0.1)',
    Unit = '',
)