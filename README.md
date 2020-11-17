# causalmodel

All states can be described as either:
* Actions (Originate from within the self) -> Can be triggered to manipulate current state position
* Stimuli (Observations, interactions, changes in sensor value) -> Cannot be triggered by the model
* Rewards (Desirable states, incentivized by seperate model)

According to Hume:
* Cause must be contiguous to effect -> Assuming that any arbitrary state can lead to any other arbitrary state, the graph must be well connected
* Cause precedes effect -> Our graph must be directed

According the the Multiple Clock Theory, we measure time in several different ways. We can define a set of clocks as the following:

* Short term (measured in seconds)  
* Mid term (minutes)
* Long term (hours)
* Extra long term (days)

Each clock can be bounded by a constant, to be refined during model run-time. We can place a set of clocks in every possible pathway between any two edges on the graph.

![cgraph](https://github.com/atomdog/causalmodel/blob/main/g.png)



Given the nature of the graph we've built so far, it would be simple to implement a simple Markov chain to gain a sense, probabilistically, of how one state may lead to another, in a manner true to a human's coginition. 

We can define a transition matrix, <i>T</i>
