import os
import GENIESystKnobList

WhichOne = "Signal"
WhichOne = "Bkgd"


knobNames = GENIESystKnobList.Signal_GENIEMultisigmaKnobNames if WhichOne=="Signal" else GENIESystKnobList.Bkgd_GENIEMultisigmaKnobNames

for name in knobNames:

  IsEnabled = 'true'

  output = '''- parameterName: "%s"
  isEnabled: %s
  dialSetDefinitions:
    - dialType: Spline
      minDialResponse: 0
      maxDialResponse: 10
      dialLeafName: "%s"
      applyCondition: "[IsData]==0"
'''%(name, IsEnabled, name)
  print(output)

knobNames = GENIESystKnobList.Signal_GENIEMorphKnobNames if WhichOne=="Signal" else GENIESystKnobList.Bkgd_GENIEMorphKnobNames

UseMirror = 'true'
for name in knobNames:
  output = '''- parameterName: "%s"
  isEnabled: %s
  dialSetDefinitions:
    - dialType: Spline
      minDialResponse: 0
      maxDialResponse: 10
      dialLeafName: "%s"
      useMirrorDial: true
      mirrorLowEdge: -1
      mirrorHighEdge: 1
      applyCondition: "[IsData]==0"
'''%(name, UseMirror, name)
  print(output)
