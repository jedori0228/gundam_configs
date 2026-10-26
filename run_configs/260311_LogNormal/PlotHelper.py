def AddICARUSData(ax, x=0.0, y=0.020, _fontsize=16, _horizontalalignment='right'):
    _LABEL_X_OFFSET = x
    _LABEL_Y_OFFSET = y
    _yrange = ax.get_ylim()
    _use_y = _yrange[1] + _LABEL_Y_OFFSET*(_yrange[1] - _yrange[0])
    _xrange = ax.get_xlim()
    _use_x = _xrange[0] + _LABEL_X_OFFSET*(_xrange[1] - _xrange[0])
    ax.text(
        x=_use_x,
        y=_use_y,
        s=r'$\bf{ICARUS}$ Data',
        fontsize=_fontsize,
        color='#d67a11',
        horizontalalignment=_horizontalalignment,
    )

def AddNuMIPOT(ax, POTToNormalize, _fontsize=16):

    _yrange = ax.get_ylim()
    _use_y = _yrange[1] + 0.02*(_yrange[1] - _yrange[0])
    _xrange = ax.get_xlim()
    _use_x = _xrange[1] - 0.02*(_xrange[1] - _xrange[0])
    _use_pot = POTToNormalize/1.0e20
    POTstr = 'NuMI, '+'{:0.2}'.format(_use_pot)+r'$\times 10^{20}$'+' POT'
    ax.text( x=_use_x, y=_use_y, s=POTstr,\
                fontsize=_fontsize, color='black', horizontalalignment='right' )