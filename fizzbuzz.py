
n = input("Enter in a number: ")
print 'Fizz buzz printing up to ',n
for num in range(1,n+1):
    if num % 3 == 0:
        if num % 5 == 0:
            print 'fizz buzz'
        else: 
            print 'fizz'
    elif num % 5 == 0:
        print 'buzz'
    else: 
        print num

    

