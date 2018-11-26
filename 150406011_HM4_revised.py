def printName(name,lastname,number):
    print "My name is", name+" "+lastname+ " "+number
name="Selin"
lastname="Kovac"
number="150406011"

printName(name,lastname,number)

import math
def getSlope(SKx1, SKy1, SKx2, SKy2):
    """Returns calculate slope of SK points
Example Usage: getSlope(SKx1, SKy1, SKx2, SKy2)
SKx1: x coordinate of P1
SKy1: y coordinate of P1
SKx2: x coordinate of P2
SKy2: y coordinate of P2
The equation of finding slope is: (SKy2-SKy1)/(SKx2-SKx1) """
    try:
        return (SKy2-SKy1)/(SKx2-SKx1)
    except ZeroDivisionError as err:
        return err                
print
def getYInt(SKx1, SKy1, SKx2, SKy2):
    """Returns calculate slope of SK points
Example Usage: getYInt(SKx1, SKy1, SKx2, SKy2)
SKx1: x coordinate of P1
SKy1: y coordinate of P1
SKx2: x coordinate of P2
SKy2: y coordinate of P2
The equation of finding intercept point is: b = -(s*SKx1) + SKy1"""  
    s = getSlope(SKx1, SKy1, SKx2, SKy2)
  
    if SKy2-SKy1==0:
      b = -(s*SKx1) + SKy1
      return b
    elif SKx2-SKx1==0:
       return None
    elif  -(s*SKx1) + SKy1:
       
       return  -(s*SKx1) + SKy1
         
print getSlope.__doc__
print getYInt.__doc__
print
def myPrint(SKx1,SKy1,SKx2,SKy2,getSlope,getYInt):
    """print function for homework
myPrint(SKx1,SKy1,SKx2,SKy2,getSlope,getYInt)
SKx1: x coordinate of P1
SKy1: y coordinate of P1
SKx2: x coordinate of P2
SKy2: y coordinate of P2
getSlope: Calculates the the slope of the line
getYInt: Finds the intersection of two points
The equation of finding slope is: (SKy2-SKy1)/(SKx2-SKx1)
The equation of finding intersect point is: SKy = -(s*SKx1) + SKy1
The line equation is: SKy=s*SKx+b 
doc: Documentation of myPrint function
"""
    print
    print "SKx1,SKy1:","(",SKx1,",",SKy1,")"
    print "SKx2,SKy2:","(",SKx2,",",SKy2,")"
    print "The slope of the line is:",getSlope(SKx1,SKy1,SKx2,SKy2)
    print "Intercept point:",getYInt(SKx1,SKy1,SKx2,SKy2)
    if SKy2-SKy1==0:
        print "line equation is: SKy=",SKy1
    elif SKx2-SKx1==0:
        print "line equation is: SKx=",SKx1
    else:
        print"The line equation is: SKy=",getSlope(SKx1, SKy1, SKx2, SKy2),"*x","+",getYInt(SKx1, SKy1, SKx2, SKy2) 
print myPrint.__doc__                
                

  
myPrint(2,3,6,7,getSlope,getYInt)
myPrint(2,7,-4,7,getSlope,getYInt)
myPrint(3,1,3,-4,getSlope,getYInt)
