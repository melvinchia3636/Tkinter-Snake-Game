from tkinter import *
from random import randint
from tkinter.font import Font

root = Tk()
root.config(bg='#FFFFFE')
root.geometry('1920x1080')
root.attributes('-transparentcolor', '#FFFFFE')
root.wm_attributes('-fullscreen', True)
root.wm_attributes('-topmost', True)

c = Canvas(root, width=1920, height=900, bg='#FFFFFE', borderwidth=0, highlightthickness=0)
counter = Label(root, text='0', font=Font(size=50, family='Bahnschrift SemiBold'), bg='#FFFFFE', fg='white')
stop = Label(root, text='STOP', font=Font(size=150, family='Bahnschrift SemiBold'), bg='#FFFFFE', fg='white')
counter.place(x=960, y=50, anchor='center')
c.place(x=960, y=550, anchor='center')

vel = 20

direction = 'DOWN'

root.title('Snake Game')

snakehead = [240, 240]
food = [int((randint(0,1920))/20)*20, int((randint(0,900))/20)*20]
snake_pos = [[240,240],[240,230]]

def draw_snake():
    for position in snake_pos:
        c.create_rectangle(position[0], position[1], position[0]+18, position[1]+18, fill='#00FFFF', outline='#FFFFFE')
    c.create_rectangle(snakehead[0], snakehead[1], snakehead[0]+18, snakehead[1]+18, fill='yellow', outline='#FFFFFE')
    

def show_food():
    global food

    c.create_oval(food[0], food[1], food[0]+18, food[1]+18, fill='#FFFF00', outline='#FFFFFE')

    if snakehead==food:
        food = [int((randint(0,1920))/20)*20, int((randint(0,900))/20)*20]
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

def stop_start(e):
    global run
    if run == True:
        run = False
    else:
        run = True

root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<space>', stop_start)

def detect_move():

    global direction
    global snakehead
    global snake_pos


    if direction=='DOWN':
        snakehead[1] += vel
        snake_pos.insert(0,list(snakehead))
        if snakehead[1] >= 900:
            snake_pos[0][1] = 0
            snakehead[1] = 0
        snake_pos.pop()

    if direction=='UP':
        snakehead[1] -= vel
        snake_pos.insert(0,list(snakehead))
        if snakehead[1] <= -20:
            snake_pos[0][1] = 880
            snakehead[1] = 880
        snake_pos.pop()

    if direction=='LEFT':
        snakehead[0] -= vel
        snake_pos.insert(0,list(snakehead))
        if snakehead[0] <= -20:
            snake_pos[0][0] = 1900
            snakehead[0] = 1900
        snake_pos.pop()

    if direction=='RIGHT':
        snakehead[0] += vel
        snake_pos.insert(0,list(snakehead))
        if snakehead[0] >= 1920:
            snake_pos[0][0] = 0
            snakehead[0] = 0
        snake_pos.pop()
    counter.config(text=str(len(snake_pos)-1))

run = True

def update():
    if run == True:
        stop.place_forget()
        detect_move()
        c.delete('all')
        draw_snake()
        show_food()
        root.update()
    if run == False:
        pass
        #stop.place(x=960, y=540, anchor='center')
        
    root.after(30, update)
    
update()

root.mainloop()
