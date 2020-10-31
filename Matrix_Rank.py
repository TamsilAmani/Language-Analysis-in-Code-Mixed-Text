class rankMatrix(object): 
    def __init__(self, Matrix): 
        self.R = len(Matrix) 
        self.C = len(Matrix[0]) 
          
    # Function for exchanging two rows of a matrix 
    def swap(self, Matrix, row1, row2, col): 
        for i in range(col): 
            temp = Matrix[row1][i] 
            Matrix[row1][i] = Matrix[row2][i] 
            Matrix[row2][i] = temp 
              
    # Function to Display a matrix 
    def Display(self, Matrix, row, col): 
        for i in range(row): 
            for j in range(col): 
                print (" " + str(Matrix[i][j])) 
            print ('\n') 
              
    # Find rank of a matrix 
    def rankOfMatrix(self, Matrix): 
        rank = self.C 
        for row in range(0, rank, 1): 
              
         
      
            # Diagonal element is not zero 
            if Matrix[row][row] != 0: 
                for col in range(0, self.R, 1): 
                    if col != row: 
                          
                        # This makes all entries of current  
                        # column as 0 except entry 'mat[row][row]'  
                        multiplier = (Matrix[col][row] /
                                      Matrix[row][row]) 
                        for i in range(rank): 
                            Matrix[col][i] -= (multiplier *
                                               Matrix[row][i]) 
                                                  
            
            else: 
                reduce = True
                  
                # Find the non-zero element  
                # in current column  
                for i in range(row + 1, self.R, 1): 
                      
                    # Swap the row with non-zero  
                    # element with this row. 
                    if Matrix[i][row] != 0: 
                        self.swap(Matrix, row, i, rank) 
                        reduce = False
                        break
                          
                if reduce: 
                      
                    # Reduce number of columns  
                    rank -= 1
                      
                    # copy the last column here 
                    for i in range(0, self.R, 1): 
                        Matrix[i][row] = Matrix[i][rank] 
                          
                # process this row again 
                row -= 1
                  
         
        return (rank) 
  
if __name__ == '__main__': 
    Matrix = [[10, 20, 10], 
              [-20, -30, 10], 
              [30, 50, 0]] 
    RankMatrix = rankMatrix(Matrix) 
    print ("Rank of the Matrix is:",  
           (RankMatrix.rankOfMatrix(Matrix)))
