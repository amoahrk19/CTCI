

def binarysearch(arr, n):
    print("searching through list {}".format(arr))
    pivot = int(len(arr) / 2)
    if n == arr[pivot]:
        return pivot
    elif n < arr[pivot]:
        return binarysearch(arr[:pivot], n)
    elif n > arr[pivot]:
        return binarysearch(arr[pivot:], n)


array_list = list(map(int, input("Input list").split()))
num = int(input("input num"))

ind = binarysearch(array_list, num)
print(ind)