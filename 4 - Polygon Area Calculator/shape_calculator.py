class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture_str = ""
            for i in range(self.height):
                if i < self.height:
                    picture_str = picture_str + ("*" * self.width) + "\n"
                else:
                    picture_str = picture_str + ("*" * self.width)

            return picture_str

    def get_amount_inside(self, shape):
        if shape.width > self.width or shape.height > self.height:
            return 0
        else:
            return int(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side
        super().__init__(self.width, self.height)

    def __str__(self):
        return "Square(side=" + str(int(self.side)) + ")"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.side = side

    def set_height(self, side):
        self.side = side
