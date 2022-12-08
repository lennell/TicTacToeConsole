# This is a sample Python script.
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
combinations = [[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6],]
pl1 = ["",0,"X"]
pl2 = ["",0,"O"]

def printBoard():
    clear()
    print("******* Current Board *******");
    print("* 1,2,3 * "+str(board[:3])+"*");
    print("* 4,5,6 * "+str(board[3:6])+"*");
    print("* 7,8,9 * "+str(board[6:])+"*");
    print("****************************");
    p1 = pl1[0] + ("* " if currP == pl1 else " ");
    p2 = pl2[0] + ("*" if currP == pl2 else "");

def clear():
    if os.name == "nt":
        os.system("cls");
    else:
        os.system("clear");


# Press the green button in the gutter to run the script.
print("TicTacToe Enter player names:" + os.name);
pl1[0] =  input("Player 1: ");
pl2[0] =  input("Player 2: ");
currP = pl1
x = 0;
y = 0;

printBoard()

def hasThreeInrow(currSign):
    for cc in combinations:
        count = 0;
        for c in cc:
            if board[c] == currSign:
                count = count + 1;
                if count == 3:
                    return True;
    return False


while True:
    if (currP[1]>2):
        old = int(input(currP[0] + " select from position: "))
        board[old-1] = "-";
        printBoard()
    new = int(input(currP[0] + " select destination position: "))
    currP[1] = currP[1]+1
    board[new-1]=currP[2]
    printBoard()
    if hasThreeInrow(currP[2]):
        break
    if (currP[0]==pl1[0]):
        currP=pl2
    else:
        currP=pl1

print("------ Ended----")
print("Winner is " + currP[0])

