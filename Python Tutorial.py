4
#   #Opeartors in Python
#   1 Arithmetic Operators
print(2**3)                     # 8
print(5%2)                      # 1
print(7//3)                     # 2

num1 = 10
num2 = 20
print("num1+num =",num1+num2)
print("num1-num =",num1-num2)
print("num1*num =",num1*num2)
print("num1/num =",num1/num2)

#   2 Assignment Operators += /= //= %=
num3 = num1+num2
num3 += num2                    # num3 = num3 + num2

#   3 Comparison Operators < > == !=
print("is num3 > num2", num3 > num2)    # True
print("is num3 = num2", num3 == num2)   # False

#   4 Logical Operators and or not
print(2 and 3)                          # 3
print(2 or 3)                           # 2
print(not 2)                            # False

#   5 Bitwise Operators | & ^ >> <<
print(5|7)                              # or 101 or 111 = 111
print(5&7)                              # and 101 and 111 = 101
print(5^7)                              # xor 101 xor 111 = 010  a xor b = (!a and b) or (a and !b)
print(3>>2)                             # 0   0011 -> 0000
print(3<<2)                             # 12  0011 -> 1100

#   6 Identity Operators is is not

#   7 Membership Operators in not in
x = [1,2,3,4,5]
print(3 in x)                           # True
print(3 not in x)                       # False


#   #Data type in Python
#   1 immutable (Numbers,Strings,Tuples)
#   1.1 Numbers integer,float,complex

#   1.2 Strings
strings = "hello world"
strings = 'hello world'
#   1.2.1 Sequence Operations
string1 = "Python"
string2 = "Tutorial"
print(string1+string2)              # PythonTutorial
print(string1*2)                    # PythonPython
print(string1[2:3])                 # t
print(string1[:2])                  # Py
print(string1[:-2])                 # Pyth
print(string1[2:])                  # thon
print(string1[-2:])                 # on
#   1.2.2 Type Speecific Method
str1 = "Edureka"
print(str1.find('ur'))               # 2
print(str1.replace('ur','eeee'))     # Edeeeeeka
print(str1.split('u'))               # ['Ed','reda']
print(str1.count('u'))               # 1
print(str1.upper())                  # EDUREKA
print(max(str1))                     # u
print(min(str1))                     # E
print(str1.isalpha())                # True

#   1.3 Tuples can't be changed
#   1.3.1 Sequence Operations
my_tup = ('Neel','qiao','Raj','Sandeep')
print(my_tup + ('Dong',))           # ('Neel', 'qiao', 'Raj', 'Sandeep', 'Dong')
                                    # if I write print(my_tup + ('Dong',))   wrong!!!!
print(my_tup * 3)                   # three time print my_tup
print(my_tup[1:5])                  # ('qiao','Raj','Sandeep')

#   2 mutable (Lists,Dictionaries,Sets)
#   2.1 Lists
my_list = ['Edureka',32,7.8]
list1 = ['1','b',2.5]
list2 = ['d']
print(list1+list2)
print(list1*2)
print(list1[1:3])
print(list1[1:])
print(list1[1::])
print(list1[:2])
print(list1[2])

print(list1.append('d'))
print(list1.extend(['d','e']))
print(list1.insert(2,'v'))
print(list1.pop())
print(list1)

array = [1,3,2,4,5,6,7,8,9]
print(array[1:3])           # [3, 2]
print(array[1:])            # [3, 2, 4, 5, 6, 7, 8, 9]
print(array[:3])            # [1, 3, 2]
print(array[3:-3])          # [4, 5, 6]
print(array[1::])           # [3, 2, 4, 5, 6, 7, 8, 9]
print(array[::2])           # [1, 2, 5, 7, 9]

#   2.2 Dictionaries
# empty Dict
myDict = {}
# Dict with integer keys
myDict = {1:'apple',2:'ball'}
# Dict with mixed keys
myDict = {'name':'john',1:[2,4,3]}
# From Sequence having each item as a pair
myDict = dict([(1,'apple'),(2,'ball')])

myDict = {1:'apple',2:'ball','name':'qiaodong'}
print(myDict[1])                                # apple
print(myDict.keys())                            # [1, 2, 'name']
print(myDict.values())                          # ['apple', 'ball', 'qiaodong']
print(len(myDict))                              # 3
print(myDict.items())                           # [(1, 'apple'), (2, 'ball'), ('name', 'qiaodong')]
print(myDict.get('name'))                       # qiaodong
print(myDict.update({4:'this is update'}))      #
print(myDict.pop('name'))                       # qiaodong

#   2.3 Sets
my_set = {1,2,3,4}

myS1 = {1,2,'c'}
myS2 = {1,'b','c'}
print(myS1|myS2)                                # set([1, 2, 'b', 'c'])
print(myS1&myS2)                                # set([1, 'c'])
print(myS1-myS2)                                # set([2])


#   #Flow Control in Python
#  if   if..else..  if..elif..else  for while   break   continue

marks = 40
if(marks > 80):
    print("A")
elif(marks > 60 and marks <= 80):
    print("B")
elif(marks > 40 and marks <= 60):
    print("c")
else:
    print("d")

num=int(input('Enter the value of n='))
if(num <= 0):
    print("Enter a valid value")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
print(sum)

# for iterator name in iterating sequence:
# range(1,5) means from 1 to 5 not included 5
# range(1,5,2) means from 1 to 5 but the step is 2 => 1,3
# range(5) means from 0 to 5 not included 5
for quant in range(99,0,-1):
    if quant > 1 :
        print(quant,"Bottles of beer on the wall,", quant,"bottles of beer")
        if quant > 2:
            suffix = str(quant) + "bottles of beer on the wall"
        else :
            suffix = "1 bottle of beer on the wall"
    elif quant == 1 :
        print("1 bottle of beer on the wall,1 bottle of beer")
        suffix = "No more beer on the wall"
    print("take one down",suffix)
    print("---")

count = 0
while True:
    print(count)
    count += 1
    if(count > 10):
        break


#   #Functions in Python
#  built-in functions / user defined functions

def fib(n):
    a = 0
    b = 1
    for x in range(n):
        a = b
        b = a+b
        print(a,'\n')
    return b

num = int(input("Enter the value of n="))
print(fib(num))


#   #File Handing in Python
# open(filename,mode)    /    read()    /    write()    /    close()

fobj = open("D:\\1.txt",'w+')
print("File content before writing:")
print(fobj.read())
fobj.write('\nPython is fun')
print("File content after writing:")
fobj.seek(0)
print(fobj.read())
fobj.close()
