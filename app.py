#Coding : utf-8
#Coding by Yodavatar
#Licensed code CC BY-NC-SA 4.0
#Game : Snake

from player import*
from tkinter import*

class App(Tk):
    def __init__(self) -> None:
        "Open the App"
        super().__init__()
        self.height = 10
        self.width = 5

        #Create the grid
        self.init_grid()

        #Create the player
        self.player = Player(height=self.height,width=self.width)

        #Touch event
        self.bind("<Key>", self.keyboard)

        #Window Parameters
        self.configure(bg="#333333", padx=10, pady=10)
        self.geometry("700x800")
        self.title("Snake")

        #new game
        #self.new_game()


    def init_grid(self) -> None:
        "init the grid with two parameters height and width"
        for i in range(self.height):
            self.grid_rowconfigure(i, weight=1,uniform="same_group")
        
        for i in range(self.width):
            self.grid_columnconfigure(i, weight=1,uniform="same_group")

        self.default_button_style = {
            "bg" : "#E7B10A", "fg": "white", "highlightthickness": 0,
            "font": ("Arial", 25, "bold")
        }
        self.default_button_grid = {"padx": 2, "pady": 2, "sticky": "nsew"}
        
        self.grid_label = []
        for i in range(self.height):
            self.grid_label.append([])
            for j in range(self.width):
                self.grid_label[i].append(None)
                self.grid_label[i][j] = Label(self, text="", **self.default_button_style)
                self.grid_label[i][j].grid(column=i, row=j,**self.default_button_grid)

    def new_game(self) -> None:
        self.score = 0
        self.gel = 0

        self.grille = []
        for i in range(4):
            self.grille.append([])  
            for o in range(4):
                self.grille[i].append([])
        
        #2 cases at the beginning
        for i in range(2):
            self.module()
        self.afficher()

    def update_grid(self) -> None:
        for i in range(self.height):  
            for o in range(self.width):
                self.grid_label[i][o] = Label(self, text="", **self.default_button_style)
                self.grid_label[i][o].grid(column=0, row=0,**self.default_button_grid)

    
    def keyboard(self,event) -> None:
        "Manage touch"
        if event.keysym == "Up":
            self.player.ChangeDirection("Up")
        elif event.keysym == "Down":
            self.player.ChangeDirection("Down")
        elif event.keysym == "Left":
            self.player.ChangeDirection("Left")
        elif event.keysym == "Right":
            self.player.ChangeDirection("Right")
        if event.keysym == "BackSpace":
            self.new_game()
        elif event.keysym == "Escape":
            exit()


#Coding : utf-8
#Coding by Yodavatar
#Licensed code CC BY-NC-SA 4.0
#Game : Snake