#min heap:
def min_heapify(arr,i):
    # l = left(i)
    # r = right(i)
    l=2*i+1 
    r=2*i+2
    if l < len(arr) and arr[l] < arr[i]:
        smallest = l
    else:
        smallest = i
    if r < len(arr) and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest)

# def left(i):
#     return 2 * i + 1

# def right(i):
#     return 2 * i + 2

def build_min_heap(arr):
    n = int((len(arr)//2)-1)
    for i in range(n, -1, -1):
        min_heapify(arr,i)

arr = [3,9,2,1,4,5]
build_min_heap(arr)
print(arr)
