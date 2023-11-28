from Igrac import Igrac

def kreirajTablu(n):
    if(n % 2 != 0 or n > 16 or n < 8):
        raise Exception("Lose uneta vrednost")
   
    vel_table = n*n
    broj_figura = (n * n - 2 * n) / 2

    if(broj_figura % 8 != 0):
        raise Exception("Broj figura mora da bude deljiv sa 8")
    
    broj_stekova = broj_figura / 8
 
    tabla = []

    belo_polje = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    crno_polje = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]

    for row in range(n):
        red = []
        for col in range(n):
            if (row + col) % 2 == 0:
                polje = [row.copy() for row in crno_polje]
                red.append(polje)
            else:
                polje = [row.copy() for row in belo_polje]
                red.append(polje)
        tabla.append(red)
    return tabla


def prikazi_tablu(tabla, n):
    print(' ', end='   ')
    for i in range(n):
        print(i+1, end="     ")
    print()

    for i in range(n):
        for j in range(3):
            if j == 1:
                print(chr(65 + i), end=' ')
            else:
                print(' ', end=' ')

            for k in range(n):
                for z in range(3):
                    print(tabla[i][k][j][z], end=" ")
            print()


def inicijalno_stanje(tabla, n):
    for index in range(1,n * (n - 2)):
        j = int(index % n)
        i = int((index / n) + 1)

        if (i + j) % 2 == 0:
            if(i % 2 == 0):
                tabla[i][j][2][0] = 'O'
            else:
                tabla[i][j][2][0] = 'X'


def unos_poteza():
    print("Unesite red steka")
    red = input()
    print("Unesite kolonu steka")
    kolona = int(input())
    print("Unesite poziciju u steku")
    poz = int(input())
    print("Unesite smer kretanja(GL, GD, DL, DD)")
    smer = input()

    return [red, kolona, poz, smer]

def izaberi_prvog():
    print("Izaberi ko prvi igra(covek - 1, racunar - 2)")
    prvi = int(input())
    if(prvi != 1 and prvi != 2):
        raise Exception("Pogresan unos")
    return prvi
    
    
def pozicija(pozicija):
    r = int(pozicija // 3)
    c = int(pozicija % 3)
    c_copy = c
    if(pozicija in [6,7,8]):
        r = r - 2
    elif(pozicija in [0,1,2]):
        r = r + 2
    return (r, c)

def odigraj(tabla, n, potez, igrac):
    red = ord(potez[0]) - 65
    kolona = int(potez[1]) - 1
    poz =  potez[2]

    p = pozicija(poz)
    r = p[0]
    c = p[1]
    c_copy = c
    #. . . 
    #X . . 
    #X O X
    #[O X X X]

    polje = tabla[red][kolona]
    stek = []

    if(postoji_u_steku(tabla, red, kolona,poz)):
        nadjen = False 
        for i in range(r,-1,-1):
            for j in range(3):
                e = c_copy % 3
                if(polje[i][e] != '.'):
                    stek.append(polje[i][e])
                    polje[i][e] = '.'
                else:
                    nadjen = True
                    break
                c_copy = c_copy + 1
                if e == 2:
                    break
            if nadjen:
                break

    print(stek)

    print(postoje_figure(tabla, red, kolona))
    # if potez[3] == 'GL':

    # elif potez[3] == 'GD':

    # elif potez[3] == 'DL':
    
    # elif potez[3] == 'GD':


def postoji_polje(n, row, col):
    if row < 0 or row > n:
        return False
    if col < 0 or col > n:
        return False
    if (row + col) % 2 !=0:
        return False
    return True

def postoje_figure(tabla, row, col):
    if tabla[row][col][2][0] == '.' or tabla[row][col][2][0] == ' ':
        return False
    else:
        return True

def postoji_u_steku(tabla, row, col, poz):
    p = pozicija(poz)
    if tabla[row][col][p[0]][p[1]] == '.' or tabla[row][col][p[0]][p[1]] == ' ':
        return False
    else:
        return True

def proveri_smer(smer):
    if smer == 'GL' or smer == 'GD' or smer == 'DL' or smer == 'DD':
        return True
    return False

def prazna_tabla(tabla, n):
    prazna = True
    for i in range(n):
        for j in range(n):
            if postoje_figure(tabla,i,j):
                prazna = False
    return prazna
def prekini(n, igrac1:Igrac, igrac2: Igrac):
    broj_figura = (n * n - 2 * n) / 2
    broj_stekova = broj_figura / 8

    if igrac1.poeni > broj_stekova / 2 or igrac2.poeni > broj_stekova / 2:
        return True
    return False

if __name__ == "__main__":
    print("Unesite velicinu tabele (8-16)")
    n = int(input())

    prvi = izaberi_prvog()

    igrac1 = Igrac('X')
    igrac2 = Igrac('O')

    tabla = kreirajTablu(n)
    inicijalno_stanje(tabla, n)
    tabla[1][1][2][1] = 'O'
    tabla[1][1][2][2] = 'X'
    tabla[1][1][1][0] = 'X'
    prikazi_tablu(tabla, n)
    print(igrac1, igrac2)

    potez = unos_poteza()
    odigraj(tabla, n,potez, 1)

    




