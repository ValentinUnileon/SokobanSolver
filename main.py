
#Sokoban solver

#   Leyenda 
#   # -> pared
#   $ -> caja
#   @ -> personaje
#   . -> objetivo
#   * -> personaje sobre objetivo
#   ! -> caja sobre objetivo

#ToDo corregir error de personaje sobre objetivo

def main():


    # Lista para almacenar las líneas del rompecabezas
    puzzle_lines = []

    # Abrir el archivo - Leer las lineas del archivo y traspasarlo a una matriz doble
    with open('puzzle.txt', 'r') as file:

        for line in file:
            row=[]
            alcanzado=0

            for char in line:
                
                if(char=='#'):
                    alcanzado=1

                if(char==' ' and alcanzado==0):
                    row.append('X')
                else:
                    row.append(char)
              
            puzzle_lines.append(row)

    #Finalizada transcripcion a matriz
            
    #VAMOS A SUPONER QUE EL TABLERO SIEMPRE ES VALIDO

    for row in puzzle_lines:
        print(row)

    print("\n")

    """""
    #PROBATINAS
        
    matrizSoluciones = getSolution(puzzle_lines)

    for row in matrizSoluciones:
        print(row)

    print("El puzle esta resuelto: ",isSolved(puzzle_lines, matrizSoluciones))
    x, y = getCharPositionXY(puzzle_lines)
    print("la posicion incial es", x, " ", y)
    print ("la anchura en ese punto es", len(puzzle_lines[y+1]))

    #print("El siguiente movimiento es valido: ", isMovementValid(x, y, puzzle_lines))
    
    print("Tiene dos paredes la caja cuando se mueva? o se va a mover a una pared la caja", isBoxWithTwoWallsANDNotMovingToWall(x, y-1, puzzle_lines))
    print("Es un movimiento invalido al moverse a un pared?", isNearWallWithOutGoal(x+1, y, puzzle_lines))

    #FIN PROBATINAS

    
    #xP, yP = getCharPositionXY(puzzle_lines)
    puzzle_lines=updatePuzzle(3, 4, 4, 4, puzzle_lines)

    for row in puzzle_lines:
        print(row)

    """
    #updatePuzzle(xP, yP, )

    #Llamamos al metodo para resolver el tablero
        #falta metodo para obtener la posicion inicial del personaje
        #falta metodo para obtener la solucion final
    steps = []
    x, y = getCharPositionXY(puzzle_lines)
    if solve_Sokoban_backtracking(x, y, puzzle_lines, steps, getSolution(puzzle_lines)):
        print("SE ha encontrado solucion")
        #imprimir steps (los devuelve el metodo de backtracking)
    else:
        print("NO se ha encontrado la solucion")
    


#FUNCIONES FUERA DEL MAIN

    
def solve_Sokoban_backtracking(x, y, puzzle, steps, solution):
    print("hola")

    if isSolved(puzzle, solution) == True:
        #Se ha resuelto el tablero
        return True, steps
        
    if isMovementValid(x, y, puzzle)==True:
        
        #Ahora hay que plantear todos los movimentos posibles del personaje
        #Arriba - abajo - derecha - izquierda

        if solve_Sokoban_backtracking(x+1, y, updatePuzzle(x, y, x+1, y, puzzle), steps):
            return True, steps + ["right"]
        
        if solve_Sokoban_backtracking(x-1, y, updatePuzzle(x, y, puzzle), steps):
            return True, steps + ["left"]

        if solve_Sokoban_backtracking(x, y+1, updatePuzzle(x, y, puzzle), steps):
            return True, steps + ["up"]
        
        if solve_Sokoban_backtracking(x, y-1, updatePuzzle(x, y, puzzle), steps):
            return True, steps + ["down"]
        
        
    
        return False, []

    return False


def getCharPositionXY(puzzle):
    
    for i, row in enumerate(puzzle):
        for j, element in enumerate(row):
            if element in {"@", "*"}:
                return j, i


def getSolution(puzzle):
    
    #En este metodo disponemos del puzzle original y queremos obtener una matriz doble con las posiciones de los '.' del puzzle

    solutionArray=[]
    rowSolution=[]

    for j, row in enumerate(puzzle):
        for i, char in enumerate(row):
            if char==".":
                rowSolution.append((i, j))
                solutionArray.append(rowSolution)
                rowSolution = []

    return solutionArray


