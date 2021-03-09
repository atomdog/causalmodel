#ticketing system
import time
#queues, checking
from datetime import datetime
import stateLib
import causal_model
class queues:
    def __init__(self):
        self.short = []
        self.mid = []
        self.long = []
    def get_current():
        pass
class ticket:
    def calc_expiry(self, type, dt):
        for x in range(0, len(dt)):
            dt[x] = int(dt[x])
        print(dt)
        print(len(dt))
        dtc = dt

        #constant in minutes
        shorttermconstant = 1
        #in minutes
        midtermconstant = 15
        #in hour
        longtermconstant = 1
        #in days
        elongtermconstant = 1

        if(type==0):
            dtc[4] = (dtc[4] + 1)%60
        if(type==1):
            dtc[4] = (dtc[4] + midtermconstant)%60
        if(type==2):
            pass
        if(type==3):
            if(dt[1]==1 or dt[1]==3 or dt[1] == 5  or dt[1] == 7 or dt[1] == 8 or dt[1] == 10 or dt[1] == 12):
                dtc[0] = (dtc[0]+elongtermconstant) % 31
            elif(dt[1]==2):
                dtc[0] = (dtc[0]+elongtermconstant) % 28
            else:
                dtc[0] = (dtc[0]+elongtermconstant) % 30
        return(dtc)

    def __init__(self, states, statet, type):
        #passed constructors
        #states = index of state start
        #statet = index of state targeted by ticket
        #if statet is triggered, close ticket validating minimum clock that satisifies time passed
        self.states = states
        self.statet = statet
        self.type = type
        #time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        d_list =  [now.strftime("%d"),now.strftime("%m"),now.strftime("%Y"),now.strftime("%H"),now.strftime("%M"),now.strftime("%S")]
        self.conception = dt_string
        #calculate expiry
        self.expiry = self.calc_expiry(self.type, d_list)
        #print ticket creation
        print("At time " + dt_string + " state " + str(states) + " triggered, ticket created targeting "+ str(statet) + ". Expiry: " + str(self.expiry))





ticky = ticket(0, 1, 3)
