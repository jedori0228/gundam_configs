from BaseInfo import BaseInfo
class DataEntryInfo(BaseInfo):
    def __init__(self, Name, Latex, POT):
        super().__init__(Name, Latex)
        self.POT = POT