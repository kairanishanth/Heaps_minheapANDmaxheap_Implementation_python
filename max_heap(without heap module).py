#max heap: 
def max_heapify(arr,i):
    # l=left(i)
    # r=right(i)
    l=2*i+1
    r=2*i+2
    if l<len(arr) and arr[l]<arr[i]:
        largest=l
    else:
        largest=i
    if r<len(arr) and arr[r]<arr[i]:
        largest=r
    if largest != i:
        arr[i],arr[largest]=arr[largest],arr[i]
        max_heapify(arr,i)
# def left(i):
#     return 2*i+1
# def right(i):
#     return 2*i+2
def build_max_heap(arr):
    n=((len(arr)//2)-1)
    for i in range(n,-1,-1):
        max_heapify(arr,i)
arr=[11,22,3,5,4,6,9,7,8]
build_max_heap(arr)
print(arr)
