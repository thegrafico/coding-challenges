ar = [
    [1,2,3], 
    [4,6,8], 
    [10,20,30]
    ]

#vertical normalr
for row in range( len(ar) ):
    for col in range( len(ar[0]) ):
        print(ar[row][col], end=',')

#Vertical reversed
for row in range( len(ar) ):
    for col in range( len(ar) - 1, -1, -1  ):
        print(ar[row][col], end=',')