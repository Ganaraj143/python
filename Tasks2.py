#1)create a list of 10 integers write a program to find the sum,maximum and minimum elements.

randomList=[2,3,4,5,6,-1,7,8,9,10]
sum=0
max=randomList[0]
min=randomList[0]
for i in randomList:                                    #1st way
    sum+=i
    if(max<i):
        max=i
    elif(min>i):
        min=i
print(f'The sum is {sum} , The max number is {max} and The min number is {min}')

def randomList1(l):
    sum=0
    max=l[0]
    min=l[0]
    for i in l:                                         #2nd way
        sum+=i
        if(max<i):
            max=i
        elif(min>i):
            min=i
    return f'The sum is {sum} , The max number is {max} and The min number is {min}'
print(randomList1([23,456,789,2,123,567,349,45,89,2,123]))

#2)Write a program to revere a list without using built-in function.

l=[23,34,54,67,12,909,35]
l1=[]
for i in range(len(l),0,-1):
    l1.append(l[i-1])
print(l1)

#3)write a program to remove duplicates from a given list[1,2,2,3,4,4,5].

list1=[1,2,2,3,4,4,5]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

#4)Write a program to find second largest number in a list.

second_largest=[35, 909, 12, 67, 54, 34, 23]
max=second_largest[0]
sec_max=second_largest[0]
for i in second_largest:
    if sec_max<i:
        if max<i:
            sec_max=max
            max=i
        else:
            sec_max=i
print(sec_max)
        
#5)write a program to separate a even list and odd list from any random list.  

given_list=[35, 909, 12, 67, 54, 34, 23]
even_list=[]
odd_list=[]
for i in given_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(f'The even list is {even_list} and the odd list is {odd_list}')

#6)write a program to count the frequency of each character in a string using a dictionary.

str1="banana"
d={}
for i in str1:
    c=0
    if i not in d:
        for j in str1:
            if i==j:
                c+=1
        d[i]=c
    c=0
print(d)

#7)given a dictionary {"a":1,"b":2,"c":3},add a new key {"d":4}

dictionary={"a":1,"b":2,"c":3}
dictionary["d"]=4
print(dictionary)

#8) write a program to merge two dictionaries.

dict1={"a":1,"b":2,"c":3}
dict2={"d":4,"e":5,"f":6}                               #1st way
dict3=dict1|dict2
print(dict3)

dict5={"a":1,"b":2,"c":3}
dict4={"d":4,"e":5,"f":6}                               #2nd way
dict5.update(dict4)
print(dict5)

#9)write a program to find the key with the maximum value in a dictionary.

max_key={'a': 10, 'b': 25, 'c': 45, 'd': 25}
maxi=max_key["a"]
key=None
for i,j in max_key.items():
    if maxi<j:
        maxi=j
        key=i
print(f'The key with maximum value of {maxi} is {key}')

#10)write a program to check if a key exists in a dictionary.

# key_exists={'a': 10, 'b': 25, 'c': 45, 'd': 25}
# check=input("enter the key :")
# there=False
# for i in key_exists.keys():
#     if check ==i:
#         there=True
#         break
# if(there):
#     print("key is there")
# else:
#     print("key is not there")

#11)unpack the tuple (10,20,30) into three variables and print

unpack_var=(10,20,30)
q,w,e=unpack_var
print(q,w,e)

#12)write a program to swap two numbers using tuples unpacking.

z,x=(10,20)
print(f'z is {z} and x is {x}')
z,x=x,z
print(f'z is {z} and x is {x}')

#13)use a tuple unpacking to assign the first two values of a list to variables and stores the rest in another list.

unpack_list=(1,2,3,4,5)
g,h,*j=unpack_list
print(g,h,j)

#14)unpack a nested tuple ((1,2),(3,4)) into seperate variables.

nested_tuple=((1,2),(3,4))
nes1,nes2=nested_tuple
nes3,nes4=nes1
nes5,nes6=nes2
print(nes3,nes4,nes5,nes6)