def swapPositions(list, pos1, pos2):       
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
  
def countSwaps(a):
    count = 0
    n = len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j + 1]:
                a = swapPositions(a, j, j + 1)
                count += 1
    return 'Array is sorted in ' + str(count) + ' swaps.\nFirst Element: ' + str(a[0]) + '\nLast Element: ' + str(a[n-1])

a = [3,2,1,4]
print(countSwaps(a))


