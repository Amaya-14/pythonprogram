# a)

num_list=[-5,9,7,3,2,-4,-6]
print(num_list)
new_list =[x for x in num_list if x >0]
print("The positive numbers are:",new_list)

# b)


n=int(input("Enter the number of elements:"))
num_list=[]
for i in range(n):
    a=int(input("Enter the numbers:"))
    num_list.append(a)
print("Entered list:",num_list)
sqr_lst = [x ** 2 for x in num_list]
print("Squared list:",sqr_lst)

# c)

word = input("Enter a word:")
vowels=[x for x in word.lower() if x in ['a','e','i','o','u']]
print("The vowels in the words are:",vowels)

# d)

w=input("Enter a word:")
ord=[ord(x) for x in  w]
print("The ordinal value is:",ord)