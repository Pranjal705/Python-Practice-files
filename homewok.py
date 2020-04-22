n=0
if n>1:
    for i  in range(2,n):
        if n % i == 0:
            print('not Prime')
        break
    else:
        print('prime')
else:
    print('not prime')
