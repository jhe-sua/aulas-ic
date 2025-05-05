class Point:
    __match_args__ = ("x","y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(3, 3)

def where_is(p):
    match p:
        case Point(0, 0):
            print("Origin")
        case Point(0, y):
            print(f"Y={y}")
        case Point(x, 0):
            print(f"X={x}")
        case Point(x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
        
where_is(a)