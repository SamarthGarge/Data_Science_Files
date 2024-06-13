n =("32",43,4,76,4,9,"Shubham",['rahul',['manya'],{"name": "Shambhavi"}])
print(n[7][1][0]) #manya
print(n[7][2]["name"]) #shambhavi

m = [("shanu",21,"iklo"), ("rahul",21,"mkp"),("mahesh",29,"mum")]
print(sorted(m, key = lambda x:x[2]))

print(sorted(m, key = lambda x:x[2], reverse = True)) #to print in decending order


def sums(a,b,c):
    print(a+b+c)


x = int(input("Enter the no. = "))
y = int(input("Enter the no. = "))
z = int(input("Enter the no. = "))

sums(x,y,z)

#Website : RealPython -> Types of functions