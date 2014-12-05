"""
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard
"""
import Tkinter as tk
import human as Human
import ai as AI
import game as Game


class Main(tk.Tk):
    """
    Entry point.  This class builds each view.
    Adapted from http://stackoverflow.com/questions/7546050/python-tkinter-changing-the-window-basics

    """
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
        """
        Show a frame for the given class.
        @param c: The index of the frame to show.
        """
        frame = self.frames[c]
        frame.tkraise()

    def show_frame_game(self, c, game_type, n, k):
        """
        Show a frame for the given class.
        @param c: The index of the frame to show.
        @param game_type: An int representing the types of players
                          0 - Human vs Human
                          1 - AI vs AI
                          2 - Human vs AI
        @param n: The number of columns per row.
        @param k: The number of pebbles per square.  
        """
        frame = self.frames[c]
        frame.set_game_type(game_type, n, k)
        frame.tkraise()


class Menu(tk.Frame):
    """
    The menu view.

    """
    # creating more constants than should be necessary because radio buttons will group if they have like values
    # These are static - no support for multiple instances of Menu
    STEP = 0
    RUN = 1
    run_or_step = STEP
    WEIGHTED_H1 = 2
    WEIGHTLESS_H1 = 3
    h1 = WEIGHTED_H1
    WEIGHTED_H2 = 4
    WEIGHTLESS_H2 = 5
    h2 = WEIGHTED_H2

    def __init__(self, parent, controller):
        """
        Constructor

        @param parent: The parent view.
        @param controller: The controller for the view.

        """

        tk.Frame.__init__(self, parent)

        self.b1 = Button(root, text="2 Human", command=lambda: controller.show_frame_game(GamePage, 0, int(self.n_text_field.get()), int(self.k_text_field.get())))
        self.b1.pack()
        self.b2 = Button(root, text="2 AI", command=lambda: controller.show_frame_game(GamePage, 1, int(self.n_text_field.get()), int(self.k_text_field.get())))
        self.b2.pack()
        self.b3 = Button(root, text="1 Human, 1 AI", command=lambda: controller.show_frame_game(GamePage, 2, int(self.n_text_field.get()), int(self.k_text_field.get())))
        self.b3.pack()
        self.b3 = Button(root, text="1 AI, 1 Human", command=lambda: controller.show_frame_game(GamePage, 3, int(self.n_text_field.get()), int(self.k_text_field.get())))
        self.b3.pack()
        self.n_label = Label(root, text="Num squares per side:")
        self.n_label.pack()
        self.n_text_field = Entry(root)
        self.n_text_field.pack()
        self.n_label = Label(root, text="Num pebbles per square:")
        self.n_label.pack()
        self.k_text_field = Entry(root)
        self.k_text_field.pack()

        self.run_or_step_label = Label(root, text="Step or Run to end (AI only):")
        self.run_or_step_label.pack()
        Menu.run_or_step = IntVar(master=root)
        Radiobutton(root, text="Step", variable=Menu.run_or_step, value=Menu.STEP).pack(anchor=W)
        Radiobutton(root, text="Run", variable=Menu.run_or_step, value=Menu.RUN).pack(anchor=W)

        self.heuristic1_label = Label(root, text="Player 1 Heuristic (AI only):")
        self.heuristic1_label.pack()
        Menu.h1 = IntVar(master=root)
        Radiobutton(root, text="Weighted", variable=Menu.h1, value=Menu.WEIGHTED_H1).pack(anchor=W)
        Radiobutton(root, text="Weightless", variable=Menu.h1, value=Menu.WEIGHTLESS_H1).pack(anchor=W)

        self.heuristic2_label = Label(root, text="Player 2 Heuristic (AI only):")
        self.heuristic2_label.pack()
        Menu.h2 = IntVar(master=root)
        Radiobutton(root, text="Weighted", variable=Menu.h2, value=Menu.WEIGHTED_H2).pack(anchor=W)
        Radiobutton(root, text="Weightless", variable=Menu.h2, value=Menu.WEIGHTLESS_H2).pack(anchor=W)




class GamePage(tk.Frame):
    """
    The grid of squares.
    """
    def __init__(self, parent, controller):
        """
        Constructor
        @param parent: The parent view.
        @param controller: The controller for the view. 
        """
        tk.Frame.__init__(self, parent)

    def set_game_type(self, game_type, n, k):
        """
        Sets the game type.
        @param game_type: An int representing the types of players
                          0 - Human vs Human
                          1 - AI vs AI
                          2 - Human vs AI (Human first)
                          3 - AI vs Human (AI first)
        @param n: The number of columns per row.
        @param k: The number of pebbles per square.  
        """
        self.grid(row=4, column=k)
        if game_type == 0:
            self.game = Game.game(Human.human_player(), Human.human_player(), n, k)
        elif game_type == 1:
            self.game = Game.game(AI.ai_player(Menu.h1.get()), AI.ai_player(Menu.h2.get()), n, k)
        elif game_type == 2:
            self.game = Game.game(Human.human_player(), AI.ai_player(Menu.h2.get()), n, k)
        else:
            self.game = Game.game(AI.ai_player(Menu.h1.get()), Human.human_player(), n, k)
        self.build_board()

    def build_board(self):
        """
        Builds and displays the board GUI.
        """
        state = self.game.get_state()
        self.buttons = []
        self.buttons.append([])
        self.buttons.append([])
        button = None
        for i in range(len(state)):
            for j in range(len(state[i])):
                button = tk.Button(self, text=state[i][j],
                               command=lambda i=i, j=j: self.move(i, j))
                button.grid(row=i, column=j)
                self.buttons[i].append(button)

        if self.game.has_ai():
            self.arrow = tk.Button(self, text=">", command=lambda: self.ai_move())
            if self.game.is_next_ai():
                if Menu.run_or_step.get() == Menu.STEP:
                    self.arrow.grid(row=3, columnspan=self.game.get_n())

        self.turn_label = tk.Label(self, text="Turn:")
        self.turn_label.grid(row=4, columnspan=self.game.get_n())
        self.player_label = tk.Label(self, text="Player 1")
        self.player_label.grid(row=5, columnspan=self.game.get_n())

        if self.game.is_next_ai():
            if Menu.run_or_step.get() == Menu.RUN:
                    self.ai_move()


    def move(self, i, j):
        """
        Submits a move to the game instance.
        @param i: The i coordinate.
        @param j: The j coordinate. 
        """
        if isinstance(self.game.next_to_move(), Human.human_player):
            if(self.game.valid_move(i, j)):
                self.game.move(i, j)
            self.update_gui()
            if self.game.is_next_ai():
                if Menu.run_or_step.get() == Menu.STEP:
                    self.arrow.grid(row=3, columnspan=self.game.get_n())
                else:
                    self.ai_move()

    def ai_move(self):
        """
        Submits a move for the AI player.
        """
        if isinstance(self.game.next_to_move(), AI.ai_player):
            self.game.ai_move()
            self.update_gui()
            if self.game.is_next_ai():
                if Menu.run_or_step.get() == Menu.RUN:
                    self.ai_move()
            else:
                self.arrow.grid_forget()

    def update_gui(self):
        """
        Updates the board GUI after a move.
        """
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
