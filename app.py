#Coding : utf-8
#Coding by Yodavatar
#Licensed code Mozilla Public License 2.0
#Game : Snake

from player import*
import tkinter as tk


class App(tk.Tk):
    def __init__(self) -> None:
        "Open the App"
        super().__init__()
        self.height = 10
        self.width = 10

        #Create the grid
        self.init_grid()

        #Create the player
        self.player = Player(height=self.height,width=self.width)
        self.player.newgame()

        #Touch event
        self.bind("<Key>", self.keyboard)

        #Window Parameters
        self.configure(bg="#333333", padx=10, pady=10)
        self.geometry("700x700")
        self.title("Snake")

        #Update the grid
        self.timeupdate = 200
        self.after(self.timeupdate, self.update_grid)

    def newgame(self) -> None:
        "New game"
        self.player.newgame()

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
                self.grid_label[i][j] = tk.Label(self, text="", **self.default_button_style)
                self.grid_label[i][j].grid(column=i, row=j,**self.default_button_grid)

    def update_grid(self) -> None:
        #In the grid
        # 0 corresponds to empty
        # 1 corresponds to snake's body
        # 2 corresponds to snake's head
        # 3 corresponds to a apple
        self.after(self.timeupdate, self.update_grid)
        self.player.move()
        for i in range(self.height):  
            for o in range(self.width):
                l = self.player.grid[i][o]
                if l == 0:
                    self.grid_label[i][o].config(bg="black")
                if l == 1:
                    self.grid_label[i][o].config(bg="grey")
                if l == 2:
                    self.grid_label[i][o].config(bg="purple")
                if l == 3:
                    self.grid_label[i][o].config(bg="red")
 
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
            self.newgame()
        elif event.keysym == "Escape":
            exit()


#Coding : utf-8
#Coding by Yodavatar
#Licensed code Mozilla Public License 2.0
#Game : Snake