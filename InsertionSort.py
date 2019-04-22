def InsertionSort(data):
    n=len(data)
    for j in range(1,n):
        key=data[j]
        i=j-1
        while i>=0 and data[i]>key:
            data[i+1]=data[i]
            i=i-1
        data[i+1]=key

data=[9,12,234,45,3645,90]        
InsertionSort(data)
print(data)
