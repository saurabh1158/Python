while True:
    name= input("Enter Customer's Name: ")
    total=0
    while True:
        print("Enter Quantity and Amount: ")
        quantity=float(input("Enter Quantity: "))
        amount= float(input("Entr Amount: "))
        total += quantity *amount
        repeat = input("Do you want to add more products:")
        if repeat == "n":
            break
    print("-"*40)
    print("Name of Customer: ", name)
    print("Total amount payable: ",total)
    print("-"*40)

    repeat1= input("Do You Want to Add New Customer: ")
    if repeat1=="n":
        break

