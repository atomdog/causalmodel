
import numpy as np
import I
class state:
    def __init__(self, name, n):
        self.name = name
        self.tr = None
        self.init_transition_vector(n)
        self.rewardState = False
        self.action_potentiate = False
        self.triggerable = False
        self.action = False
        self.stimuli = True
        self.target_function = None
        self.wordCloud = None
        self.TI = None 
    def init_transition_vector(self, n):
        tsiv = (1/n) / 4
        self.tr = np.full((n, 4), tsiv, dtype = 'float128')
    def add_state(self, budget):
        n = budget/(len(self.tr))
        sum = 0
        for x in range(0, len(self.tr)):
            self.tr[x]= self.tr[x] * (1 - budget)
        self.tr = np.vstack([self.tr, np.full((1,4), budget/4, dtype = 'float128')])
        print(np.sum(self.tr))
        return(self.tr)
    def state_triggered(self):
        #open expiry ticket
        pass
    def enact(self):
        pass
    def reward(self,):
        if(self.rewardState==True):
            pass
        else:
            pass
            #trigger reward in I
    def action_potentiate(self, rIndex):
        val = np.sum(tr[rIndex])
        tr[rIndex] = np.ndarray([0.0,0.0,0.0,0.0])
        #redistribute prob to other ones randomly
        pass
    def update(self):
        pass
    def pNS(self):
        pNS = np.amax(self.tr)
        return(pNS)
    def set_target_function(self, tf):
        self.target_function = tf
    def target_function(self, passthru):
        return(self.target_function(passthru))
    def updateCloud(self, txt):
        self.wordCloud = txt
    def setTopicID(self, TI):
        self.TI = TI
