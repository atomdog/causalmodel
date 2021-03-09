
class profile():
    pronouns = ["he", "him ", "his"], ["she", "her", "hers"], ["they", "their", "theirs"]
    prefix = [['Mister', 'Doctor'], ['Miss', 'Doctor'], ['None', 'Doctor']]
    suffix = [['Sir'], ["Ma'am"], []]
    def __init__(self, ID, face_path):
        self.ID = ID
        self.face = face_path
        self.name = None
        #pronouns
        self.pronouns = None
        self.title = None
        #attitude, politeness
        self.pScore = (None, None)
        #permissions
        self.trust = 0
        #presumed emotional state
        self.pES = 0
        #previous conversations attributed to this person
        self.prevConv = None
        self.phonenumber = None
        self.email = None
        self.appeal = None
        #add expiring and unknowns to unknown db
    def createConvFile(self, Conv_path):
        self.prevConv = Conv_path
    def update_pronouns(self, pronounindex):
        self.pronouns = pronounindex
    def update_pScore(self, pScoreu):
        self.pScore = pScoreu
    def updatetrust(self, trustu):
        self.trust = trust
    def update_pES(self, PESu):
        self.PES = PESu
    def updateprevConv(self, prevConv, uv):
        return(True)
    def retUParam(self):
        f = [self.ID, self.name, self.face, self.pronouns, self.title, self.pScore, self.trust, self.pES, self.prevConv, self.phonenumber, self.email]
        return(f)
