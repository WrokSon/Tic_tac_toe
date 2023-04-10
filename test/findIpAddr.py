def detectWinner(grid):
        for i in range(3):
            # Vérifie l'alignement horizontal
            if grid[i][0] == grid[i][1] == grid[i][2] != 0:
                return True
            # Vérifie l'alignement vertical
            if grid[0][i] == grid[1][i] == grid[2][i] != 0:
                return True
        # Vérifie l'alignement diagonal de gauche à droite
        if grid[0][0] == grid[1][1] == grid[2][2] != 0:
            return True
        # Vérifie l'alignement diagonal de droite à gauche
        if grid[0][2] == grid[1][1] == grid[2][0] != 0:
            return True
        return False

matrice = [[0,0,1],
           [0,1,0],
           [1,0,1]]

print(detectWinner(matrice))