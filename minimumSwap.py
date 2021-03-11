def minimumSwaps(arr):
    a = dict(enumerate(arr,1))
    print(a)
    b = {v:k for k,v in a.items()}
    print(b)
    count = 0
    for i in a:
        print("i:" + str(i))
        x = a[i]
        print("x:" + str(x))
        if x!=i:
            y = b[i]
            a[y] = x
            b[x] = y
            count+=1
            print("a:")
            print(a)
            print("b:")
            print(b)
    return count
        
n = int(input())
arr = list(map(int,input().split()))
print(minimumSwaps(arr))