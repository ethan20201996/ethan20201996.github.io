# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:04:36 2021

@author: jyfxx
"""
import random 
import csv
import matplotlib.pyplot
import agentframework
import matplotlib.animation
import matplotlib
import requests
import bs4
import tkinter

matplotlib.use('TkAgg') 

#seed = 1 
#random.seed(seed)

environment = []
f = open ("in.txt", newline="")
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for values in row:
        rowlist.append(values)
    environment.append(rowlist)
f.close()

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True	
	
def update(frame_number):
    
    fig.clear()  
    ax = fig.add_axes([0, 0, 1, 1])
    global carry_on

    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood) 

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
       matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
		
    print("after eating:")
    for i in range(num_of_agents):
       print(agents[i])
       
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

    
root = tkinter.Tk()
root.wm_title("Model")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x)) 


# Check the agents.
for i in range(num_of_agents):
    print(agents[i])


tkinter.mainloop() 
