import numpy as np
import stateLib as sl
import ticket
import actions
state_q = 8
tm = []
current_state = None
for x in range(0, state_q):
    name = "S"+str(x)
    f = sl.state(name, state_q)
    tm.append(f)
    print(tm[x].tr)


#YOOOOO YOOO LET'S GOOOO BABY BIG W FINALLY KNOW HOW TO USE LAMBDA FUNCTIONS
#assign target functions manually to states with relevant functions

f = lambda a : actions.summarize(a)
tm[0].set_target_function(f)
f1 = lambda a : actions.getHeadlines()
tm[1].set_target_function(f)
f2 = lambda a, b : actions.send(a,b)
tm[2].set_target_function(f)
f3 = lambda a: actions.toggle_diffuser("0")
tm[3].set_target_function(f3)
f4 = lambda a: actions.toggle_diffuser("1")
tm[4].set_target_function(f4)
