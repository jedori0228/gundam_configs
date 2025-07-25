import os
import GENIESystKnobList

knobNames = GENIESystKnobList.GENIEMultisigmaKnobNames

for name in knobNames:

  IsEnabled = 'true'
  #if 'MFP' in name or 'Fr' in name:
  #  IsEnabled = 'false'

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

knobNames = GENIESystKnobList.GENIEMorphKnobNames

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
