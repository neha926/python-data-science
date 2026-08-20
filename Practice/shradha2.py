# str="neha"     # Strings are immutable in python
# print(str[0])
# str[0]="y"
# print(str[0])


# s=['neha', 89.8, 56, 'bmt']
# print(s[0])
# s[3]='shubh'
# print(s[0])


# insert element at any index include remaining elements
# list=[3,2,0,1]
# list.insert(0,4)
# print(list)


# reverse the list
# list=[3,2,0,1]
# list.reverse()
# print(list)



# sort the list in ascnding order
# list=[3,2,0,1]
# list.sort()
# print(list)



# sort the list in descending order
# list=[9,3,0,1,7]
# list.sort(reverse=True)
# print(list)



# add element at the end of the list
# list=[9,3,0,1,7]
# list.append(5)
# print(list)



# a=input("enter movie name 1 : ")
# b=input("enter movie name 2 : ")
# c=input("enter movie name 3 : ")
# list=[]
# list.append(f'{a},{b},{c}')
# print(list)




# palindrome for list 

# list=["NEHA",1,"NEHA"]
# copy=list.copy()
# print(copy)

# copy.reverse()
# print(copy)

# if list==copy:
#     print("list is palindrome")
#     print(list)
# else:
#     print("list is not palindrome")
#     print(list)



# tup=("C","D","A","A","B","B","A")
# tup[0]="B"
#print(tup)  # This will raise an error because tuples are immutable



# list=["C","D","A","A","B","B","A"]
# list.sort()
# print(list)


# list=[1,9,5,3,0,2] # #Mutable data type
# print(list)
# list[1]=7
# print(list)



# name="neha"       #not executed cause strings are immutable
# print(name)

# name[0]="s"
# print(name)


# import calendar
# month=calendar.month_name[4]
# print(month)  # This will print the name of the month corresponding to the number 4, which is "April"



# dict={
#     "table" : ["a piece of furniture","list of facts and figures"],
#     "cat":"a small animal"
# }

# print(dict)



# sub={"python","java","c++","python","javascript","java","python","java","c++","c"}

# print(len(sub)) 


sub={}                #dict
math=int(input("enter math mark : "))
science=int(input("enter sci mark : "))
history=int(input("enter his mark : "))
total=math+science+history
per=(total/300)*100 
# print(total)
# print(per)
sub.update({"math":math,"science":science,"history":history,"total":total,"per":per})
print(f"{sub}")
    


# collection=set()

# set={(9,9.0,10,10.0)}
# print(set)
