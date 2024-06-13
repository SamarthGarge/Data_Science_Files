# Sort the list without using sort function with selection or bubble sort

n = [23,45,87,76,56,89]

print("Original List: ", n)

for i in range(0, len(n)):
    for j in range(i + 1, len(n)):
        if n[i] >= n[j]:

            temp = n[i]
            n[i] = n[j]
            n[j] = temp


print("Sorted List", n)