def reverse(input):
    reverse_str=''
    for char in input:
        reverse_str=char+reverse_str
    return reverse_str
    
    
x="hello rafik"
reversed=reverse(x)
print("input is:",x)
print("reverse string is :", reversed)
if x==reversed:
    print("string is palindrome")
else:
    print("not palindrome")