f = int(input("Enter any number"))

for n in range(1, 10):
    print(n)
    if n == f:
        print('number found')
        break
else:
    print('number not found')

print('program end !')