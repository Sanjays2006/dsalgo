arr = [77,4,32,45,7,6454,66]

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if(arr[j] > arr[j+1]):
            arr[j+1],arr[j] = arr[j],arr[j+1]
print(arr)