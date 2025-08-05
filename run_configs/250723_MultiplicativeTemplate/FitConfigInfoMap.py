from FitConfigInfo import FitConfigInfo

FitConfigInfoMap = dict()

FitConfigInfoMap['SimFit'] = FitConfigInfo(
    Name = 'SimFit',
    Latex = 'Simultaneous fit',
)
FitConfigInfoMap['IndvFit'] = FitConfigInfo(
    Name = 'IndvFit',
    Latex = 'Per-variable fit',
)

for OriginalKey in ['SimFit', 'IndvFit']:

    for LLHMethod in ['PoissonLLH', 'BarlowLLH', 'StatCovariance']:
        NewKey = OriginalKey+'_'+LLHMethod
        NewName = FitConfigInfoMap[OriginalKey].Name+'_'+LLHMethod
        NewLatex = FitConfigInfoMap[OriginalKey].Latex

        FitConfigInfoMap[NewKey] = FitConfigInfo(
            Name = NewName,
            Latex = NewLatex,
        )