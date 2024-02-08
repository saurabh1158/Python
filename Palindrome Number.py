num = int(input ("Enter Number to Check Palindrome Number: "))
temp= num
rev=0

while num >0:
    dig= num%10
    rev = rev * 10  + dig
    num= num//10

if temp== rev:
    print("Number is Palindrome number")

else:
    print("Number is not Palindrome Number ")
