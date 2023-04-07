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
while True:
    loc1 = str(input("What original location? "))
    loc2 = str(input("What new location? "))
    rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)],rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)] = rowcolumn[(int(loc2[0])-1)][(int(loc2[1])-1)],rowcolumn[(int(loc1[0])-1)][(int(loc1[1])-1)]
    for i in range(9):
        print(rowcolumn[i])