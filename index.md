# GEOG 5990

---

# GEOG 5990 Portfolio

## Discription

This model includes each basic part of practical:
_ builds agents in a space;
_ gets them to interact with each other;
_ reads in environmental data;
_ gets agents to interact with the environment;
_ randomizes the order of agent actions;
_ displays the model as an animation;
_ is contained within a GUI;
_ is initialised with data from the web.
Addionally, I modified the model to let agent eat fast if they have more store, I made a self.speed label in **init** method to control the iteration of store:
def eat(self):
if self.environment[self.y][self.x] > 10:
self.environment[self.y][self.x] -= 10
self.store = self.store + 10 + self.speed
if self.store > 4000:
self.speed += 100

### Link below:

<a href="https://raw.githubusercontent.com/ethan20201996/ethan20201996.github.io/main/model.py">Model<a>
<a href="https://raw.githubusercontent.com/ethan20201996/ethan20201996.github.io/main/agentframework.py">Framework<a>
