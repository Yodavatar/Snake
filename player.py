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
        # 2 corresponds to snake's head
        # 3 corresponds to a apple
        self.height = height
        self.width = width
        self.headposition = (0,0)
        self.snakebody = []

    def newgame(self) -> None:
        "Setup a new game"
        self.grid = []

        for i in range(self.height):
            self.grid.append([])
            for _ in range(self.width):
                self.grid[i].append(0)

        self.snakebody = []
        self.snakebody.append((int(self.height/2),int(self.width/2)))
        self.headposition = (int(self.height/2),int(self.width/2))
        self.grid[int(self.height/2)][int(self.width/2)] = 2
        self.lastmove = "Right"
        self.apples = 0
        self.freeze = False
        self.modifieddirection = False
        self.newapple()
        self.newapple()

    def checkvictory(self) -> bool:
        "Deduce if the game is a victory"
        sizesnake = len(self.snakebody)
        if self.height*self.width == sizesnake:
            return True
        return False

    def checkend(self, i:int,j:int)-> bool:
        "Return if the position in i j is okay for the snake"
        if self.grid[i][j] == 1 or self.grid[i][j] == 2:
            return False
        return True
    
    def checkapple(self, i:int,j:int)-> bool:
        "Return if the position in i j is an apple"
        if self.grid[i][j] == 3:
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
        self.grid[i][j]=3

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

    def reaction_move(self,headi:int,headj:int,i:int,j:int) -> None:
        "Update the snake"
        if self.checkend(i,j):
            if self.checkapple(i,j):
                self.apples += 1
                self.snakebody.append((i,j))
                self.grid[headi][headj] = 1
                self.headposition = (i,j)
                self.grid[i][j] = 2
                self.newapple()
            else:
                self.snakebody.append((i,j))
                self.grid[headi][headj] = 1
                self.headposition = (i,j)
                self.grid[i][j] = 2
                tail_i,tail_j = self.snakebody[0]
                self.grid[tail_i][tail_j] = 0
                self.snakebody = self.snakebody[1:]
        else:
            self.End()

    def move(self) -> None:
        "Update the game, the snake move"
        if self.freeze:
            return
        else:
            self.modifieddirection = False
            headi,headj = self.headposition#position of the head of the snake
            if self.lastmove == "Up":
                i,j = self.correction_position(headi,headj-1)
                self.reaction_move(headi,headj,i,j)

            elif self.lastmove == "Down":
                i,j = self.correction_position(headi,headj+1)
                self.reaction_move(headi,headj,i,j)

            elif self.lastmove == "Left":
                i,j = self.correction_position(headi-1,headj)
                self.reaction_move(headi,headj,i,j)

            elif self.lastmove == "Right":
                i,j = self.correction_position(headi+1,headj)
                self.reaction_move(headi,headj,i,j)

    def ChangeDirection(self, direction:str) -> None:
        "You can change direction only if you don't turn around"
        if self.lastmove == direction:
            return
        else:
            if "Up" == direction and self.modifieddirection == False:
                if self.lastmove == "Down":
                    return
                else:
                    self.Up()
                    self.modifieddirection = True

            if "Down" == direction and self.modifieddirection == False:
                if self.lastmove == "Up":
                    return
                else:
                    self.Down()
                    self.modifieddirection = True

            if "Left" == direction and self.modifieddirection == False:
                if self.lastmove == "Right":
                    return
                else:
                    self.Left()
                    self.modifieddirection = True

            if "Right" == direction and self.modifieddirection == False:
                if self.lastmove == "Left":
                    return
                else:
                    self.Right()
                    self.modifieddirection = True

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
        if self.checkvictory():
            print("You win with "+str(self.apples)+" apples.")
        else:
            print("You lose with "+str(self.apples)+" apples.")

    def __str__(self) -> str:
        "Print the grid"
        text = ""
        for i in self.grid:
            line = ""
            for j in i:
                line+=str(j)+" "
            text+=line+"\n"
        return text


#Coding : utf-8
#Coding by Yodavatar
#Licensed code CC BY-NC-SA 4.0
#Game : Snake