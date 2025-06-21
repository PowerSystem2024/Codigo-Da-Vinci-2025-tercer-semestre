class KnightTour {
    constructor(size = 8) {
        this.size = size;
        this.board = Array.from({ length: size }, () => Array(size).fill(-1));
        this.moves = [
            [2, 1], [1, 2], [-1, 2], [-2, 1],
            [-2, -1], [-1, -2], [1, -2], [2, -1]
        ];
        this.solutionFound = false;
    }

    isSafe(x, y) {
        return x >= 0 && y >= 0 && x < this.size && y < this.size && this.board[x][y] === -1;
    }

    solve() { 
        this.board[0][0] = 0;
        
        if (!this.solveUtil(0, 0, 1)) {
            console.log("No existe solución");
            return false;
        }
        
        this.printSolution();
        return true;
    }

    solveUtil(x, y, moveCount) {
        if (moveCount === this.size * this.size) {
            this.solutionFound = true;
            return true;
        }

        for (const [dx, dy] of this.moves) {
            const nextX = x + dx;
            const nextY = y + dy;

            if (this.isSafe(nextX, nextY)) {
                this.board[nextX][nextY] = moveCount;
                
                if (this.solveUtil(nextX, nextY, moveCount + 1)) {
                    return true;
                }
                 
                this.board[nextX][nextY] = -1;
            }
        }

        return false;
    }

    printSolution() {
        console.log("Solución encontrada:");
        for (let i = 0; i < this.size; i++) {
            let row = "";
            for (let j = 0; j < this.size; j++) {
                row += this.board[i][j].toString().padStart(3, ' ') + " ";
            }
            console.log(row);
        }
    }
}


const knightTour = new KnightTour(8);
console.time("Tiempo de ejecución");
knightTour.solve();
console.timeEnd("Tiempo de ejecución");
