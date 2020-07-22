from tkinter import *
from random import randint

root = Tk()
root.config(bg='black')
root.geometry('1000x1000')

c = Canvas(root, width=1000, height=1000, bg='black')
c.place(x=0, y=0)

vel = 10

direction = 'DOWN'

root.title('Snake Game')

snakehead = [240, 240]
food = [int((randint(0,500))/10)*10, int((randint(0,500))/10)*10]
snake_pos = [[240,240],[240,230],[240,220]]

def draw_snake():
    for position in snake_pos:
        c.create_rectangle(position[0], position[1], position[0]+10, position[1]+10, fill='red')
    c.create_rectangle(snakehead[0], snakehead[1], snakehead[0]+10, snakehead[1]+10, fill='green')
    

def show_food():
    global food

    c.create_rectangle(food[0], food[1], food[0]+10, food[1]+10, fill='#FFFF00')

    if snakehead==food:
        food = [int((randint(0,500))/10)*10, int((randint(0,500))/10)*10]
        snake_pos.append(food)

def left(e):
    global direction
    direction = 'LEFT'

def right(e):
    global direction
    direction = 'RIGHT'

def up(e):
    global direction
    direction = 'UP'

def down(e):
    global direction
    direction = 'DOWN'

root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Left>', left)
root.bind('<Right>', right)

def detect_move():

    global direction
    global snakehead
    global snake_pos


    if direction=='DOWN':
        snakehead[1] += vel
        snake_pos.insert(0,list(snakehead))
        snake_pos.pop()

    if direction=='UP':
        snakehead[1] -= vel
        snake_pos.insert(0,list(snakehead))
        snake_pos.pop()

    if direction=='LEFT':
        snakehead[0] -= vel
        snake_pos.insert(0,list(snakehead))
        snake_pos.pop()

    if direction=='RIGHT':
        snakehead[0] += vel
        snake_pos.insert(0,list(snakehead))
        snake_pos.pop()

run = True

def update():
    detect_move()
    c.delete('all')
    show_food()
    draw_snake()
    root.update()
    root.after(50, update)
    
update()

root.mainloop()
