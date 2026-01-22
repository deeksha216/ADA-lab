# Step 1: Start
# Step 2: Read elements into array arr
# Step 3: If the size of array > 1, then
#     a. Find mid = length(arr) // 2
#     b. Divide the array into two halves:
#       left = arr[0 … mid − 1]
#       right = arr[mid … end]
#     c. Recursively apply Merge Sort on left
#     d. Recursively apply Merge Sort on right
#     e. Merge the two sorted halves into arr
# Step 4: Print the sorted array
# Step 5: Stop

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = list(map(int, input("Enter elements: ").split()))
merge_sort(arr)
print("Sorted array:", arr)
 