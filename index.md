<!--
 * @Author: your name
 * @Date: 2021-01-26 14:49:25
 * @LastEditTime: 2021-05-08 16:52:55
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \ethan20201996.github.io\index.md
-->

# GEOG 5990

---

# GEOG 5990 Portfolio

## Discription

This model includes each basic part of practical:<br/>
&nbsp;&nbsp;_ builds agents in a space;<br/>
&nbsp;&nbsp;_ gets them to interact with each other;<br/>
&nbsp;&nbsp;_ reads in environmental data;<br/>
&nbsp;&nbsp;_ gets agents to interact with the environment;<br/>
&nbsp;&nbsp;_ randomizes the order of agent actions;<br/>
&nbsp;&nbsp;_ displays the model as an animation;<br/>
&nbsp;&nbsp;_ is contained within a GUI;<br/>
&nbsp;&nbsp;_ is initialised with data from the web.<br/>
Addionally, I modified the model to let agent eat fast if they have more store, I made a self.speed label in **init** method to control the iteration of store:<br/>
def eat(self):<br/>
if self.environment[self.y][self.x] > 10:<br/>
self.environment[self.y][self.x] -= 10<br/>
self.store = self.store + 10 + self.speed<br/>
if self.store > 4000:<br/>
self.speed += 100<br/>
The final canvas will output as a png file <br/>

### Final result:

<img src="./temp.png">

## Link below:

<a href="https://raw.githubusercontent.com/ethan20201996/ethan20201996.github.io/main/model.py">Model<a>
<a href="https://raw.githubusercontent.com/ethan20201996/ethan20201996.github.io/main/agentframework.py">Framework<a>

## Resume

<a href="https://ethan20201996.github.io/homepage.html">On the way......<a>
