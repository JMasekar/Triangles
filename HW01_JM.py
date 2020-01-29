"""
@author- Jigar Masekar

HW01 Testing Triangles: Code for function classify_triangle()

"""


def classify_triangle(a, b, c):

    if a > 500 or b > 500 or c > 500:
        return "Error"

    if a <= 0 or b <= 0 or c <= 0:
        return "Error"

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return "Error"

    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return "It is not a Triangle"

    if a == b and b == c and c == a:
        return "Equilateral Triangle"

    elif ((a * a) + (b * b)) == (c * c) or ((c * c) + (b * b)) == (a * a) or ((c * c) + (a * a)) == (b * b):
        return "Right Triangle"

    elif (a != b) and (b != c) and (a != c):
        return "Scalene Triangle"
    else:
        return "Isosceles Triangle"

