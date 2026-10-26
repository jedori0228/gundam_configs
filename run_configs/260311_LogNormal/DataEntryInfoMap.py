from DataEntryInfo import DataEntryInfo

DataEntryInfoMap = dict()

# Asimov
DataEntryInfoMap['Asimov'] = DataEntryInfo(
    Name = 'Asimov',
    Latex = 'Asimov',
    POT = 2.5006160e+20,
)

# Fake data from 30% MC
DataEntryInfoMap['FakeDataFromMCSubset'] = DataEntryInfo(
    Name = 'FakeDataFromMCSubset',
    Latex = 'Subset of MC',
    POT = 2.5006160e+20,
)

# Fake data from 30% MC + LQCD fit
DataEntryInfoMap['FakeDataLQCDZExpFit'] = DataEntryInfo(
    Name = 'FakeDataLQCDZExpFit',
    Latex = 'Subset of MC, LQCD Z-exp fit',
    POT = 2.5006160e+20,
)

# Fake data from 30% MC + LQCD fit
DataEntryInfoMap['FakeDataLQCDParkZExpFit'] = DataEntryInfo(
    Name = 'FakeDataLQCDParkZExpFit',
    Latex = 'Subset of MC, LQCD (Park) Z-exp fit',
    POT = 2.5006160e+20,
)

# Fake data from 30% MC + LQCD fit
DataEntryInfoMap['FakeDataMINERvAZExpFit'] = DataEntryInfo(
    Name = 'FakeDataMINERvAZExpFit',
    Latex = 'Subset of MC, MINERvA Z-exp fit',
    POT = 2.5006160e+20,
)

# Fake data from 30% MC + LQCD fit
DataEntryInfoMap['FakeDataQEBugFix'] = DataEntryInfo(
    Name = 'FakeDataQEBugFix',
    Latex = 'Subset of MC, QE bug fix',
    POT = 2.5006160e+20,
)

# Fake data from 30% MC + FSI
DataEntryInfoMap['FakeData_FSI_hN'] = DataEntryInfo(
    Name = 'FakeData_FSI_hN',
    Latex = 'Subset of MC, FSI hN',
    POT = 2.5006160e+20,
)
DataEntryInfoMap['FakeData_FSI_INCL'] = DataEntryInfo(
    Name = 'FakeData_FSI_INCL',
    Latex = 'Subset of MC, FSI INCL',
    POT = 2.5006160e+20,
)
DataEntryInfoMap['FakeData_FSI_G4BC'] = DataEntryInfo(
    Name = 'FakeData_FSI_G4BC',
    Latex = 'Subset of MC, FSI G4BC',
    POT = 2.5006160e+20,
)



# Fake data from 30% MC + Signal doubled
DataEntryInfoMap['FakeData_SignalDoubled'] = DataEntryInfo(
    Name = 'FakeData_SignalDoubled',
    Latex = 'Subset of MC, signal doubled',
    POT = 2.5006160e+20,
)

# Fake data from 30% MC + Signal doubled
DataEntryInfoMap['FakeData_Signal1p5'] = DataEntryInfo(
    Name = 'FakeData_Signal1p5',
    Latex = 'Subset of MC, signal 1.5',
    POT = 2.5006160e+20,
)



# - Sideband: 15% data
# - Signal: Fake data from 30% MC
DataEntryInfoMap['Random15PercentRealDataForSideband_FakeDataForSignal'] = DataEntryInfo(
    Name = 'Random15PercentRealDataForSideband_FakeDataForSignal',
    Latex = r'15% data for sideband, fake data for signal',
    POT = 3.5670840e+19,
)

# - Sideband: 15% data
# - Signal: 15% data
DataEntryInfoMap['Random15PercentRealData'] = DataEntryInfo(
    Name = 'Random15PercentRealData',
    Latex = r'15% data',
    POT = 3.5670840e+19,
)

# - Sideband: 100% data
# - Signal: Fake data from 30% MC
DataEntryInfoMap['RealDataForSideband_FakeDataForSignal'] = DataEntryInfo(
    Name = 'RealDataForSideband_FakeDataForSignal',
    Latex = r'Data for sideband, fake data for signal',
    POT = 2.5006160e+20,
)

# - Sideband: 100% data
# - Signal: 15% data
DataEntryInfoMap['RealDataForSideband_Random15PercentRealDataForSignal'] = DataEntryInfo(
    Name = 'RealDataForSideband_Random15PercentRealDataForSignal',
    Latex = r'Data for sideband, 15% data for signal',
    POT = 2.5006160e+20,
)

# - Sideband: 100% data
# - Signal: 100% data
DataEntryInfoMap['RealData'] = DataEntryInfo(
    Name = 'RealData',
    Latex = r'Data',
    POT = 2.5006160e+20,
)