class BinInfo:

   def __init__(self, Name, Type):

     self.Name = Name
     self.Type = Type

     self.ValidateType()

   def Summary(self):
     return "Variable name: %s, Type: %s"%(self.Name, self.Type)

   def ValidateType(self):
     if self.Type not in ["int", "float"]:
       raise ValueError("[BinInfo][GetTypeString] Type:", self.Type, "is not supported for %s"%(self.Name))

class BinParser:

  def __init__(self, Filepath):
    self.Filepath = Filepath

    print("[BinParser][__init__] Reading binning info from %s"%(self.Filepath))

    lines = open(self.Filepath).readlines()
    if len(lines)<2:
      raise ValueError("[BinParser][ReadFile] Input file containes less than 2 lines")
    header = lines[0].strip('\n')
    if not header.startswith("variables:"):
      raise ValueError("[BinParser][ReadFile] Header should starts with \"variables:\", but it is:\n%s"%(header))

    header_split = header.split()
    header_split = header_split[1:] # remove "variables:"

    BinInfoArray = []
    i_header=0
    while i_header<len(header_split):
      this_Var = header_split[i_header]
      next_Var = header_split[i_header+1]
      if this_Var==next_Var:
        BinInfoArray.append( BinInfo(this_Var, "float") )
        i_header += 2
      else:
        BinInfoArray.append( BinInfo(this_Var, "int") )
        i_header += 1
    ## Printing bin info summary
    for bin_info in BinInfoArray:
      print(bin_info.Summary())

    self.CutExprs = []
    for i in range(1,len(lines)):
      this_line = lines[i].strip('\n')
      bin_values = this_line.split()
      if len(bin_values)!=len(header_split):
        raise ValueError("[BinParser][ReadFile] Line %d has wrong number of values; should be %d, but %d provided"%(i, len(header_split), len(bin_values)))

      CutExpr = ""
      j=0
      for i_bin in range(0, len(BinInfoArray)):
        this_CutExpr = ""
        if BinInfoArray[i_bin].Type=="int":
          this_CutValue = bin_values[j]
          this_CutExpr += "%s==%s"%(BinInfoArray[i_bin].Name, this_CutValue)
          j += 1
        elif BinInfoArray[i_bin].Type=="float":
          this_CutValue_Low = bin_values[j]
          this_CutValue_High = bin_values[j+1]
          this_CutExpr += "%s>=%s & %s<%s"%(BinInfoArray[i_bin].Name, this_CutValue_Low, BinInfoArray[i_bin].Name, this_CutValue_High)
          j += 2
        else:
          raise ValueError("[BinParser][ReadFile] Type:", BinInfoArray[i_bin].Type, "is not supported for %s"%(BinInfoArray[i_bin].Name))

        if CutExpr=="":
          CutExpr = this_CutExpr
        else:
          CutExpr += " & "+this_CutExpr

      self.CutExprs.append(CutExpr)
