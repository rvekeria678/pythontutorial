numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#print(new_list)

#print([n + 1 for n in [1,2,3]])

#print([n*n for n in [1,2,3,5,6,7,8,9,10]])

#print([n*2 for n in range(1,5)])

#names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]

#short_names = [name for name in names if len(name) <= 4]

#large_names = [name.upper() for name in names if len(name) > 4]

#print(large_names)

# Squaring Numbers
print([n*n for n in [1,1,2,3,5,8,13,21,34,55]])

# Filter Even Numbers
print([n for n in range(0,100) if n%2==0])

#