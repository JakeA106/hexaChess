import tkinter as tk
p = 1
n = 2
b = 3
q = 4
ch = 5
ca = 6
k = 7
row0 =    [0,0,0,0,0]
row1 =   [0,0,0,0,0,0]
row2 =  [0,0,0,2,0,0,0]
row3 = [0,0,0,0,0,0,0,0]
row4 =[0,0,0,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,0,0]
row6 =  [0,0,0,2,0,0,0]
row7 =   [0,0,0,0,0,0]
row8 =    [0,0,0,0,0]
rowcolumn = [row0,row1,row2,row3,row4,row5,row6,row7,row8]
def identifypiece(location):
    if  location == 1:
        return "pawn"
    elif location == 2:
        return "knight"
    elif location == 3:
        return "bishop"
    elif location == 4:
        return "queen"
    elif location == 5:
        return "chancellor"
    elif location == 6:
        return "camel"
    elif location == 7:
        return "king"
def capture(capturer, captured):
    rowcolumn[(int(loc2[0])-1)][(int(loc2[2])-1)] = rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)]
    rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)] = 0
while True:
    loc1 = str(input("What original location? "))
    if rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)] == 0:
        print("There is no piece there!")
    else:
        print("There is a " + str(identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)])) + " there.")

        loc2 = str(input("What new location? "))
        if rowcolumn[(int(loc2[0])-1)][(int(loc2[2])-1)] == 0:
            rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)],rowcolumn[(int(loc2[0])-1)][(int(loc2[2])-1)] = rowcolumn[(int(loc2[0])-1)][(int(loc2[2])-1)],rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)]
            print("The " + str(identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)])) + " at " + loc1 + " moved to " + loc2 + ".")
        else:
            capture(rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)], rowcolumn[(int(loc2[0])-1)][(int(loc2[2])-1)])
            print("The " + str(identifypiece(rowcolumn[(int(loc1[0])-1)][(int(loc1[2])-1)])) + " at " + loc1 + " captured the " + str(identifypiece(rowcolumn[(int(loc2[0])-1)][(int(loc2[2])-1)])) + " at " + loc2)
        for i in range(9):
            print(rowcolumn[i])