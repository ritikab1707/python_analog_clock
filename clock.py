import tkinter as tk
import time
import math 

WIDTH=400
HEIGHT=400

m=tk.Tk()
m.title("Analog Clock")
canvas=tk.Canvas(m,width=WIDTH,height=HEIGHT,bg="white")
canvas.pack()

def clock():
    canvas.delete("all")
    now=time.localtime()
    hour=now.tm_hour%12
    minute=now.tm_min
    seconds=now.tm_sec

    #shape of clock
    canvas.create_oval(2,3,WIDTH,HEIGHT,outline="black",width=2)

    #hour numbers
    for i in range(12):
        angle=i* math.pi/6 - math.pi/2
        x=WIDTH/2 + 0.7* WIDTH/2 * math.cos(angle)
        y=HEIGHT/2 + 0.7* WIDTH/2 * math.sin(angle)
        if i==0:
            canvas.create_text(x,y-10,text=str(i+12),font=("Roboto",15))
        else:
            canvas.create_text(x,y,text=str(i),font=("Roboto",15))
    
    #minute lines
    for i in range(60):
        angle=i* math.pi/30 - math.pi/2
        x1=WIDTH/2 + 0.8* WIDTH/2 *math.cos(angle)
        y1=HEIGHT/2 + 0.8* HEIGHT/2 *math.sin(angle)
        x2=WIDTH/2 + 0.9* WIDTH/2 *math.cos(angle)
        y2=HEIGHT/2 + 0.9* HEIGHT/2 *math.sin(angle)
        if i%5==0:
            canvas.create_line(x1,y1,x2,y2,fill="black",width=3)
        else:
            canvas.create_line(x1,y1,x2,y2,fill="black",width=1)
    
    #hour hands
    hour_angle=(hour+minute/60)* math.pi/6 - math.pi/2
    hour_x=WIDTH/2 + 0.5 * WIDTH/2 *math.cos(hour_angle)
    hour_y=HEIGHT/2 + 0.5 * HEIGHT/2 *math.sin(hour_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,hour_x,hour_y,fill="black",width=6)
    
    #minute hands
    minute_angle=(minute+seconds/60)* math.pi/30 - math.pi/2
    minute_x=WIDTH/2 + 0.7 * WIDTH/2 *math.cos(minute_angle)
    minute_y=HEIGHT/2 + 0.7 * HEIGHT/2 *math.sin(minute_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,minute_x,minute_y,fill="black",width=4)

    #second hands
    second_angle=seconds* math.pi/30 - math.pi/2
    second_x=WIDTH/2 + 0.6 * WIDTH/2 *math.cos(second_angle)
    second_y=HEIGHT/2 + 0.6 * HEIGHT/2 *math.sin(second_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,second_x,second_y,fill="red",width=2)

def update_clock():
    clock()
    canvas.after(1000, update_clock)  # Schedule the next update after 1000 milliseconds (1 second)

update_clock()

m.mainloop()
