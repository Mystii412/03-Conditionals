import math

#break this code down so that no functionality is lost, 
#   but main is no longer than 13 lines (counting "def main()" - not counting comments)
#You should write 5 functions - no function (other than main) 
#   should be no more than 10 lines (counting "def function_name" - not counting comments)
#Two of the fuctions you write should call another function with arguments passed to it
def print_values(area, perim, shape):
    print(f"{shape} area:", {round(area, 3)})
    print(f"{shape} perimeter:", {round(perim, 3)})

def square():
    """Asks for side length and calculates area an perimeter of a square with given proportions"""
    try:
        side = float(input("Side length: "))
    except:
        side = 0.0
    area = side * side
    perim = 4 * side
    print_values(area, perim,'Square')
def rect():
        """Asks for width and height and calculates area and perimeter of a rectangle with given proportions"""
        try:
            w = float(input("Width: "))
            h = float(input("Height: "))
        except:
            w = 0.0
            h = 0.0
        area = w * h
        perim = 2 * w + 2 * h
        print_values(area,perim,'Rectangle')

def circle():
    """Asks for radius and calculates area and circumference of a circle with given proportions"""
    try:
        r = float(input("Radius: "))
    except:
        r = 0.0
    area = math.pi * r * r
    circ = 2 * math.pi * r
    print("Circle area:", round(area, 3))
    print("Circle circumference:", round(circ, 3))
    print("Circle Summary -> A:", round(area, 3), "C:", round(circ, 3))

def tri():
    """Asks for base and height and calculates area of a triangle with given proportions"""
    try:
        base = float(input("Base: "))
        height = float(input("Height: "))
    except:
        base = 0.0
        height = 0.0
    area = 0.5 * base * height
    print("Triangle area:", round(area, 3))
    

def main():
    print("Simple geometry pack (areas/perimeters)")
    mode = input("square/rect/circle/tri: ").strip().lower()
    if mode == "square":
       square()
    elif mode == "rect":
        rect()
    elif mode == "circle":
        circle()
    elif mode == "tri":
        tri()
    else:
        print("Unknown shape.")
        


if __name__ == "__main__":
    main()