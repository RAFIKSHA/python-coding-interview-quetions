def primenumber(num):
    if num<0:
        return print("number is not prime number")
    elif num%2!=0:
        return print("number is  prime")
    else :
        return print("number  not is prime")       

num=int(input("enter the prime number"))

primenumber(num)