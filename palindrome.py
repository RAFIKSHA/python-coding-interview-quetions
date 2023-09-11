Num=int(input("Enter a value:"))  
Temp=Num   
Rev=0  
while(Num>0):  
    dig = Num % 10  
    Rev = Rev * 10 + dig  
    Num = Num // 10  
if(Temp==Rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  