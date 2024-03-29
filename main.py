
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

    for row in puzzle_lines:
        print(row)

    #Llamamos al metodo para resolver el tablero
        #falta metodo para obtener la posicion inicial del personaje
        #falta metodo para obtener la solucion final
    steps = []
    if solve_Sokoban_backtracking():
        print("Se ha encontrado solucion")

    


#FUNCIONES FUERA DEL MAIN

    
def solve_Sokoban_backtracking(self, x, y, puzzle, steps, solution):
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



def isSolved(self, puzzle, solution):
    print("solution")

def isMovementValid(self, x, y, puzzle):
    print("nose")

def updatePuzzle(self, x, y, puzzle):
    print("nose")
    #devuelve puzle con las posiciones movidas








    









if __name__ == "__main__":
    main()


