class MyPoint(object):
    """Creates a point on a coordinate plane with values x and y and a color c."""

    def __init__(self, coord_x, coord_y, color):

        """Defines x and y variables"""
        try:
            self.__x = int(coord_x)
        except ValueError:
            print("X must be a integer")

        try:
            self.__y = int(coord_y)
        except ValueError:
            print("Y must be a integer")

        try:
            colors = ["red", "green", "blue", "yellow", "magenta"]
            ok = 0
            for item in colors:
                if color == item:
                    ok = 1
            if ok == 1:
                self.__c = color
            else:
                raise ValueError
        except ValueError:
            print('Colors must be one of the following : red , green , blue, yellow, magenta')

    def set_x(self, x):
        """
        Set the x coordinate of the point.
        :param x :integer representing the new x coordinate of the point
        :except ValueError if the param x is not an integer
        """
        try:
            x = int(x)
        except ValueError:
            print("The new x value must be an integer.")
        self.__x = x

    def set_y(self, y):
        """
        Set the y coordinate of the point.
        :param y:integer representing the new y coordinate of the point
        :except ValueError if the param y is not an integer
        """
        try:
            y = int(y)
        except ValueError:
            print("The new y value must be an integer.")
        self.__y = y

    def set_color(self, color):
        """
        Set the color of the point.
        :param color:the new color of the point
        :ValueError if the color parameter is not a string or if it's not word from the predefined colors
        """
        try:
            colors = ["red", "green", "blue", "yellow", "magenta"]
            ok = 0
            for item in colors:
                if color == item:
                    ok = 1
            if ok == 1:
                self.__c = color
            else:
                raise ValueError
        except ValueError:
            print('Colors must be one of the following : red , green , blue, yellow, magenta')

    def get_x(self):
        """
        Returns the x coordinate of the point.
        :return: x :integer representing the coordinate x of the point
        """
        return self.__x

    def get_y(self):
        """
        Returns the y coordinate of the point.
        :return: y :integer representing the coordinate y of the point
        """
        return self.__y

    def get_color(self):
        """
        Returns the color of the point.
        :return: c :string representing the color of the point
        """
        return self.__c

    def __str__(self):
        """
        This function converts the point into a string representation.
        :return: the string representation of the point.
        """
        return "Point(%s,%s) of color %s" % (self.__x, self.__y, self.__c)

    def __eq__(self, other):
        """
        This function verify if 2 different points are the same.
        :param other: the other point
        :return: True(if the points are the same) or False(if the points are not the same)
        """
        try:
            other = MyPoint(other.__x, other.__y, other.__c)
            return self.__x == other.__x and self.__y == other.__y and self.__c == other.__c
        except ValueError:
            print("The other value is not a point")
        except AttributeError:
            print("The other argument does not have the same attributes")


