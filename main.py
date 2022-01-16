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

#Funkció ami megnézi hogy van-e még játszható lépés a játéktáblán
def areMovesLeft():
    for i in board:
        for j in i:
            if j == "-":
                return True
    return False

#Fő ciklus, ami addig fut, amíg van játszható lépés a táblán
while areMovesLeft():
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
    else:
        board[row][col] = "o"
    
    #Körök száma változó növelése
    turn += 1
    
    #Jelenlegi játéktábla kiíratása
    for i in board:
        print(i)