def isSolved(puzzle, solution):
    
    for box in solution:
        for coordinates in box:
            x, y=coordinates
            if puzzle[y][x] != "$":
                return False
        
    return True

    

def isMovementValid(x, y, puzzle): #x y es la posicion a la que se va a mover el personaje

    #En este metodo tenemos que comprobar si la posicion en la que se encontraria el personaje segund las coordenadas x y es valida
    #para ello hay que tener en cuenta que las cajas que hay en el mapa pueden moverse, y que no deben hacerlo en determinadas posiciones
    #Tambien hay casos especiales en los que la posicion parece ser validda en un principio pero realmente no lo es porque deja al programa sin solucion
        #Uno de estos caso puede ser que la caja se quede pegada a una pared y que no tenga ninguna caja en la vertical o en la horizontal
        #otra situacoin a contemplar puede ser que una caja tenga dos paredes en su
    
    #Para empezar tenemos que tener en cuenta que la posicion actual se encuentra en puzzle y es valida seguro
    #La nueva tenemos que construirla con x e y 

    #xP, yP = getCharPositionXY(puzzle)
    if puzzle[y][x] == "#":
        return False
    
    #comprobar si cuando muevo el personaje este mueve una caja y tiene dos paredes alrededor y no se encuentra en un "." 

    if isBoxWithTwoWallsANDNotMovingToWall(x, y, puzzle) : #tambien se comprueba si se va a mover hacia una pared Y si no va a mover una caja da FALSE
        return False  #NO es valido                        #*****hay que comprobar cuando la caja ya esta pegada a la pared
    
    if isNearWallWithOutGoal(x, y, puzzle):
        return False #NO es valido

  # if isNearWallWithOutGoal(): #metodo que, si la caja se mueve hacia un pared, comprueba si tiene en la vertical o en la horizontal un objetivo, en ese caso el mov sera valido, sino no
        #return False
  # if la caja esta pegada contra la pared y quieres empujarla -- ya esta
        #return False
  # infrontOfOtherBox() if va a empujar a una caja y tiene otra en frente
        #return False


    return True


def isNearWallWithOutGoal(x, y, puzzle): #no hace falta comprobar si se va a mover hacia una pared

    if puzzle[y][x] == "$": #Entonces va a mover una caja

        if puzzle[y + 1][x] in {"@", "*"} and puzzle[y - 1][x] != ".":

            if puzzle[y-2][x] in {"#", "!"} and puzzle[y-2][x+1] in {"#", "!"} and puzzle[y-2][x-1] in {"#", "!"}:
                #si tiene 3 cajas alrededor hay que comprobar si hay un . en su vertical porque si no es un movimiento invalido
                #ahora hay que comprobar si la horizontal tiene algun .
                for row in puzzle[y-1]:
                    if row == ".":
                        return False #Puede moverse a esa posicion

                return True   
            
        if puzzle[y - 1][x] in {"@", "*"} and puzzle[y + 1][x] != ".":
            
            if puzzle[y+2][x] in {"#", "!"} and puzzle[y+2][x+1] in {"#", "!"} and puzzle[y+2][x-1] in {"#", "!"}:

                for row in puzzle[y+1]:
                    if row == ".":
                        return False # Puede moverse a esa posicion
                    
                return True
            
        if puzzle[y][x+1] in {"@", "*"} and puzzle[y][x-1] != ".":
            
            if puzzle[y][x-2] in {"#", "!"} and puzzle[y+1][x-2] in {"#", "!"} and puzzle[y-1][x-2] in {"#", "!"}:

                for i in range(len(puzzle)):
                    cell = puzzle[i][x-1]
                    if cell == ".":
                        return False  # Puede moverse a esa posición

                return True
            
        if puzzle[y][x-1] in {"@", "*"} and puzzle[y][x+1] != ".":

            if puzzle[y][x+2] in {"#", "!"} and puzzle[y+1][x+2] in {"#", "!"} and puzzle[y-1][x+2] in {"#", "!"}:  #falta implementar fullLineWallX()

                for i in range(len(puzzle)):
                    cell = puzzle[i][x+1]
                    if cell == ".":
                        return False  # Puede moverse a esa posición

                return True                


    return False



def fullLineWallX(x, y, puzzle):
    #metodo utilizado para saber si la pared a la que se va a acercar la caja esta llena de paredes por debajo y por arriba, en tal caso el mov es invalido
    for row in puzzle[y+2]:
        if row != "#":
            return False #No esta full de paredes por lo tanto el mov es valido

