def spiralOrder(matrix):
        """

        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        print("entered the function")
        rows = len(matrix)
        col = len(matrix[0]) if rows > 0 else 0
        res = []

        while(matrix):
                res+=matrix.pop(0)  # pop the first row and add it to the result

                if(matrix and matrix[0]):
                        for i in range(len(matrix)):
                                res.append(matrix[i].pop())
                                

        # for i in range(0, col):  #The first row in the matrix always goes as it is in the spiral order
        #     res.append(matrix[0][i])
        
        # remaining_rows=0
        # # travserse the remaining rows in matrix
        # for i in range(1, rows):
        #       res.append(matrix[i][col-1])
        #       remaining_rows+=1
        #       if ( i == rows-1):
        #             remaining_rows-=1
        #             for j in range(col-2,-1,-1):
        #                 res.append(matrix[i][j])
        # print("res as of now", res)
        # print("remaining rows", remaining_rows)
        # if (remaining_rows > 0):
        #     for i in range(rows-2,remaining_rows, -1):
        #          res.append(matrix[i][0])
        #          if(remaining_rows -1 == i):
        #              for j in range(1, col-1):
        #                  res.append(matrix[i][j])
        #                  return res

res = spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)



