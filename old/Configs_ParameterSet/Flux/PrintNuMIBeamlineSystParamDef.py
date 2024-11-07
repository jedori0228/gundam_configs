import NuMIBeamlineSystKnobList

knobNames = NuMIBeamlineSystKnobList.NuMIBeamlineFluxSYstKnobNames

for name in knobNames:
  output = '''- parameterName: "%s"
  isEnabled: true
  dialSetDefinitions:
    - dialType: Spline
      minimumSplineResponse: 0
      dialLeafName: "%s"
      applyCondition: "[IsData]==0"
'''%(name, name)
  print(output)

