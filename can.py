# class Canvas:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def draw(self, shape, color):
#         # Function to draw shape on the canvas with given color
#         pass


# class Circle:
#     def __init__(self, x, y, radius, color):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.color = color


# def draw_circle(canvas, circle):
#     """
#     Draw a circle on the canvas with the given color.

#     Args:
#         canvas (Canvas): Canvas object to draw on
#         circle (Circle): Circle object to draw
#     """

#     # Get circle properties
#     circle_color = circle.color
#     circle_center = (circle.x, circle.y)
#     circle_radius = circle.radius

#     # Draw the circle on the canvas
#     canvas.draw((circle_center, circle_radius), circle_color)

#-----------------------------------------------------------

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, shape, color):
        # Function to draw shape on the canvas with given color
        pass


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


def draw_rectangle(canvas, rectangle):
    """
    Draw a rectangle on the canvas with the given color.

    Args:
        canvas (Canvas): Canvas object to draw on
        rectangle (Rectangle): Rectangle object to draw
    """

    # Draw the rectangle on the canvas
    canvas.draw(rectangle, rectangle.color)
    
# Create objects
canvas = Canvas(500, 400)
rect = Rectangle(10, 20, 100, 50, "Red")

# Draw rectangle
draw_rectangle(canvas, rect)