# Step 1: Start
# Step 2: Read integer n (number of elements)
# Step 3: Read n integers into array arr
# Step 4: Repeat for i = 0 to n − 2
#     Repeat for j = 0 to n − i − 2
#       If arr[j] > arr[j + 1], then
#       Swap arr[j] and arr[j + 1]
# Step 5: Print the sorted array
# Step 6: Stop



n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)