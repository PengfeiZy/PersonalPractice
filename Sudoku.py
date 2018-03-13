# Time: 2017/11/20
# Object: Write a class to solve the Sudoku problem
# Divide the problem:
    # 1. The most import property of Sudoku is its number can never be repeat in row, column and distric
    #    that it locates on. So in our class, the first function we need to create is to check whether 
    #    the number that we plug in is repeat.
    # 2. As soon as we create 1, we need to create another function that can help us to find the
    #    next blank space, and return its index of row and column. Or if we have reached the very last
    #    space of the Sudoku, it will return us -1, -1. For this part, we will find its column in specific
    #    row. If there is no 0 in this row, we will go to anther row. 
    # 3. Now we have finished 2 preparation functions, we can go to main function. In this function, we will 
    #    start with a specific row and column, if it's 0, we fill the number and then go to its next index 
    #    with funciton 2. If it's next index can be filled with a reasonable number under condition of function1, 
    #    we fill it, and recursively call function3. Otherwise, we set Sudoku[x][y] = 0, and re-fill it until we    
    #    get final answer.


class Sudoku(object):

    # Sudoku matrix:
    # [[8,0,0,0,0,0,0,0,0],
    #  [0,0,3,6,0,0,0,0,0],
    #  [0,7,0,0,9,0,2,0,0],
    #  [0,5,0,0,0,7,0,0,0],
    #  [0,0,0,8,4,5,7,0,0],
    #  [0,0,0,1,0,0,0,3,0],
    #  [0,0,1,0,0,0,0,6,8],
    #  [0,0,8,5,0,0,0,1,0],
    #  [0,9,0,0,0,0,4,0,0]]

    def __init__(self, sudoku_matrix):
        assert type(sudoku_matrix) == list, 'sudoku_matrix must be a 9*9 matrix'
        self.value = sudoku_matrix

    # This function is used to check if the"value" that we will insert in is conflict with is row, column or district.
    def check_repeat(self, x, y, value):
        # check its row value.
        for column in self.value[x]:
            if column == value:
                return False
        # check its column value.
        for row in self.value:
            if row[y] == value:
                return False
        # check its value in its district.
        x_num, y_num = x//3*3, y//3*3
        for i in range(x_num, x_num+3):
            for j in range(y_num, y_num+3):
                if self.value[i][j] == value:
                    return False
        return True

    # This function is used to reach to next blank(0) number of sudoku. If it is zero, return False. 
    # Otherwise, we return the row number and column number of next blank value. We foucus both on next
    # row number and next column number.

    # Python function will return the very first value that it calculates.
    def next(self, x, y):
        # Next column number. We need to check all the value that behind it because we do not know where the loop
        # can break. As long as it breaks, the for loop will stop and return row number and column number. 
        for i in range(y+1, 9):
            if self.value[x][i] == 0:
                return x, i
        # If every blank in this row is full, we will renturn next row number and column number.
        for i in range(x+1, 9):
            for j in range(0, 9):
                if self.value[i][j] == 0:
                    return i, j 
        return -1, -1    

    # This is our main function used to solve the suduko game. We need some recursion here. If we find next value
    # impair the check_repeat funciton we will go back last layout and re-fill that number.
    def try_solve(self, x, y):
        if self.value[x][y] == 0:
            for i in range(1,10):
                if self.check_repeat(x,y,i):
                    self.value[x][y] = i
                    next_x, next_y = self.next(x,y)
                    if next_x == -1:
                        return True
                    else:
                        # When self.tre_solve function has repeat value because self.check_repeat return a False,
                        # this recursion will go back to last layout to re-fill the blank.
                        end = self.try_solve(next_x,next_y)
                        # When this condition is impaired, it will go back to for loop, and re-fill the blank with
                        # another i so this recursion can continue.
                        if not end:
                            self.value[x][y] = 0 
                        else:
                            return True

    # This is the last function that we use to call try_solve function to solve our sudoku.
    @property
    def start_to_solve(self):
        # Start with the first number, if it's blank, we start right here; otherwise we start with 
        # next function.
        if self.value[0][0] == 0:
            self.try_solve(0,0)
        else:
            x,y = self.next(0,0)
            self.try_solve(x,y)
        for i in self.value:
            print(i)

matrix = [[8,0,0,0,0,0,0,0,0],
 [0,0,3,6,0,0,0,0,0],
 [0,7,0,0,9,0,2,0,0],
 [0,5,0,0,0,7,0,0,0],
 [0,0,0,8,4,5,7,0,0],
 [0,0,0,1,0,0,0,3,0],
 [0,0,1,0,0,0,0,6,8],
 [0,0,8,5,0,0,0,1,0],
 [0,9,0,0,0,0,4,0,0]]

s = Sudoku(matrix)
s.start_to_solve
