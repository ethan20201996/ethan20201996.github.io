# GEOG 5990

---

# GEOG 5990 Portfolio

## Discription

This model includes each basic part of practical:&emsp;
nbsp;nbsp;_ builds agents in a space;&emsp;
nbsp;nbsp;_ gets them to interact with each other;&emsp;
nbsp;nbsp;_ reads in environmental data;&emsp;
nbsp;nbsp;_ gets agents to interact with the environment;&emsp;
nbsp;nbsp;_ randomizes the order of agent actions;&emsp;
nbsp;nbsp;_ displays the model as an animation;&emsp;
nbsp;nbsp;_ is contained within a GUI;&emsp;
nbsp;nbsp;_ is initialised with data from the web.&emsp;
Addionally, I modified the model to let agent eat fast if they have more store, I made a self.speed label in **init** method to control the iteration of store:&emsp;
def eat(self):&emsp;
if self.environment[self.y][self.x] > 10:&emsp;
self.environment[self.y][self.x] -= 10&emsp;
self.store = self.store + 10 + self.speed&emsp;
if self.store > 4000:&emsp;
self.speed += 100&emsp;

### Link below:

<a href="https://raw.githubusercontent.com/ethan20201996/ethan20201996.github.io/main/model.py">Model<a>
<a href="https://raw.githubusercontent.com/ethan20201996/ethan20201996.github.io/main/agentframework.py">Framework<a>
