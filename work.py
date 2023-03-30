

n=int(input("enter a prime number"))

for i in range(2,n):
    if n%i==0:
        print("not a prime number")
        chk=False
        break
    else:
        chk=True

if chk:
    print("prime number")


