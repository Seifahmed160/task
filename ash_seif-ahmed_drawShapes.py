import math

def printAndSort(shapes=[]):
    print("The List Before Sorting: \n------------------------")
    print(shapes)
    shapes.sort(key=lambda i:i[1])
    print("The List After Sorting: \n-----------------------")
    print(shapes)



def constructShape(n,shapePrint,lengthPrint):
    shapes = []
    for i in range(n):
        shapetuple =[]
        for j in range(1):
            shapeName = input("Enter The Name of "+shapePrint+" "+str(i+1)+": ")
            shapetuple.append(shapeName)
            shapeLength = float(input("Enter The "+lengthPrint+" of "+shapePrint+" "+str(i+1)+": "))
            shapetuple.append(shapeLength)
        shapes.append(tuple(shapetuple))
    return shapes


def drawSquare(n,shapes=[]):
    for i in range(n):
        len=shapes[i][1]
        print("Square "+str(i+1)+" :\n")

        for i in range(int(len)):
            print ('*' * int(len))
            
                
def drawTriangle(n,shapes=[]):
    for i in range(n):
        len=shapes[i][1]
        print("Triangle "+str(i+1)+" :\n")

        for row in range (int(len)):
            for col in range (row + 1):
                print('*', end='')
            print()

    
def drawPyramid(n,shapes=[]):
    for i in range(n):
        len=shapes[i][1]
        print("Pyramid "+str(i+1)+" :\n")

        k = 0
        for i in range(1, int(len)+1):
            for space in range(1, (int(len)-i)+1):
                print(end="  ")
        
            while k!=(2*i-1):
                print("* ", end="")
                k += 1

            k = 0
            print()

def drawCircle(n,shapes=[]):
    for i in range(n):
        len=shapes[i][1]
        radius=int(len/2)
        print("Circle "+str(i+1)+" :\n")

        for i in range((2 * radius)+1):
  
            # for vertical movement
            for j in range((2 * radius)+1):
                
                dist = math.sqrt((i - radius) * (i - radius) +
                    (j - radius) * (j - radius))
    
                # dist should be in the
                # range (radius - 0.5)
                # and (radius + 0.5) to print stars(*)
                if (dist > radius - 0.5 and dist < radius + 0.5):
                    print("*",end="")
                else:
                    print(" ",end="")     
        
            print()





while True:
    key= input("Please Enter A Key of shape That You Want To Create:\n---------------------------------------------------------\n1-Circle\n2-square\n3-right triangle\n4-pyramid\n")
    shapes=[]
    if key == "1":
        n = int(input("Enter number of circles you want to create: "))
        shapePrint="Circle"
        lengthPrint="Diameter"
        shapes=constructShape(n,shapePrint,lengthPrint)
        printAndSort(shapes)
        drawCircle(n,shapes)
        

    elif key == "2":
        n = int(input("Enter number of Squares you want to create: "))
        shapePrint="Square"
        lengthPrint="Side Length"
        shapes=constructShape(n,shapePrint,lengthPrint)
        printAndSort(shapes)
        drawSquare(n,shapes)

    elif key == "3":
        n = int(input("Enter number of Triangles you want to create: "))
        shapePrint="Right Triangle"
        lengthPrint="Height"
        shapes=constructShape(n,shapePrint,lengthPrint)
        printAndSort(shapes)
        drawTriangle(n,shapes)


    elif key == "4":
        n = int(input("Enter number of Pyramids you want to create: "))
        shapePrint="Pyramid"
        lengthPrint="Height"
        shapes=constructShape(n,shapePrint,lengthPrint)
        printAndSort(shapes)
        drawPyramid(n,shapes)


    cond=input("Do You Want To Create Another List of Shapes? (Y/N)")
    if cond=="N":
        print("GoodBye!")
        break


