from tkinter import *
import threading
import time



#Dummy variable
threadState = 0
x = 5

def check():
    if threadState > 0:
        run()


def run():
    if x >5:
        root.configure(background='red') #Change the background to red
        theLabel.config(text="You are too close")
    else:
        root.configure(background='lightgreen')  # Change the background to green
        theLabel.config(text="Your distance is fine")

#create window
root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#Label with message
theLabel = Label(root,text="Warning")
theLabel.pack()

#Button stop the thread
button = Button(root,text="Start/Stop",command=check)
button.pack()

#Window Properties
root.geometry("500x200")
root.configure(background='White')
root.title("Sensor checker")
root.mainloop()







