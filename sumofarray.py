def addition(arr1,arr2):

    sum=[]
    if len(arr1) != len(arr2):
        return None  # Return None if the arrays have different lengths

    size=len(arr1)
    sum = [0] * size
    for i in range(size):
        sum[i]=(arr1[i] + arr2[i])
        #we can also used the sum.append(arr1[i] + arr2[i]) that time no need to set size of sum
    # for i in range(len(arr1)-1):
    #     for j in range(len(arr2)-1):
    #         sum[j]= arr1[i]+arr2[j]
    return sum    

arr1=[10,20,30]

arr2=[10,20,40]
sum=addition(arr1,arr2)
print(sum)