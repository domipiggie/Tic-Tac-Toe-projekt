#Játéktábla létrehozása
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
#Szükséges változók deklarálása
turn = 1
col = -1
row = -1
win = False
lastPlayer = ""

#Funkció ami megnézi hogy van-e még játszható lépés a játéktáblán
def areMovesLeft():
    for i in board:
        for j in i:
            if j == "-":
                return True
    return False

def winner(l):
    return ((board[0][0] == l and board[0][1] == l and board[0][2] == l) or
            (board[1][0] == l and board[1][1] == l and board[1][2] == l) or
            (board[2][0] == l and board[2][1] == l and board[2][2] == l) or
            (board[0][0] == l and board[1][0] == l and board[2][0] == l) or
            (board[0][1] == l and board[1][1] == l and board[2][1] == l) or
            (board[0][2] == l and board[1][2] == l and board[2][2] == l) or
            (board[0][0] == l and board[1][1] == l and board[2][2] == l) or
            (board[0][2] == l and board[1][1] == l and board[2][0] == l))

#Fő ciklus, ami addig fut, amíg van játszható lépés a táblán
while areMovesLeft() and not win:
    #Ciklusváltozó
    isEmpty = False
    #Ciklus ami bekéri a felhasználótól hogy hova szeretne lépni és ellenőrzi hogy üres-e a terület ahova lépni szeretne
    while not isEmpty:
        row = int(input())
        col = int(input())
        if board[row][col] == "-":
            isEmpty = True
    
    #Megfelelő játékos jelének letétele (minden páratlan kör x, minden páros kör o)
    if turn % 2 != 0:
        board[row][col] = "x"
        lastPlayer = "x"
    else:
        board[row][col] = "o"
        lastPlayer = "o"
    
    #Körök száma változó növelése
    turn += 1
    
    #Jelenlegi játéktábla kiíratása
    for i in board:
        print(i)
    
    if winner(lastPlayer):
        print("A játékot", lastPlayer, "nyerte!")
        win = True

input("Nyomja meg az entert a kilépéshez.")