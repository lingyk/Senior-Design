from tkinter import *
from tkinter.ttk import *
import circle

root = Tk(className='DRS_UI')
#root.geometry('800x800')
myCanvas = Canvas(root,width = 600, height = 500)
style = Style()
myCanvas.pack()


#Label(root, text = 'Health/Status', font =('Verdana', 15)).pack(side = TOP, pady = 10) 
  

#any underline text adjustment
circle.create_text(55,25,myCanvas,text = "Health/Status",font = 'Times 12 underline') #adjust health/status position, font
circle.create_text(35,130,myCanvas,text = "Utility",font = 'Times 12 underline')
circle.create_text(160,130,myCanvas,text = "Reflectivity",font = 'Times 12 underline')


#any created circle adjustment 
circle.create_circle(35,55,10,myCanvas,fill = 'red',outline = 'red')
circle.create_circle(75,55,10,myCanvas,fill = 'yellow',outline = 'yellow')
circle.create_circle(115,55,10,myCanvas,fill = 'green',outline = 'green')

#any text adjustment
circle.create_text(35,75,myCanvas,text = 'Error',font = 'Times 12 ')
circle.create_text(75,75,myCanvas,text = 'Busy',font = 'Times 12 ')
circle.create_text(115,75,myCanvas,text = 'Ready',font = 'Times 12 ')

#any created polygon adjustment
circle.round_rectangle(myCanvas,5, 5, 150, 100, radius=20, outline = 'black', fill= '') #150x100 area
circle.round_rectangle(myCanvas,5,110,200,400,radius=20, outline = 'black', fill = '') #200x400 area

#any buttom adjustment
style.configure('TButton', font = 'Times 12', relief = 'sunken', foreground = 'black')
Button(text = 'Data File',style = 'TButton').place(x = 15, y = 150)




mainloop() 
