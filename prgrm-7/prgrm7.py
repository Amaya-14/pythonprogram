a = input("Enter a string: ")

first = a[0]
b = first

for i in range(1, len(a)):
    if a[i] == first:
        b += "$"
    else:
        b += a[i]

print(b)
