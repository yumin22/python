#insertion sort 삽입 정렬
#Time complexity: 0(n^2)
#Space complexity: 0(1)
#In-place: Yes

#ex) [10,20,5,4]
#key=20 정렬이 안되어있다고 가정
#j=0 (j: 정렬이 되어있는 인덱스 값)
#arr[j+1]=arr[0+1]=arr[1] <=key

#ex2) [10,20,5,4]
#i=2
#key=5
#j=i-1=1 ->0 -> -1

#ex3) [5,10,20,4]
#key=4
#j=2=>i >=1 ->0 ->-1 (-1값이 되면 while문 탈출)

#ex4) while문을 빠져나오는 다른 경우 [4,5,10,20,16]
#key=16
#j=3 -> 2
#arr[j+1]-> arr[3]=key


range(1,5) #[1,2,3,4]

def insertion(arr):
    for i in range(1,len(arr)):  #1번부터 시작, 제일 왼쪽 값은 볼 필요가 없다. 
        key=arr[i]  #Key: 정렬이 안된 부분의 첫 번째 원소
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

x=[5,2,10,4]
print(insertion(x))