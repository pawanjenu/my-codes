def heapify(arr,n,i):
    lar = i
    left = 2*i + 1
    right = 2*i + 2
   

    if(left < n and  arr[i] < arr[left]):   # for decreasing jus mk it arr[i] > arr[left]
        lar = left

    if(right < n and  arr[i] < arr[right]): #      jus do as abv "'''''''"
            lar = right

    if lar != i:
        arr[i] ,arr[lar] = arr[lar] ,arr[i]

        heapify(arr,n,lar)  #recursive

def hsort(arr):
    n = len(arr)

    for i in range(n,-1,-1):
        heapify(arr,n,i)

    #swaping for creating max heap
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)



arr = [12,2,5,1,8,7,0]
hsort(arr)
n= len(arr)
print ("Sorted array is")
for i in range(n):
    print (arr[i])

        


