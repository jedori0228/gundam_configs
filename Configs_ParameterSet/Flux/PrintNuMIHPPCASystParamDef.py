import os

NPCA=175

NMax=15

for i in range(NPCA):
  name = 'numi_pc_%d'%(i)

  if i>=NMax:
    break

  output = '''- parameterName: "%s"
  isEnabled: true
  dialSetDefinitions:
    - dialType: Spline
      minimumSplineResponse: 0
      dialLeafName: "%s"
      applyCondition: "[IsData]==0"
'''%(name, name)
  print(output)

