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
    while(not proveri_smer(smer)):
        print("Pogresno unet potez, unesi ponovo:")
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

    polje = tabla[red][kolona]
    stek = []

    if(postoji_u_steku(tabla, red, kolona,poz)):
        nadjen = False 
        for i in range(r,-1,-1):
            for j in range(3):
                e = c_copy % 3
                if(polje[i][e] != '.'):
                    stek.append(polje[i][e])
                else:
                    nadjen = True
                    break
                c_copy = c_copy + 1
                if e == 2:
                    break
            if nadjen:
                break          
        vrh = vrhSteka(red, kolona)
        if potez[3] == 'GL':
            igraj(tabla,n, stek, red - 1, kolona - 1, vrh)
        elif potez[3] == 'GD':
            igraj(tabla, n, stek, red - 1, kolona + 1, vrh)
        elif potez[3] == 'DL':
            igraj(tabla, n, stek, red + 1, kolona - 1, vrh)
        elif potez[3] == 'DD':
            igraj(tabla, n, stek, red + 1, kolona + 1, vrh)

def vrhSteka(red, kolona):
    c_copy = 0
    poz = 0
    for i in range(2,-1,-1):
            for j in range(3):
                e = c_copy % 3

                if(tabla[red][kolona][i][e] == '.'):
                    break
                else:
                    poz = poz + 1
                c_copy = c_copy + 1
                if e == 2:
                    break
            if(tabla[red][kolona][i][e] == '.'):
                    break
    return poz
def igraj(tabla, n, stek, red, kolona, vrh1):
    vrh = vrhSteka(red, kolona)
    po = pozicija(vrh)
    if postoji_polje(n,red, kolona) and (len(stek) + vrh) < 8 and (vrh + len(stek)) > vrh1: 
        c_copy = po[1]
        k = 0
        for i in range(po[0],-1,-1):
            for j in range(3):
                e = c_copy % 3

                tabla[red][kolona][i][e] = stek[k]
                
                k = k + 1
                if k > len(stek) - 1:
                    break
                c_copy = c_copy + 1
                if e == 2:
                    break
            if k > len(stek) - 1:
                    break
    else:
        print("Vise od 8 figura u rezultujucem steku")
def prazna_susedna(tabla, red, kolona):
    if not postoje_figure(tabla, red - 1, kolona - 1) and not postoje_figure(tabla, red - 1, kolona + 1) and not postoje_figure(tabla, red + 1, kolona - 1) and not postoje_figure(tabla, red + 1, kolona + 1):
        return True
    return False
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
    tabla[1][1][2][1] = 'X'
    tabla[1][1][2][2] = 'O'
    tabla[1][1][1][0] = 'X'
    tabla[0][0][2][0] = 'X'
    tabla[0][0][2][1] = 'O'
    tabla[0][0][2][2] = 'X'
    tabla[0][0][1][0] = 'O'
    prikazi_tablu(tabla, n)
    print(igrac1, igrac2)

    potez = unos_poteza()
    odigraj(tabla, n,potez, 1)
    prikazi_tablu(tabla, n)

    




