def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i+1
    return -1
arr=[10,30,40,50,60]
target=40
result=linear_search(arr,target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
    