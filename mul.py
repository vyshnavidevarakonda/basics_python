print("******* multiplication table ********")
while True:
    n = int(input("enter a number:"))
    if(n==0):
        print("Thank you!!!")
        break
    else:
        for i in range(1,11):
            ans = n*i
            print(f"{n} * {i}={ans}")