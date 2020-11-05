
#ex1
def Xnor(bool1,bool2):
    """function that calculate the Xnor logic gate"""
    if(bool1==True and bool2==True):
        return True
    elif(bool1==False and bool2==False):
        return True
    elif((bool1==True and bool2==False)or(bool1==False and bool2==True)):
        return False

#ex2
def CountDigit(intnum):
    count=0
    while intnum >0:
        intnum //= 10
        count += 1
    return count

def digitnum(number,locationum):
    if(locationum>CountDigit(number)):
        return None
    for i in range(locationum-1):
        number//=10
    return number%10


def Digit(number5):
    """functin to calculate number according follwing roles
        the function gets a number until 5 digits
        number digits    action
        1               same number
        2               sum of two digits
        3               sum of the first and last digits
        4               sum of the two middle digits
        5               show the middle digit"""
    num=int(number5)
    counter = CountDigit(number5)
    print("the number of digits:", counter)
    if(counter==1):
        print("The number is:",number5)
    elif(counter==2):
        firstdig=digitnum(number5,1)
        secdig=digitnum(number5,2)
        print("sum of the first and last digits",firstdig+secdig)
    elif(counter==3):
        firstdig=digitnum(number5,1)
        lastdig=digitnum(number5,3)
        print("The sum of the first and last digits",firstdig+lastdig)
    elif(counter==4):
        midL=digitnum(number5,3)
        midR=digitnum(number5,2)
        print("The sum of the two middle digits",midL+midR)
    elif(counter==5):
        middle=digitnum(number5,3)
        print("The middle digit is:", middle)
    elif(counter>5):
        print(("Error!"))
    return None

#ex3

def IsEven(number1):
    if(number1%2==0):
        return True
    else:
        return False




def GoodOrder(intnumber):
    """boolean function gets a integer number
    return True when all the digis are even or odd"
    """
    sizenum=CountDigit(intnumber)
    first_digit=digitnum(intnumber, 1)
    Even_flag=IsEven(first_digit)
    while (sizenum > 0):
        next_digit=digitnum(intnumber,sizenum)
        if(IsEven(next_digit)==Even_flag):
            pass
        else:
            return False
        sizenum -= 1
    return True

# assert GoodOrder(1573)is True
print("good order?",GoodOrder(1573))


#4 need to fix!!
"""print a piramid of number from one to the choose number """

def UpAndDown(start):
    if(start==1):
        print(start,end='')
    else:
        print(start,end='')
        UpAndDown(start-1)
        print(start, end='')

print(UpAndDown(7))

def PrintSpace(times):
    print('_'*times,end='')

def Figure(edge):
    #if(edge>0 and type(edge)==int):
    for i in range(1,edge):
        PrintSpace(edge-i)
        for j in range(1,2):
            print(i,end='')
            for n in range(0,edge,2):
                print()

#Figure(4)

#6
def IsPrimary(primenum,check=2):
    """cheking prime number
    prime number= True
    not prime number = False"""
    if(primenum==check):
        return True
    else:
        if(primenum%check==0):
            return False
        else:
            return IsPrimary(primenum,check+1)


print("is prime?",IsPrimary(103))





#8

'''
A function that receives the coordinates of Pascal's triangle (x,y)
and returns the value in the same coordinates.
'''


def Pascal(x, y):
    if x == y or y == 0:
        result = 1
    else:
        result = Pascal(x - 1, y - 1) + Pascal(x - 1, y)
    return result


# print("PascalTriangle (5,2) =>{0}".format(Pascal(5, 2)))
# print("PascalTriangle (4,2) =>{0}".format(Pascal(4, 2)))
# print("PascalTriangle (3,1) =>{0}".format(Pascal(3, 1)))