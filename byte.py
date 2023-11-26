
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
            # Oznake za redove
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


if __name__ == "__main__":
    print("Unesite velicinu tabele (8-16)")
    n = int(input())

    tabla = kreirajTablu(n)
    inicijalno_stanje(tabla, n)
    prikazi_tablu(tabla, n)



