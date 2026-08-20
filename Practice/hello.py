print('''Hellow Neha Let's start coding

"Hellow Neha Let's start coding''')

# a="SHUBHAM NEHA"
# print(a[9::2])

# age=int(input("Enter your age: "))
# print(age)

# print(2**3)
# print(12%2)

# a=12
# b=12

# print(a>b)

# print(12>=12 and 13==13)
# print(11>=12 and 13==13)
# print(12>=12 or 13!=13)
# print(11>=12 or 13!=13)


# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# if n1>n2:
#     print(f"{n1} is greater than {n2}")
# elif n1<n2:
#     print(f"{n2} is greater than {n1}")
# else:
#     print(f"{n1} is equal to {n2}")




# gen=input("Enter your gender (M/F): ")
# if (gen=='M' or gen=='m'):
#     print("Good Morning Sir")
# elif (gen=='F' or gen=='f'):
#     print("Good Morning Ma'am")
# else:
#     print("Good Morning")
    


# n=int(input("Enter a number: "))
# if n%2==0:
#     print(f"{n} is an even number") 
# elif n%2!=0:
#     print(f"{n} is an odd number") 
# else:
#     print("Invalid input")




# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# if age>=18 and age<=120:
#     print(f"Hello,{name} you are valid voter")
# elif age>0 and age<18:
#     print(f"Hello,{name} you are Eligible for voting after 18 years")  

# else:
#     print(f"{name} please enter valid age")




# year=int(input("Enter Year Which you want to know it is Leap or Not :"))
# if year%4==0 or year%400==0 or year%100==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")





# temp=int(input("Enter Temperature : "))
# if temp<0:
#     print(f'{temp} Celcious is Freezing cold ❄')
# elif temp>=0 and temp<=10:
#     print(f'{temp} Celcious is Very cold 🥶')
# elif temp>10 and temp<=20:
#         print(f'{temp} Celcious cold ☁')
# elif temp>20 and temp<=30:
#          print(f'{temp} Celcious is Pleasant 🌤')
# elif temp>30 and temp <=40:
#           print(f'{temp} Celcious is Hot 🌞')
# else:
#     print(f'{temp} Celcious is Very Hot 🔥')




# for i in range(1,21):
#     print(i)


                                        # reverse no
# for i in range(-78,-0):
#     print(i)


# simple table
# for i in range(5,51,5): 
#     print(i)


# user table
# table=int(input("Enter a number for table: "))
# for i in range(table,table*10+1,table):
#     print(i)


# Strings:                           mi mojat bsale
# a="NEHA SHUBHAM"
# for i in range(13):
#     print(a[i])


# a="NEHA SHUBHAM"                   swat mojal
# print(len(a))

# for i in range(len(a)):
#     print(a[i])


# a="NEHA SHUBHAM"              # second method
# print(a)

# for i in a:
#     print(i)



# for i in range(1,21):
#     if i>=15 and i<=18:
#         continue
#     print(i)



# n=int(input("Enter no : "))           print hello from user no
# for i in range(n):
#     print('Hellow World')


# n=int(input("Enter no : "))           #reverse positive
# for i in range(n,1,-1):
#     print(i)



# n=int(input("Enter no : "))           #natural positive
# for i in range(1,n+1):
  
#         print(i)



# n=int(input("Enter no : "))       #table of random no from user
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# n=int(input("Enter no : "))
# for i in range(n)



# n=int(input("Enter no : "))         # to find sum of no
# sum=0
# for i in range(1,n+1):
#     sum =sum+i
# print(f"Sum of {n} is {sum}") 


# # to factorial of no :5*4*3*2*1


# n=int(input("Enter no : "))         
# fact=1
# for i in range(1,n+1):
#     fact =fact *i
# print(f"fact of {n} is {fact}") 



