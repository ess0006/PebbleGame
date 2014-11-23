'''
Created on Nov 22, 2014

@author: Eric
'''
import Tkinter as tk
from Tkinter import *
import HumanPlayer as HumanPlayer
import AIPlayer as AIPlayer
import Game as Game

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, None, None)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, GamePage):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location; 
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)
        
    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()
 
class Menu(tk.Frame):     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        
        self.b1 = Button(root, text="2 Human", command=lambda: controller.show_frame(GamePage))
        self.b1.pack()
        self.b2 = Button(root, text="2 AI", command=lambda: controller.show_frame(GamePage))
        self.b2.pack()
        self.b3 = Button(root, text="1 Human, 1 AI", command=lambda: controller.show_frame(GamePage))
        self.b3.pack()
        

    def set_two_human(self):
        self.game = Game.Game(HumanPlayer.HumanPlayer(), HumanPlayer.HumanPlayer())
    
    def set_two_ai(self):
        self.game = Game.Game(AIPlayer.AIPlayer(), AIPlayer.AIPlayer())
        
    def set_human_ai(self):
        self.game = Game.Game(AIPlayer.AIPlayer(), HumanPlayer.HumanPlayer())


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        
        button = tk.Button(self, text="Go to the start page", 
                           command=lambda: controller.show_frame(Menu))
        button.pack()
        
root = Tk()

app = Main(root)

root.mainloop()