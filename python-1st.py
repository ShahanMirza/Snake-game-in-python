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

def myfunc(n):
    return lambda a: a+n

mydouble=myfunc(2)
print(mydouble(11))