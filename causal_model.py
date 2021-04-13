import numpy as np
import stateLib
import ticket
import actions
#make class!!!!

class model():


    def __init__(self):
        self.tm = []
        self.state_q = 8
        self.total_encountered = 0
        #occurence clone to measure number of occurences
        self.tm_occ_clone = None
        self.ticket_stack = ticket.queues()
        self.current_state = None
        for x in range(0, self.state_q):
            name = "S"+str(x)
            f = stateLib.state(name, state_q)
            self.tm.append(f)
            print(self.tm[x].tr)
            self.tm_occ_clone.append(np.full((self.state_q, 4), 0, dtype = 'float128'))

    def reload_prob(self):
        total_occur = 0
        for x in range(0, len(tm)):
            for y in range(0, len(tm[x])):
                for z in range(0, len[tm[x][y]]):
                    total_occur+=self.tm_occ_clone[x][y][z]
            for y in range(0, len[tm[x]):
                for z in range(0, len[tm[x][y]]):
                    self.tm[x][y][z] = self.tm_occ_clone[x][y][z]/total_occ_clone
            total_occur = 0
        


    def manual_state_load(self):
        f = lambda a : actions.summarize(a)
        self.tm[0].updateVerbCloud(["find", "read", "look", "tell"])
        self.tm[0].set_target_function(f)
        self.tm[0].name = "summarize"

        f1 = lambda a : actions.getHeadlines()
        self.tm[1].updateObjectCloud(["headline", "news"])
        self.tm[1].updateVerbCloud(["get", "read", "tell"])
        self.tm[1].set_target_function(f1)
        self.tm[1].name = "news"

        f2 = lambda a, b : actions.send(a,b)
        self.tm[2].set_target_function(f2)
        self.tm[2].name = "send"


        f3 = lambda a: actions.toggle_diffuser("0")
        self.tm[3].updateObjectCloud(["diffuser"])
        self.tm[3].updateVerbCloud(["turn", "switch"])
        self.tm[3].updateDescriptorCloud(["off"])
        self.tm[3].set_target_function(f3)
        self.tm[3].name = "diffuser_off"

        f4 = lambda a: actions.toggle_diffuser("1")
        self.tm[4].updateObjectCloud(["diffuser"])
        self.tm[4].updateVerbCloud(["turn", "switch"])
        self.tm[4].updateDescriptorCloud(["on"])
        self.tm[4].set_target_function(f4)
        self.tm[4].name = "diffuser_on"

        f5 = lambda a: actions.getPrecipitation("Boston", "MA")
        self.tm[5].updateObjectCloud(["weather"])
        self.tm[5].updateVerbCloud(["read", "tell", "whats"])
        self.tm[5].set_target_function(f5)
        self.tm[5].name = "read_weather"

        f6 = lambda a: actions.getCurrentTemp("Boston", "MA")
        self.tm[6].updateObjectCloud(["temperature"])
        self.tm[6].updateVerbCloud(["read", "tell", "whats"])
        self.tm[6].set_target_function(f5)
        self.tm[6].name = "read_temp"


#YOOOOO YOOO LET'S GOOOO BABY BIG W FINALLY KNOW HOW TO USE LAMBDA FUNCTIONS
#assign target functions manually to states with relevant functions
#assign states verb object descriptor clouds manually
