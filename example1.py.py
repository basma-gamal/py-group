n=3
if (n%2 != 0 and 1<=n<=100) or (n%2 == 0 and 6<=n<=2):
    print("Weird")
elif n%2 == 0 and (2<=n<=5 or n>20):
    print("Not Weird")
else:
    print("it isn't in the range")