# n=int(input("Enter no : "))         #sum of even no or odd no
# even=0
# odd=0
# for i in range(1,n+1): 
#         if i%2==0:
#             even=even+i
#         else:
#             odd=odd+i

# print(f"\n Sum of even no is : {even} \n Sum of odd no is : {odd}")





# #sum of factors and Factors: take ex 13 = 13 ko khud 13 or 1 => 13 ko divide krta hai. thats the factors 7=1,7 aur jis no ke sirf 2 factor ho vo prime hota hai

# n=int(input("Enter no : "))
# sum=0
# for i in range(1,n+1):
#     if n%i==0:
#         print (f"factors : {i}")
#         sum=sum+i
        
# print(f"sum of that factors is : {sum}")




# accept a no check if it is a perfect no or not.
# a no whose sum of factors=number itself 
# is called perfect no.

# n=int(input("Enter no : "))   
# sum=0      
# for i in range (1,n):
#     if n%i==0:  #and i!=n:            #factor nikalo
#                                       #print (i)
#         sum=sum+i
# if sum==n:                            #check it's perfect or not 
#     print(f"\n{n} is a perfect number")
# else:
#     print(f"\n{n} is not a perfect number")
    
# print(f"sum of factors = number itself is \n {n} = {sum}")
        
        
# n=int(input("enter no : "))
# count=0
# for i in range (1,n+1):
#     if n%i==0:              #factor nikalo
#                             # print (i) factor print ho rhe hai
#         count=count+1
#                             #print(count) factor count ho rhe hai

# if count==2:                #fir sirf 2 factor ho to vo prime no hota hai
#     print(f"{n} : is a prime number")
# else:
#     print(f"{n} : is not a prime number") 
   
        


#Reverse string
# a="SHUBHAM" 

# b=""
# for i in range(len(a)-1,-1,-1):
#         # print(a[i])
#     b=b+a[i]
# print(b)



#string la palindrome krt pn and guess pn krt
# a=input("Enter a string: ")

# b=''
# for i in range(len(a)-1,-1,-1):
#         # print(a[i])
#     b=b+a[i]
# print(b)

# if b==a:
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not a palindrome")       
        


# Given a string (sfvah6576^$%^$), count the number of characters, digits and symbols in it.

# s=input("Enter a string: ")
# char=0
# digit=0
# symbol=0
# for i in s:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         symbol+=1
# print(f" Totalcount of chacters, digits and symbols is: \n Chars = {char} \n Digits = {digit} \n Symbols = {symbol}")





 # to print each digit of a number
# Example: 123456 => 1 2 3 4 5 6
# n=int(input("Enter a number: ")) 
# while n > 0:
#     print(n%10)     # eth te 6 print zale
#     n=n//10



# kisi bhi no ko reverse kro /palindrome krt 
# n=int(input("Enter a number: ")) 
# rev=0
# while n > 0:
#     rev=rev*10+n%10     # eth te 6 print zale
#     n=n//10
# print(rev)




# n=int(input("Enter a number: ")) 
# copy=n
# rev=0
# while n > 0:
#     rev=rev*10+n%10     # eth te 6 print zale
#     n=n//10
# print(rev)

# if copy==rev:           
    
# #n==rev kru shakat ny abtak n pe hi process kiya uski vajah se value 0 ho gyi
#     print(f"{copy} is a palindrome")
# else:   
#     print(f"{copy} is not a palindrome")


import random 
num=random.randint(1,100)
tries=0
while True:
    guess=int(input("Guess a number between 1 and 100: "))
    tries+=1
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {num} in {tries} tries.")
        break



























# import random
# num=random.randint(1,100)
# tries=0

# while True:
#         guess=int(input("Guess no between 1 - 100 : "))
#         tries+=1
#         print("tries")
#         if guess<num:
#          print("go high")
#         elif guess>num:
#             print("go low")
        
#         else:
#             print(f"Congrats!!! Your Guess no is match with {num} in {tries} Tries")
#         break    
    



