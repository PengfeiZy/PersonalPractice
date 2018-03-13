# Time: 2017/12/15 EIGHT QUEEN Auther: PENGFEI XIONG
# This project is used to solve Eight Queen Problem. It's an exercise of recurssion.
# Procedure of problem solving:
# 1. We start with row, and judge whether it's dangerous in its column, and diagonal lines. 
# 2. We assume our main function is correct, then we recusively apply it with different rows until we finish
#    all the rows.

# not_dangerous function is used to judge whether it's dangerous, chess is our chess board, it's a 8*8 matrix.
def not_dangerous(row, column, chess): 
    # When all flags equal to 1, then we can say it's not dangerous:
    flag1, flag2, flag3, flag4, flag5 = 1, 1, 1, 1, 1 

    # Check its column:
    for k in range(8):
        if chess[k][column] != 0:
            flag1 = 0

    # Check its left top diagonal:
    i, j = row, column
    while i >= 0 and j >= 0:
        if chess[i][j] != 0:
            flag2 = 0
        i-=1
        j-=1
    
    # Check its left bottom diagonal:
    i, j = row, column
    while i < 8 and j >= 0:
        if chess[i][j] != 0:
            flag3 = 0
        i+=1
        j-=1
    # Check its right top diagonal:
    i, j = row, column
    while i >= 0 and j < 8:
        if chess[i][j] != 0:
            flag4 = 0
        i-=1
        j+=1
    # Check its right bottom diagonal:
    i, j = row, column
    while i < 8 and j < 8:
        if chess[i][j] != 0:
            flag5 = 0
        i+=1
        j+=1
    if flag1 and flag2 and flag3 and flag4 and flag5:
        return True
    else:
        return False

# This if main recurssive function that we used to place queen in our chess board:
count = 0
def eightqueen(row,column,chess):
    # 我们需要打印每种情况，所以在递归函数内部将chess赋值给新的chess2，从而使得我们在函数内部改变chess2的数值
    # 能够对应该递归函数自己相应的情况，而不是改变整个棋盘
    chess2 = chess
    global count
    if row == 2:
        for each in chess:
            print(each)
        count+=1
        print(count,'\n\n')
    # 注意，在不符合初始条件的时候，我们要判断当前位置是否dangerous，如果不是，我们就放置棋子；反之，我们判断下一行
    else:
        for i in range(column):
            if not_dangerous(row,i,chess):    #这里的chess是函数外部传入进来的函数，而我们要改变的是chess2
                for j in range(8):
                    chess2[row][j] = 0
                chess2[row][i] = 1
                eightqueen(row+1,column,chess2)

chess = [[0 for i in range(8)] for j in range(8)]

eightqueen(0,8,chess)