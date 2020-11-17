# causalmodel

All states can be described as either:
* Actions (Originate from within the self) -> Can be triggered to manipulate current state position
* Stimuli (Observations, interactions, changes in sensor value) -> Cannot be triggered by the model
* Rewards (Desirable states, incentivized by seperate model)

According to Hume:
* Cause must be contiguous to effect -> Assuming that any arbitrary state can lead to any other arbitrary state, the graph must be well connected
* Cause precedes effect -> Our graph must be directed

According the the Multiple Clock Theory, we measure time in several different ways. We can define a set of clocks as the following:

* Short term (measured in seconds)  (0)
* Mid term (minutes) (1)
* Long term (hours) (2)
* Extra long term (days) (3)

Each clock can be bounded by a constant, to be refined during model run-time. We can place a set of clocks in every possible pathway between any two edges on the graph. Each clock can represent the probability of the state it leads to occurring within its bounds. Upon reaching a state, the clocks begin ticking until the constant bound elapses. If another state occurs, the probability value of the shortest clock still ticking is bolstered.

![cgraph](https://github.com/atomdog/causalmodel/blob/main/g.png)

Here is a depiction of what the graph may look like, with the squares being the set of clocks, and circles being states.

Given the nature of the graph built so far, it would be simple to implement a simple Markov chain to gain a sense, probabilistically, of how one state may lead to another, in a manner true to a human's coginition. 

We can define a transition matrix, <i>T</i>, where rather than every entry being a singular probability, every entry is a vector <i>t</i>, which is composed of the four probability values of the clock, and perform any standard Markov processes.

However, the model can also trigger any action state from the current stimuli state, if given the current observation state, taking that action results in an increased probability of a reward state.

Here is where this breaks down. It seems difficult to implement conditional probability via the transition matrix. 
