def minimumBribes(arr):
    if len(arr) < 2:
        print("Too chaotic")

    count = 0
    expectedleft = 1
    expectedMiddle = 2
    expectedRight = 3

    for i in range(len(arr)):

        if arr[i] == expectedleft:
            expectedleft = expectedMiddle
            expectedMiddle = expectedRight
            expectedRight += 1
        elif arr[i] == expectedMiddle:
            count += 1
            expectedMiddle = expectedRight
            expectedRight += 1
        elif arr[i] == expectedRight:
            count += 2
            expectedRight += 1
        else:
            print("Too chaotic")
            return
    print(str(count))
    return


queue = [2, 3, 4, 1, 5]
minimumBribes(queue)
