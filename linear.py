arr = list(map(int,input().split()))

n = int(input("Enter the no. you want to search: "))

def fun(arr,n):
  for i in range(len(arr)):
    if arr[i] == n:
        return 1

if fun(arr,n):
   print("found")
else:
   print("not found")