def fullLineWallY(x, y, puzzle):
    print("nose")

def isBoxWithTwoWallsANDNotMovingToWall(x, y, puzzle):

    # Detectamos si el personaje está al lado de una caja
    if puzzle[y][x] == "$":  # Entonces va a mover una caja
        counter = 0
        # Buscamos hacia dónde va a mover la caja

        if puzzle[y + 1][x] in {"@", "*"} and puzzle[y - 1][x] != ".":
            # Está a la derecha por lo tanto va a moverte a la izquierda
            if puzzle[y - 1][x] in {"#", "!"}:
                return True  # No se puede mover a una pared
            else:
                if puzzle[y - 2][x] in {"#", "!"}:
                    counter += 1
                if puzzle[y - 1][x + 1] in {"#", "!"}:
                    counter += 1
                if puzzle[y - 1][x - 1] in {"#", "!"}:
                    counter += 1

        if puzzle[y - 1][x] in {"@", "*"} and puzzle[y + 1][x] != ".":
            # Está a la izquierda por lo tanto va a moverte a la derecha
            if puzzle[y + 1][x] in {"#", "!"}:
                return True  # No se puede mover a una pared - NO VALIDO
            else:
                # Se comprueba las tres cajas de alrededor
                if puzzle[y + 2][x] in {"#", "!"}:
                    counter += 1
                if puzzle[y + 1][x - 1] in {"#", "!"}:
                    counter += 1
                if puzzle[y + 1][x + 1] in {"#", "!"}:
                    counter += 1

        if puzzle[y][x + 1] in {"@", "*"} and puzzle[y][x - 1] != ".":
            # Está abajo por lo tanto te mueve para arriba
            if puzzle[y][x - 1] in {"#", "!"}:
                print("hola jefe", x, y, puzzle[y][x - 1] in {"!", "#"})
                return True  # No puede moverse a una pared 
            else:
                if puzzle[y][x - 2] in {"#", "!"}:
                    counter += 1
                if puzzle[y + 1][x - 1] in {"#", "!"}:
                    counter += 1
                if puzzle[y - 1][x - 1] in {"#", "!"}:
                    counter += 1

        if puzzle[y][x - 1]in {"@", "*"} and puzzle[y][x + 1] != ".":
            # Está por arriba entonces lo mueve para abajo
            if puzzle[y][x + 1] in {"#", "!"}:
                return True  # No se puede mover a una pared - lo damos por malo
            else:
                if puzzle[y][x + 2] in {"#", "!"}:
                    counter += 1
                if puzzle[y + 1][x + 1] in {"#", "!"}:
                    counter += 1
                if puzzle[y - 1][x + 1] in {"#", "!"}:
                    counter += 1

        if counter >= 2:
            return True  # Si está entre dos o más cajas

    return False  # Valido




def updatePuzzle(xP, yP, x, y, puzzle):  # Cuando una caja se pone encima de un objetivo se tiene que cambiar al caracter '!'
    #tenemos la posicion actual del personaje y la posicion a la que se va a mover

    ####### se necesitan modificar muchas cosas porque hay que tener en cuenta que cuando el personaje
        #   esta encima de una caja se convierte en un *
    
    char=puzzle[y][x] #dependiendo del caracter al que se vaya a mover el personaje
    

    if char == "$":  # Entonces va a mover una caja

        puzzle[yP][xP] = " "
        puzzle[x][y]="@"

        
        # Calcula la dirección de movimiento de la caja
        dx = x - xP
        dy = y - yP
        # Mueve la caja a la nueva posición
        puzzle[y + dy][x + dx] = "$"
        # Si la caja está sobre un objetivo, cambia su representación a '!'
        if puzzle[y + dy][x + dx] == ".":
            puzzle[y + dy][x + dx] = "!"

        
    elif char == ".":  # Si el personaje estaba encima de un objetivo debería de cambiar de forma a *
        
        #comprobar si el personaje estaba en forma de *

        if puzzle[yP][xP] == "*":
            puzzle[yP][xP] = "."
        else:
            puzzle[yP][xP] = " "
        
        puzzle[x][y]="*"


    elif char==" ":
        #movimiento normal

        if puzzle[yP][xP] == "*":
            puzzle[yP][xP] = "."
        else:
            puzzle[yP][xP] = " "

        puzzle[x][y]="@"



    return puzzle



   








    









if __name__ == "__main__":
    main()


