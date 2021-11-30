def find_sum(Array, sum):
    Array.sort()
    arr_size = len(Array)
    for i in range(0, arr_size):
        first = 0
        last = arr_size - 1
        while first < last:
            love_sum = Array[first] + Array[i] + Array[last]
            if love_sum == sum and first != i:
                print(Array[i], Array[first], Array[last])
                return True
            elif love_sum < sum:
                first += 1
            else:
                last -= 1
    print(False)
    return False


Array = [1, 5, 6, 7, 8, 9]
find_sum(Array, 12)
