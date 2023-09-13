# cook your dish here
flag=0
t=int(input())
for i in range(t):
    n1=int(input())
    lst=[]
    n2=input()
    lst.append(n2)
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            flag=1
        else:
            flag=0
    if flag==1:
        print("list in the form of ascendeing order")
    else:
        print("in desc")   
