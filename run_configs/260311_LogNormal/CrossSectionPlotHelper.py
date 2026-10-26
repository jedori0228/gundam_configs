def GetCrossSectionTitle(TrueVariableName):

    VariableYTitle = ''
    if TrueVariableName=='TruedeltaPT':
        VariableYTitle = r'$\frac{d \sigma}{d \delta p_{T}}$ $\frac{cm^{2}}{(GeV/c) Ar}$'
    elif TrueVariableName=='TruedeltaalphaT':
        VariableYTitle = r'$\frac{d \sigma}{d \delta \alpha_{T}}$ $\frac{cm^{2}}{(degree) Ar}$'
    elif TrueVariableName=='TrueMuonCos':
        VariableYTitle = r'$\frac{d \sigma}{d \cos{\theta_{\mu}}}$ $\frac{cm^{2}}{Ar}$'
    elif TrueVariableName=='TrueMuonProtonCos':
        VariableYTitle = r'$\frac{d \sigma}{d \cos{\theta_{\mu,p}}}$ $\frac{cm^{2}}{Ar}$'
    elif TrueVariableName=='TrueProtonP':
        VariableYTitle = r'$\frac{d \sigma}{d p_{p}}$ $\frac{cm^{2}}{(GeV/c) Ar}$'  
    else:
        raise ValueError(f'[GetCrossSectionTitle] {TrueVariableName} is not supported')
    
    return VariableYTitle

def GetCrossSectionYMax(TrueVariableName, PhaseSpaceCut):

    if TrueVariableName=='TruedeltaPT':
        VariableYMax = 1.3E-37
        if PhaseSpaceCut == 'MuonPLT0p8':
            VariableYMax = 0.6E-37
    elif TrueVariableName=='TruedeltaalphaT':
        VariableYMax = 4E-40
        if PhaseSpaceCut == 'MuonPLT0p8':
            VariableYMax = 1.5E-40
    elif TrueVariableName=='TrueMuonCos':
        VariableYMax = 2.5E-37
    elif TrueVariableName=='TrueMuonProtonCos':
        VariableYMax = 4.3E-38
    elif TrueVariableName=='TrueProtonP':
        VariableYMax = 1.1E-37
    else:
        raise ValueError(f'[GetCrossSectionYMax] {TrueVariableName} is not supported')
    
    return VariableYMax

def AddSignalDefText(ax, TrueVariableName, SigDefText, _fontsize=16):

    _LABEL_X_OFFSET = 0.
    _LABEL_Y_OFFSET = 0.
    NewLine=True

    if TrueVariableName=='TruedeltaPT':
        _LABEL_X_OFFSET = 0.9
        _LABEL_Y_OFFSET = 0.55
    elif TrueVariableName=='TruedeltaalphaT':
        _LABEL_X_OFFSET = 0.50
        _LABEL_Y_OFFSET = 0.55
    elif TrueVariableName=='TrueMuonCos':
        _LABEL_X_OFFSET = 0.40
        _LABEL_Y_OFFSET = 0.45
    elif TrueVariableName=='TrueMuonProtonCos':
        _LABEL_X_OFFSET = 0.75
        _LABEL_Y_OFFSET = 0.07
        NewLine=False
    elif TrueVariableName=='TrueProtonP':
        _LABEL_X_OFFSET = 0.80
        _LABEL_Y_OFFSET = 0.55
    else:
        raise ValueError(f'[GetCrossSectionTitle] {TrueVariableName} is not supported')
    
    _yrange = ax.get_ylim()
    _use_y = _yrange[0] + _LABEL_Y_OFFSET*(_yrange[1] - _yrange[0])
    _xrange = ax.get_xlim()
    _use_x = _xrange[0] + _LABEL_X_OFFSET*(_xrange[1] - _xrange[0])
    ax.text(
        x=_use_x,
        y=_use_y,
        s='Signal definition:\n'+SigDefText if NewLine else 'Signal definition: '+SigDefText,
        fontsize=_fontsize,
        horizontalalignment='right'
    )

