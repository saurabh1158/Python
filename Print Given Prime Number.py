start=int(input("Enter Satrting Number:"))
end=int(input("Enter End Number:"))
print("Prime Number Between", start,"and",end)

for num in range(start ,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)