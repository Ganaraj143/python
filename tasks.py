#1)write a function in python that takes two numbers as arguments and returns their sum.
#----------------------------------------------------------------------------------------
def sum(a,b):
     return a+b                                  #1st way 
result_sum=sum(1,3)
print("The sum of two numbers : ",result_sum)

def sum1(a,b):
    print("The sum of two numbers : ",a+b)       #2nd way
sum1(1,3)
    
#2)write a function that returns of square of the given number.
#----------------------------------------------------------------
def square(a):
    return a*a                                     #1st way
result_square=square(5)
print("The square is: ",result_square)

def square1(a):
    print("The square is: ",a*a)                   #2nd way
square1(5)

#3)write a function that accepts a name and prints "Hello <name>!".

def name(name):
    return "Hello "+name                            #1st way
name1=name("pspk")
print(name1)

def name2(name):
    print("hello "+name)                            #2nd way
name2("pspk")

#4) Write a function that takes any number of arguments and returns there sum using *args.

def sumOfNumbers(*num):
    l=len(num)
    sum1=0                                          #1st way
    for i in range(0,l):
        sum1=sum1+num[i]
    return sum1
s=sumOfNumbers(1,2,3,4,5)
print(s)

def sumOfNumbers1(*num):
    sum1=0
    for i in num:                                  #2nd way
        sum1=sum1+i
    print(sum1)
sumOfNumbers1(6,7,8,9,0)

#5) Write a function with deffault arguments that greets a user (default value:"Guest")

def greet(name="Guest"):
    return "Good evening "+name                     #1st Way
greetings=greet("pspk")
print(greetings)

def greet1(name="Guest"):
    print("Good Morning",name)                      #2nd way
greet1()

#6) write a function that takes two numbers and returns both their sum and product.

def sumAndProduct(a,b):
    add=a+b
    pro=a*b
    return "The sum is "+str(add)+".The product is "+str(pro)           #1st way
sumAndPro=sumAndProduct(10,20)
print(sumAndPro)

def sumAndProduct1(a,b):
    print("The sum is "+str(a+b)+".The product is "+str(a*b))           #2nd way
sumAndProduct1(5,5)

#7) write a function that swaps two numbers and returns the swapps values.

def swapnum(a,b):
    print(f'The number is before swapped using third variable.Now a is {a} and b is {b}')
    temp =a
    a=b                                                                                                    #1st way
    b=temp 
    return f'The number is after swapped using third variable.Now a is {a} and b is {b}'
print(swapnum(1,2))

def swapnum1(a,b):
    print(f'The number is before swapped without using third variable.Now a is {a} and b is {b}')
    a,b=b,a                                                                                                #2nd way
    print(f'The number is after swapped without using third variable.Now a is {a} and b is {b}')
swapnum1(3,4)

#8) write a funtion that checks whether a number is even or odd.

def evenOrOdd(num):
    if(num%2==0):
        return "Its a even number."
    else:                                                             #1st way
        return "its a odd number."
print(evenOrOdd(6))

def evenOrOdd1(num):
    if(num%2==0):
        print("Its a even number.")
    else:                                                             #2nd way
        print("Its a odd number")
evenOrOdd1(5)

#9) write a function that takes a list and returns the largest element.

def largestElement(num):
    length=len(num)
    max=num[0]
    for i in range(length):
        if(num[i]>max):                                                 #1st way
            max=num[i]
    return max
number=largestElement([1,2,3,9,23,5,1234,7,98])
print(number)

def largestElement1(num):
    max=num[0]
    for i in num:                                                       #2nd way
        if(max<i):
            max=i
    print("The largest number in list :",max)
largestElement1([23,453,54,234,567,25])

#10) write a function that counts the number of vowels in a given string.

def vowelsCount(str1):
    a="aeiou"
    count=0
    for i in range(len(str1)):
        for j in range(len(a)):
            if(str1[i]==a[j]):
                count+=1
    return count
c=vowelsCount("Temple")
print("The vowels count on given string :",c)

def vowelsCount1(str1):
    a="aeiou"
    c=0
    for i in str1:
        for j in a:
            if(i==j):
                c+=1
    print("The vowels count on given string :",c)
vowelsCount1("pawan kalyan")