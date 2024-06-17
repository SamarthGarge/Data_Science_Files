num=[24,67,84,46,58]

for i in range (0,len(num)):
    for j in range(i+1,len(num)):
        if(num[i]>=num[j]):
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)


        
    
 