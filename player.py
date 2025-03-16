#Coding : utf-8
#Coding by Yodavatar
#Licensed code CC BY-NC-SA 4.0
#Game : Snake

import random

class Player():
    def __init__(self,height:int,width:int) -> None:
        #In the grid
        # 0 corresponds to empty
        # 1 corresponds to snake's body
        # 2 corresponds to a apple

        self.height = height
        self.width = width
        self.snakebody = []
        self.newgame()

    def newgame(self) -> None:
        "Setup a new game"
        self.grid = []

        for i in range(self.height):
            self.grid.append([])
            for _ in range(self.width):
                self.grid[i].append(0)

        self.snakebody.append((int(self.height/2),int(self.width/2)))
        self.lastmove = "Right"
        self.apples = 0
        self.freeze = False
        self.victory = False
        self.newapple()
        self.newapple()

    def checkvictory(self) -> None:
        "Deduce if the game is a victory"
        sizesnake = len(self.snakebody)
        if self.height*self.width == sizesnake:
            self.victory = True
        else:
            self.victory = False

    def checkend(self, i:int,j:int)-> bool:
        "Return if the position in i j is okay for the snake"
        if self.grid[i][j] == 1:
            return False
        return True
    
    def checkapple(self, i:int,j:int)-> bool:
        "Return if the position in i j is an apple"
        if self.grid[i][j] == 2:
            return True
        return False

    def newapple(self) -> None:
        "Add new apple on the grid"
        freeposition = []
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    freeposition.append((i,j))
        
        pos = random.randint(0,len(freeposition)-1)
        i,j = freeposition[pos]
        self.grid[i][j]=2

    def correction_position(self, i:int, j: int)-> tuple:
        "Return the new position if i or j are out the grid"
        if i < 0:
            i = self.width -1
        elif i >= self.width:
            i = 0
        if j < 0:
            j = self.height-1
        elif j >= self.height:
            j = 0
        return (i,j)

    def Move(self) -> None:
        "Update the game, the snake move"
        if self.freeze:
            pass
        else:
            i,j = self.snakebody[-1]#position of the head of the snake

            if self.lastmove == "Up":
                i,j = self.correction_position(i,j-1)
                if self.checkend(i,j):
                    if self.checkapple(i,j):
                        self.snakebody.append((i,j))
                        self.newapple()
                    else:
                        self.snakebody.append((i,j))
                        self.snakebody = self.snakebody[1:]
                else:
                    self.End()

            elif self.lastmove == "Down":
                i,j = self.correction_position(i,j+1)
                if self.checkend(i,j):
                    if self.checkapple(i,j):
                        self.snakebody.append((i,j))
                        self.newapple()
                    else:
                        self.snakebody.append((i,j))
                        self.snakebody = self.snakebody[1:]
                else:
                    self.End()

            elif self.lastmove == "Left":
                i,j = self.correction_position(i-1,j)
                if self.checkend(i,j):
                    if self.checkapple(i,j):
                        self.snakebody.append((i,j))
                        self.newapple()
                    else:
                        self.snakebody.append((i,j))
                        self.snakebody = self.snakebody[1:]
                else:
                    self.End()

            elif self.lastmove == "Right":
                i,j = self.correction_position(i+1,j)
                if self.checkend(i,j):
                    if self.checkapple(i,j):
                        self.snakebody.append((i,j))
                        self.newapple()
                    else:
                        self.snakebody.append((i,j))
                        self.snakebody = self.snakebody[1:]
                else:
                    self.End()

    def ChangeDirection(self, direction:str) -> None:
        "You can change direction only if you don't turn around"
        if self.lastmove == direction:
            pass
        else:
            if "Up" == direction and self.lastmove == "Down":
                pass
            else:
                self.Up()
            if "Down" == direction and self.lastmove == "Up":
                pass
            else:
                self.Down()
            if "Left" == direction and self.lastmove == "Right":
                pass
            else:
                self.Left()
            if "Right" == direction and self.lastmove == "Left":
                pass
            else:
                self.Right()

    def Up(self) -> None:
        "Change the direction for Up"
        self.lastmove = "Up"
    
    def Down(self) -> None:
        "Change the direction for Down"
        self.lastmove = "Down"

    def Left(self) -> None:
        "Change the direction for Left"
        self.lastmove = "Left"

    def Right(self) -> None:
        "Change the direction for Right"
        self.lastmove = "Right"

    def End(self) -> None:
        "Stop the game"
        self.freeze = True
        self.checkvictory()
        if self.victory:
            print("You win with "+str(self.apples)+" apples.")
        else:
            print("You lose with "+str(self.apples)+" apples.")

    def __str__(self) -> None:
        "Print the grid"
        for i in self.grid:
            line = ""
            for j in i:
                line+=j
            print(line)


#Coding : utf-8
#Coding by Yodavatar
#Licensed code CC BY-NC-SA 4.0
#Game : Snake