lst=[]
n=int(input("enter the number of elements in list: "))
print("INPUT: List=")
for i in range(0,n):
    ele=int(input())

    lst.append(ele)

print("ÖUTPUT: ")

for i in lst:
    if i>0:
        print(i)
