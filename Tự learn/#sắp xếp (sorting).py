# Sắp xếp nổi bọt (Bubble Sort)
def bubble_sort(arr):
    n=len(arr)
    for i in range (n):
        for j in range (0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]   
    return arr
# Example usage
arr=[64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)
sorted_arr=bubble_sort(arr)
print("Sorted array:", sorted_arr)
# Sắp xếp chọn (Selection Sort)
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i], arr[min_idx]=arr[min_idx], arr[i]
    return arr
b=[[1,2],[2,43],[2,4]]
x=b[:2]
print(x)
x[1].append(10)
print(x)
