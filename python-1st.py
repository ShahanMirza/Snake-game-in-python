# f=100
# print (f)
# def some():
#     global f
#     print(f)
#     f="changing global value"
#     #print (f )

# some()
# print (f)
# del f
# f="deleted"
# print(f)

# tup1=('Shahan','Mirza','BS CS ','UOG')
# tup2=(0,1,2,3,4,5,6,7)
# (firstName,lastName,Degree,institute)=tup1
# print(tup1[1])
# print(tup2[0:3])
# print(firstName)
# print(lastName)
# print(Degree)
# print(institute)

# a=(5,6)
# b=(6,4)
# if(a>b):print("a is greater")
# else: print("b is greater")

# a={'x':100, 'y':200,'z':300}
# b=list(a.items())
# print(b)
# x = ("a", "b","c", "d", "e")
# print(x[2:4])
# if 5 > 2 :
#  print("5 is greater than 2")
#  print("is indentation works?") 
# x="tin","tun","ton"
# a,b,c=x

# print(a)
# print(b)
# print(c)

# x={"behvr":'lovely',"kuch be":'fantastic',"yeh chz":"awesome"}
# y=range(6)
# print(y, type(y))
# def myfunc():
    
#     print("python is "+str(x))

# myfunc()
# print(type(x))

# a='''     lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua'''
# print(a[-10:-1], a.upper(), a.strip(), a.replace('e','a'), a.split(','))
# x ="Hello, World!"
# if 'K' not in x:
#  print( 'not present ')
# else:
#  print('present') 

# quantity=3
# itemno=2
# price=67.7
# myorder="i want {1} pieces of item {0} for {2} dollars"
# print(myorder.format(quantity,itemno,price))
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# class myclass():
#  def myfunc(self):
#     return 0

# x=myclass()
# print(bool(x.myfunc()))

# testList=["apple","banana","cherry","mango","pineapple","kiwi","malon"]
# newList=[x for x in testList if "ap" in x ]
# print(newList)
# for x in testList:
#     if "apple" in x:
#         newList.append(x)
# print(newList)
# print(testList)
# for i in range(len(testList)):
#     if testList[i]=="mango":
#         testList[i]="lolipop"
# print(testList)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# thisJson={
#     "brand":"ford",
#     "model":"Mustang",
#     "year":2021
# }
# thisJson['color']='black'
# print(thisJson)
# x=thisJson.values()
# print(x)

# x=lambda a,b,c:a*b*c
# print(x(6,2,3))

# def myfunc(n):
#     return lambda a: a+n

# mydouble=myfunc(2)
# print(mydouble(11))

#divisible by 7 but are not a multiple of 5

# l=[]
# for i in range(20,320):
#     if(i%7==0) and (i%5!=0):
#         l.append(str(i))
# print (','.join(l))

#factorial


# def factor(count):
#  if count==0:
#     return 1
#  return count*factor(count-1)
# count=int(input())
# print (factor(count))

#program to generate a dictionary that contains (i, i*i)
# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print (d)

#comma-separated numbers from console and generate a list and a tuple which contains every number
# value=input()
# l=value.split(",)
# t=tuple(l)
# print(l)
# print(t)

# class InputOutString(object):
#     def __init__(self):
#         self.s=""
#     def getString(self):
#         self.s=input()
#     def printString(self):
#         print self.s.upper()
# strObj=InputOutString()
# strObj.getString()
# strObj.printString()   
# def solve(numheads,numlegs):
#     ns='No solutions!'
#     for i in range(numheads+1):
#         j=numheads-i
#         if 2*i+4*j==numlegs:
#             return i,j
#     return ns,ns

# numheads=35
# numlegs=94
# solutions=solve(numheads,numlegs)
# print (solutions )
#string reverse
# s=input()
# s=s[::-1]
# print(s)
# import math
# c=50
# h=30
# value=[]
# items=[x for x in input().split(",")]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(",".join(value))

# input_str=input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist=[[0 for col in range(colNum)]for row in range(rowNum)]

# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]=row*col
# print(multilist)
#sorting 
# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items))

#uper case
# lines=[]
# while True:
#     s=input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break
# for sentence in lines:
#     print(sentence)

#sorting
# s= input()
# words=[word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))

# list=[]
# items=[x for x in input().split(',')]
# for p in items:
#     intp=int(p,2)
#     if not intp%5:
#         list.append(p)
# print(','.join(list))

# values=[]
# for i in range(1000,9001):
#     s=str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))

#calculate the number of letters and digits

# consoleinput=input()
# d={"DIGITS":0,"LETTERS":0}
# for c in consoleinput:
#     if c.isdigit():
#         d['DIGITS']+=1
#     elif c.isalpha():
#         d['LETTERS']+=1
#     else:
#         break
# print("LETTERS",d["LETTERS"])
# print("DIGITS",d["DIGITS"])

# value=input()
# d={"UPERCARSE":0,"LOWERCASE":0}
# for c in value:
#     if c.isupper():
#         d["UPERCARSE"]+=1
#     elif c.islower():
#         d["LOWERCASE"]+=1
# print("UPERCARSE",d["UPERCARSE"])
# print("LOWERCASE",d["LOWERCASE"])


# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print (n1+n2+n3+n4)

# value=input()
# numbers=[x for x in value.split(',') if int(x)%2!=0]
# print(",".join(numbers))