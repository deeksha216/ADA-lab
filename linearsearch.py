# Step 1: Start
# Step 2: Read integer n (number of elements)
# Step 3: Read n elements into array arr
# Step 4: Read element key to be searched
# Step 5: Set found = false
# Step 6: For i = 0 to n − 1, repeat
#     If arr[i] == key, then
#       Print position (i + 1)
#       Set found = true
#       Stop the loop
# Step 7: If found == false, print “Element not found”
# Step 8: Stop

n=int(input("enter the number of element"))
arr= list(map(int,input("enter the element:").split()))
key= int(input("enter the element to search :"))


found=False
for i in range(n):
    if arr[i]==key:
        print("element the position",i+1)
        found=True
        break

if not found:
     print("element not found") 
