# Step 1: Start
# Step 2: Read integer n (number of elements)
# Step 3: Read n elements into array arr
# Step 4: Set max_element = arr[0]
# Step 5: For i = 1 to n − 1, repeat
#     If arr[i] > max_element, then
#       Set max_element = arr[i]
# Step 6: Print the maximum element
# Step 7: Stop

n=int(input("enter the number of element"))
arr= list(map(int,input("enter elents :").split()))

max_element =arr[0]
for i in range(1,n):
    if arr[i]>max_element:
        max_element=arr[i]
print("maximun element",max_element)