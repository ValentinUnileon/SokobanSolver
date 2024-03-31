
#Sokoban solver

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

    #PROBATINAS
        
    matrizSoluciones = getSolution(puzzle_lines)

    for row in matrizSoluciones:
        print(row)

    print("El puzle esta resuelto: ",isSolved(puzzle_lines, matrizSoluciones))
    x, y = getCharPositionXY(puzzle_lines)
    print("la posicion incial es", x, " ", y)

    #print("El siguiente movimiento es valido: ", isMovementValid(x, y, puzzle_lines))
    
    print("Tiene dos paredes la caja cuando se mueva? o se va a mover a una pared la caja", isBoxWithTwoWallsANDNotMovingToWall(x+1, y, puzzle_lines))

    #FIN PROBATINAS

    #Llamamos al metodo para resolver el tablero
        #falta metodo para obtener la posicion inicial del personaje
        #falta metodo para obtener la solucion final
    #steps = []
    #if solve_Sokoban_backtracking():
    #    print("Se ha encontrado solucion")
        #imprimir steps (los devuelve el metodo de backtracking)
    #else:
    #    print("nose")
    


#FUNCIONES FUERA DEL MAIN

    
def solve_Sokoban_backtracking(x, y, puzzle, steps, solution):
    print("hola")

    if isSolved(puzzle, solution) == True:
        #Se ha resuelto el tablero
        return True, steps
        
    if isMovementValid(x, y, puzzle)==True:
        
        #Ahora hay que plantear todos los movimentos posibles del personaje
        #Arriba - abajo - derecha - izquierda
        if solve_Sokoban_backtracking(x+1, y, updatePuzzle(x, y, puzzle), steps):
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
            if element == "@":
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

    

def isMovementValid(x, y, puzzle):

    #En este metodo tenemos que comprobar si la posicion en la que se encontraria el personaje segund las coordenadas x y es valida
    #para ello hay que tener en cuenta que las cajas que hay en el mapa pueden moverse, y que no deben hacerlo en determinadas posiciones
    #Tambien hay casos especiales en los que la posicion parece ser validda en un principio pero realmente no lo es porque deja al programa sin solucion
        #Uno de estos caso puede ser que la caja se quede pegada a una pared y que no tenga ninguna caja en la vertical o en la horizontal
        #otra situacoin a contemplar puede ser que una caja tenga dos paredes en su
    
    #Para empezar tenemos que tener en cuenta que la posicion actual se encuentra en puzzle y es valida seguro
    #La nueva tenemos que construirla con x e y 

    xP, yP = getCharPositionXY(puzzle)
    if puzzle[y][x] == "#":
        return False
    
    #comprobar si cuando muevo el personaje este mueve una caja y tiene dos paredes alrededor y no se encuentra en un "." 

    if isBoxWithTwoWallsANDNotMovingToWall(x, y, puzzle) : #tambien se comprueba si se va a mover hacia una pared Y si no va a mover una caja da FALSE
        return False  #NO es valido                        #*****hay que comprobar cuando la caja ya esta pegada a la pared
    
  # if isNearWallWithOutGoal():
        #return False
  # if la caja esta pegada contra la pared y quieres empujarla
        #return False
  # if va a empujar a una caja y tiene otra en frente
        #return False


    return True
    

def isBoxWithTwoWallsANDNotMovingToWall(x, y, puzzle):
    counter = 0

    # Detectamos si el personaje está al lado de una caja
    if puzzle[y][x] == "$":  # Entonces va a mover una caja

        # Buscamos hacia dónde va a mover la caja

        if puzzle[y + 1][x] == "@" and puzzle[y - 1][x] != ".":
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

        if puzzle[y - 1][x] == "@" and puzzle[y + 1][x] != ".":
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

        if puzzle[y][x + 1] == "@" and puzzle[y][x - 1] != ".":
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

        if puzzle[y][x - 1] == "@" and puzzle[y][x + 1] != ".":
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




def updatePuzzle(x, y, puzzle):  #cuando una caja se pone encima de un objetivo se tiene que cambiar al caracter !
    print("nose")
    #devuelve puzle con las posiciones movidas








    









if __name__ == "__main__":
    main()


