def hourglassSum(arr):
    maxTrioByRows = len(arr[0]) - 2
    maxTrioByCols = len(arr) - 2
    lst = [[] for i in range(maxTrioByRows * maxTrioByCols)]

    c = 0
    idx = 0
    for i in range(0,maxTrioByCols):
        for j in range(0, maxTrioByRows):
            lst[c].append(arr[i][j])
            lst[c].append(arr[i][j+1])
            lst[c].append(arr[i][j+2])
            # lst[c].append(str(i) + str(j))
            # lst[c].append(str(i) + str(j+1))
            # lst[c].append(str(i) + str(j+2))

            lst[c].append(arr[i+1][j+1])
            # lst[c].append(str(i+1) + str(j+1))
            
            lst[c].append(arr[i+2][j])
            lst[c].append(arr[i+2][j+1])
            lst[c].append(arr[i+2][j+2])
            # lst[c].append(str(i+2) + str(j))
            # lst[c].append(str(i+2) + str(j+1))
            # lst[c].append(str(i+2) + str(j+2))
            # print(str(arr[i][j]), end='')
            c+=1
        # print()

    print('len(lst): ' + str(len(lst)))
    results = []
    print('len(results): ' + str(len(results)))
    for x in lst:
        print(x, sep=',', end='') 
        print('-> ' + str(sum(x)), end='\n')
        results.append(sum(x))
    
    print(results, sep=',')
    print('max ' + str(max(results)))
    return  max(results)

row1  = [1 ,1 ,1 ,0 ,0 ,0]
row2  = [0 ,1 ,0 ,0 ,0 ,0]
row3  = [1 ,1 ,1 ,0 ,0 ,0]
row4  = [0 ,9 ,2 ,-4 ,-4 ,0]
row5  = [0 ,0 ,0 ,-2 ,0 ,0]
row6  = [0 ,0 ,-1 ,-2 ,-4 ,0]

# row1 = [1, 1, 1, 0, 0, 0]
# row2 = [0, 1, 0, 0, 0, 0]
# row3 = [1, 1, 1, 0, 0, 0]
# row4 = [0, 0, 2, 4, 4, 0]
# row5 = [0, 0, 0, 2, 0, 0]
# row6 = [0, 0, 1, 2, 4, 0]
arr = [row1, row2, row3, row4, row5, row6]

hourglassSum(arr)