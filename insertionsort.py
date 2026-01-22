# Alogorith insertion_sort(A,n)
# for i<-1 to n-1 do
#     key <-A[i]
#     j <-i - 1
#     while j>=0 andA[j]> key do
#      A[j+1] <-A[j]
#      j <- j-1
#     end while
#     A[j+1] <- Key
# end for
#  return A

def insertion_sort(arr):
 n =len(arr)

 for i in range (1,n):
   key=arr[i]
   j=i-1

   while j>=0 and arr[j]>key:
      arr[j+1] =arr[j]
      j-=1
   arr[j+1]=key
 return arr
arr=[64,55,22,11,12]
print(insertion_sort(arr))
