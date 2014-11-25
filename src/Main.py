'''
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard
'''
import Tkinter as tk
from Tkinter import *
import HumanPlayer as HumanPlayer
import AIPlayer as AIPlayer
import Game as Game

class Main(tk.Tk):
    '''
    Entry point.  This class builds each view.
    '''
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, None, None)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(5, weight=1)
        container.grid_columnconfigure(5, weight=1)

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
        '''
        Show a frame for the given class.
        @param c: The index of the frame to show.
        '''
        frame = self.frames[c]
        frame.tkraise()
        
    def show_frame_game(self, c, game_type, n, k):
        '''
        Show a frame for the given class.
        @param c: The index of the frame to show.
        @param game_type: An int representing the types of players
                          0 - Human vs Human
                          1 - AI vs AI
                          2 - Human vs AI
        @param n: The number of columns per row.
        @param k: The number of pebbles per square.  
        '''
        frame = self.frames[c]
        frame.set_game_type(game_type, n, k)
        frame.tkraise()
 
class Menu(tk.Frame):     
    '''
    The menu view.
    '''
    def __init__(self, parent, controller):
        '''
        Constructor
        @param parent: The parent view.
        @param controller: The controller for the view. 
        '''
        tk.Frame.__init__(self, parent)
        
        self.b1 = Button(root, text="2 Human", command=lambda: controller.show_frame_game(GamePage, 0, int(self.n_text_field.get()), int(self.k_text_field.get())))
        self.b1.pack()
        self.b2 = Button(root, text="2 AI", command=lambda: controller.show_frame_game(GamePage, 1, int(self.n_text_field.get()), int(self.k_text_field.get())))
        self.b2.pack()
        self.b3 = Button(root, text="1 Human, 1 AI", command=lambda: controller.show_frame_game(GamePage, 2, int(self.n_text_field.get()), int(self.k_text_field.get())))
        self.b3.pack()
        self.n_label = Label(root, text="Num squares per side:")
        self.n_label.pack()
        self.n_text_field = Entry(root)
        self.n_text_field.pack()
        self.n_label = Label(root, text="Num pebbles per square:")
        self.n_label.pack()
        self.k_text_field = Entry(root)
        self.k_text_field.pack()
        
        


class GamePage(tk.Frame):
    '''
    The grid of squares.
    '''
    def __init__(self, parent, controller):
        '''
        Constructor
        @param parent: The parent view.
        @param controller: The controller for the view. 
        '''
        tk.Frame.__init__(self, parent)
    
    def set_game_type(self, game_type, n, k):
        '''
        Sets the game type.
        @param game_type: An int representing the types of players
                          0 - Human vs Human
                          1 - AI vs AI
                          2 - Human vs AI
        @param n: The number of columns per row.
        @param k: The number of pebbles per square.  
        '''
        self.grid(row=4, column=k)
        if game_type == 0:
            self.game = Game.Game(HumanPlayer.HumanPlayer(), HumanPlayer.HumanPlayer(), n, k)
        elif game_type == 1:
            self.game = Game.Game(AIPlayer.AIPlayer(), AIPlayer.AIPlayer(), n, k)
        else:
            self.game = Game.Game(HumanPlayer.HumanPlayer(), AIPlayer.AIPlayer(), n, k)
        self.build_board()
        
    def build_board(self):
        '''
        Builds and displays the board GUI.
        '''
        state = self.game.get_state()
        self.buttons = []
        self.buttons.append([])
        self.buttons.append([])
        button = None
        for i in range(len(state)):
            for j in range(len(state[i])):
                button = tk.Button(self, text=state[i][j], 
                               command= lambda i=i,j=j: self.move(i, j))
                button.grid(row=i, column=j)
                self.buttons[i].append(button)
                
        if self.game.has_ai():
            self.arrow = tk.Button(self, text=">", command=lambda: self.ai_move())
            if self.game.is_next_ai():
                self.arrow.grid(row=3,columnspan=self.game.get_n())
            
        self.turn_label = tk.Label(self, text="Turn:")
        self.turn_label.grid(row=4,columnspan=self.game.get_n())
        self.player_label = tk.Label(self, text="Player 1")
        self.player_label.grid(row=5,columnspan=self.game.get_n())
        
            
    def move(self, i, j):
        '''
        Submits a move to the Game instance.
        @param i: The i coordinate.
        @param j: The j coordinate. 
        '''
        if isinstance(self.game.next_to_move(), HumanPlayer.HumanPlayer):
            if(self.game.valid_move(i,j)):
                self.game.move(i, j)
            self.update_gui()
            if self.game.is_next_ai():
                self.arrow.grid(row=3,columnspan=self.game.get_n())
    
    def ai_move(self):
        '''
        Submits a move for the AI player.
        '''
        if isinstance(self.game.next_to_move(), AIPlayer.AIPlayer):
            self.game.ai_move()
            self.update_gui()
            if not self.game.is_next_ai():
                self.arrow.grid_forget()
    
    def update_gui(self):
        '''
        Updates the board GUI after a move.
        '''
        state = self.game.get_state()
        for i in range(len(state)):
            for j in range(len(state[i])):
                self.buttons[i][j]["text"] = state[i][j]
        winner = self.game.winner()
        if winner != 0:
            self.player_label["text"] = "Player " + str(winner) + " wins!"
        else:
            self.player_label["text"] = "Player " + str(self.game.turn)
        
root = Tk()

app = Main(root)

root.mainloop()