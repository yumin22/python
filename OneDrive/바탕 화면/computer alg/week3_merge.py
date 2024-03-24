#merge sort
#Time comlpexity: 0(n log n)
#Space comlexity: 0(n)
#Stable: Yes

def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=[mid:]
        merge(L)
        merge(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]< r[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i< len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        return arr
