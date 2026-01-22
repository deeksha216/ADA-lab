# Step 1: Start
# Step 2: Read sorted array arr
# Step 3: Read element key to be searched
# Step 4: Set low = 0 and high = length(arr) − 1
# Step 5: While low ≤ high, repeat
#     a. Compute mid = (low + high) // 2
#     b. If arr[mid] == key,
#       Print position and Stop
#     c. Else if arr[mid] < key,
#       Set low = mid + 1
#     d. Else
#       Set high = mid − 1
# Step 6: If element not found, print “Element not found”
# Step 7: Stop

arr = list(map(int, input("Enter sorted elements: ").split()))
key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position", mid + 1)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
