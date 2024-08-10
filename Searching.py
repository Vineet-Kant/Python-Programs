#Binary Search
pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid+1
    return False

list=[1,2,5,8,12,16,18,30,45,50]
n=12
if search(list,n):
    print("Found at", pos+1)
else:
    print("Not Found")

#Linear Search
def serch(lis,n1):
    i=0
    for n1 in lis:
        if lis[i] == n1:
            return True
        else:
            return False
lis=[54,26,48,66,15,6,78,98,74]
n1=98
if serch(lis,n1):
    print("Found",)
else:
    print("Not Found")
