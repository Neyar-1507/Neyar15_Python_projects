def board():
    print("        |        |        ")
    print(f"  {a}     |   {b}    |   {c}    ")
    print("________|________|________")
    print("        |        |        ")
    print(f"  {d}     |   {e}    |   {f}    ")
    print("________|________|________")
    print("        |        |        ")
    print(f"  {g}     |   {h}    |   {i}    ")
    print("        |        |        ")

def board_pl():
    print("        |        |        ")
    print(f"  {a1}     |   {b1}    |   {c1}    ")
    print("________|________|________")
    print("        |        |        ")
    print(f"  {d1}     |   {e1}    |   {f1}    ")
    print("________|________|________")
    print("        |        |        ")
    print(f"  {g1}     |   {h1}    |   {i1}    ")
    print("        |        |        ")

def check():
    if a1=="X" and b1=="X" and c1 == "X":
        print("Player X Wins!")
        exit()
    elif a1=="O" and b1=="O" and c1 == "O":
        print("Player O Wins!")
        exit()
    elif d1=="X" and e1=="X" and f1 == "X":
        print("Player X Wins!")
        exit()
    elif d1=="O" and e1=="O" and f1 == "O":
        print("Player O Wins!")
        exit()
    elif g1=="X" and h1=="X" and i1 == "X":
        print("Player X Wins!")
        exit()
    elif g1=="O" and h1=="O" and i1 == "O":
        print("Player O Wins!")
        exit()
    elif a1=="X" and e1=="X" and i1 == "X":
        print("Player X Wins!")
        exit()
    elif a1=="O" and e1=="O" and i1 == "O":
        print("Player O Wins!")
        exit()
    elif c1=="X" and e1=="X" and g1 == "X":
        print("Player X Wins!")
        exit()
    elif c1=="O" and e1=="O" and g1 == "O":
        print("Player O Wins!")
        exit()
    elif a1=="X" and d1=="X" and g1 == "X":
        print("Player X Wins!")
        exit()
    elif a1=="O" and d1=="O" and g1 == "O":
        print("Player O Wins!")
        exit()
    elif b1=="X" and e1=="X" and h1 == "X":
        print("Player X Wins!")
        exit()
    elif b1=="O" and e1=="O" and h1 == "O":
        print("Player O Wins!")
        exit()
    elif c1=="X" and f1=="X" and i1 == "X":
        print("Player X Wins!")
        exit()
    elif c1=="O" and f1=="O" and i1 == "O":
        print("Player O Wins!")
        exit()


a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9

a1=" "
b1=" "
c1=" "
d1=" "
e1=" "
f1=" "
g1=" "
h1=" "
i1=" "

chance=[1,2,3,4,5,6,7,8,9]
board()
for i in range(5):
    x=int(input("Where do you want to place X: "))

    while x not in chance:
        print("Enter other number as it is occupied!") 
        x=int(input("Where do you want to place X: "))
        board_pl()


    while x in chance:
        if x==1:
            a1="X"
            chance.remove(1)
            board_pl()
            check()
        elif x==2:
            b1="X"
            chance.remove(2)
            board_pl()
            check()
        elif x==3:
            c1="X"
            chance.remove(3)
            board_pl()
            check()
        elif x==4:
            d1="X"
            chance.remove(4)
            board_pl()
            check()
        elif x==5:
            e1="X"
            chance.remove(5)
            board_pl()
            check()
        elif x==6:
            f1="X"
            chance.remove(6)
            board_pl()
            check()
        elif x==7:
            g1="X"
            chance.remove(7)
            board_pl()
            check()
        elif x==8:
            h1="X"
            chance.remove(8)
            board_pl()
            check()
        elif x==9:
            i1="X"
            chance.remove(9)
            board_pl()
            check()

        

    o=int(input("Where do you want to place O: "))

    while o not in chance:
        print("Enter other number as it is occupied!") 
        o=int(input("Where do you want to place O: "))
        board_pl()

    while o in chance:
        if o==1:
            a1="O"
            chance.remove(1)
            board_pl()
            check()
        elif o==2:
            b1="O"
            chance.remove(2)
            board_pl()
            check()
        elif o==3:
            c1="O"
            chance.remove(3)
            board_pl()
            check()
        elif o==4:
            d1="O"
            chance.remove(4)
            board_pl()
            check()
        elif o==5:
            e1="O"
            chance.remove(5)
            board_pl()
            check()
        elif o==6:
            f1="O"
            chance.remove(6)
            board_pl()
            check()
        elif o==7:
            g1="O"
            chance.remove(7)
            board_pl()
            check()
        elif o==8:
            h1="O"
            chance.remove(8)
            board_pl()
            check()
        elif o==9:
            i1="O"
            chance.remove(9)
            board_pl()
            check()
   
    
    
        
