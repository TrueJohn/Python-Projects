from Domain.MyPoint_class import MyPoint
import matplotlib.pyplot as plt


class PointRepository:
    """Creates a list of _points."""

    def __init__(self, points_list):
        """
        Initialising the point repository.
        :param points_list: a list of points
        """
        self._points = points_list.copy()

    def __str__(self):
        """
        Converting a PointRepository object into a string.
        """
        try:
            repr_str = f"The number of _points in the repository is: {self.get_length()}\n"
            for point in self._points:
                repr_str += str(point) + "\n"
            return repr_str
        except TypeError:
            print("The repository is empty.")

    def get_length(self):
        """
        This function gets the length of the repository.
        :return:length
        """
        try:
            return len(self._points)
        except TypeError:
            print("The repository is empty")

    def add_point(self, x, y, color):
        """
        #1 Add a new point to the repository.
        :param x: x coordinate (integer)
        :param y: y coordinate (integer)
        :param color: color (string)

        """
        try:
            x_coord = int(x)
        except ValueError:
            print("The X coordinate must be an integer")
        else:
            try:
                y_coord = int(y)
            except ValueError:
                print("The Y coordinate must be an integer")
            else:
                try:
                    colors = ["red", "green", "blue", "yellow", "magenta"]
                    ok = 0
                    for item in colors:
                        if color == item:
                            ok = 1
                    if ok == 0:
                        raise ValueError
                except ValueError:
                    print('Colors must be one of the following : red , green , blue, yellow, magenta')
                else:
                    point = MyPoint(x_coord, y_coord, color)
                    self._points.append(point)

    def get_all_points(self):
        """
        #2 Prints all the _points from the point repository.
        :return: list of _points
        """
        copy_list = self._points
        return copy_list

    def get_a_point_at_a_given_index(self, index):
        """
        #3 Returns the point at a given index.
        :param index: the index of the point wanted
        :return:the point at the given index
        """
        try:
            if index < 0 or index >= len(self._points):
                raise IndexError
        except IndexError:
            print(f'The given index={index} is not in the boundary of the repository (0,{len(self._points)}).')
        else:
            return self._points[index]

    def get_all_points_of_given_color(self, color):
        """
        #4 Gets all _points of a given color.
        :param color:the wanted color
        :return:temporary_point_list:a list of _points with the same wanted color
        """
        try:
            colors = ["red", "green", "blue", "yellow", "magenta"]
            ok = 0
            for item in colors:
                if color == item:
                    ok = 1
            if ok == 0:
                raise ValueError
        except ValueError:
            print('Colors must be one of the following : red , green , blue, yellow, magenta')
        temporary_point_list = PointRepository([])
        for i in range(len(self._points)):
            if color == self._points[i].get_color():
                temporary_point_list.add_point(self._points[i].get_x(), self._points[i].get_y(),
                                               self._points[i].get_color())
        return temporary_point_list

    def get_all_points_inside_a_square(self, up_left_corner, length):
        """
        #5 Gets all the _points inside a given square.
        :param up_left_corner: the coordinates of the up_left_corner of the square(point)
        :param length: the length of the square(natural number)
        :return:the list of _points inside the given square
        """
        try:
            length = int(length)
            if length <= 0:
                raise ValueError
        except ValueError:
            print("The length must be an natural number bigger then 0.")

        try:
            up_left_corner = MyPoint(up_left_corner.get_x(), up_left_corner.get_y(), up_left_corner.get_color())
        except ValueError:
            print("The up_left_corner parameter must be a point ( x(integer) ,y(integer) ,color(string))")

        temporary_point_list = PointRepository([])

        for i in range(len(self._points)):
            if not (not (up_left_corner.get_x() + length >= self._points[i].get_x() >= up_left_corner.get_x()) or not (
                    up_left_corner.get_y() >= self._points[i].get_y() >= up_left_corner.get_y() - length)):
                temporary_point_list.add_point(self._points[i].get_x(), self._points[i].get_y(),
                                               self._points[i].get_color())
        return temporary_point_list

    def get_minimum_distance_between_two_points(self):
        """
        #6 Returns the minimum distance between 2 _points in the repository
        :return: minimum:the minimum distance between 2 _points in the repository
        """
        try:
            if len(self._points) < 2:
                raise IndexError
        except IndexError:
            print("The repository doesn't have at least 2 point.")

        minimum = get_the_length_between_two_points(self._points[0], self._points[1])
        for i in range(self.get_length()):
            for j in range(i + 1, self.get_length()):
                if get_the_length_between_two_points(self._points[i], self._points[j]) < minimum:
                    minimum = get_the_length_between_two_points(self._points[i], self._points[j])
        return minimum

    def update_point(self, index_p, x, y, color):
        """
        #7 Updates a point at a given index
        :param index_p: the index of the point to update
        :param x: the new x coordinate of the point
        :param y: the new y coordinate of the point
        :param color: the new color of the point
        :return:
        """
        self._points[index_p].set_x(x)
        self._points[index_p].set_y(y)
        self._points[index_p].set_color(color)

    def delete_point(self, index):
        """
        #8 Deletes a point at a given index
        :param index: the index of the point to delete
        """
        try:
            if index < 0 or index >= len(self._points):
                raise IndexError
        except IndexError:
            print(f'The given index={index} is not in the boundary of the repository (0,{len(self._points)}).')
        except TypeError:
            print("The repository is empty.")
        else:
            if index == 0 and self.get_length() > 1:
                self._points = self._points[index + 1:]
            elif index == 0:
                self._points = None
            elif index == self.get_length():
                self._points = self._points[:index]
            else:
                self._points = self._points[:index] + self._points[index + 1:]

    def delete_all_points_inside_a_square(self, up_left_corner, length):
        """
        #9 Deletes all the _points inside a square.
        :param up_left_corner: the coordinates of the up_left_corner of the square(point)
        :param length: the length of the square(natural number)
        :return:the list of _points inside the given square
        """
        try:
            up_left_corner = MyPoint(up_left_corner.get_x(), up_left_corner.get_y(),
                                     up_left_corner.get_color())
        except ValueError:
            print("The up_left_corner of the square parameter must be a point ( x ,y ,color)")

        try:
            length = int(length)
            if length <= 0:
                raise ValueError
        except ValueError:
            print("The length must be a natural numbers bigger then 0")
        temp_list = PointRepository([])
        for i in range(self.get_length()):
            if up_left_corner.get_x() + length >= self._points[i].get_x() >= up_left_corner.get_x() and \
                    up_left_corner.get_y() >= self._points[i].get_y() >= up_left_corner.get_y() - length:
                temp_list.add_point(self._points[i].get_x(), self._points[i].get_y(), self._points[i].get_color())
        return temp_list

    def plot_points_in_chart(self):
        """
        #10 This function plots the points from the repository in a chart.
        """
        x_list = []
        y_list = []
        color_list = []
        for i in range(self.get_length()):
            x_list.append(self._points[i].get_x())
            y_list.append(self._points[i].get_y())
            color_list.append(self._points[i].get_color())
        plt.scatter(x_list, y_list, c=color_list)
        plt.show()

    def get_all_points_inside_of_a_given_circle(self, center_of_the_circle, radius_given):
        """
        #11 This function gets all the points inside a given circle.
        :param center_of_the_circle:the coordinates of the center of the circle
        :param radius_given:integer representing the radius of the circle
        :return:temp_list:a list of points that are inside the given circle
        """
        try:
            center_of_the_circle = MyPoint(center_of_the_circle.get_x(), center_of_the_circle.get_y(),
                                           center_of_the_circle.get_color())
        except ValueError:
            print("The center_of_the_circle parameter must be a point ( x ,y ,color)")

        try:
            radius_given = int(radius_given)
            if radius_given <= 0:
                raise ValueError
        except ValueError:
            print("The given radius must be a natural number bigger then 0")
        temp_list = PointRepository([])
        for i in range(self.get_length() - 1):
            if (self._points[i].get_x() - center_of_the_circle.get_x()) ^ 2 + (
                    self._points[i].get_y() - center_of_the_circle.get_y()) ^ 2 <= radius_given ^ 2:
                temp_list.add_point(self._points[i].get_x(), self._points[i].get_y(), self._points[i].get_color())
        return temp_list

    def get_all_points_inside_a_given_rectangle(self, up_left_corner, length, width):
        """
        #12 This function gets all the points inside a given rectangle.
        :param up_left_corner:the point of up left corner of the rectangle (x,y,color)
        :param length:(integer & >0)the length of the rectangle
        :param width:(integer & >0)the width of the rectangle
        :return:
        """
        try:
            up_left_corner = MyPoint(up_left_corner.get_x(), up_left_corner.get_y(),
                                     up_left_corner.get_color())
        except ValueError:
            print("The up_left_corner parameter must be a point ( x ,y ,color)")

        try:
            length = int(length)
            width = int(width)
            if length <= 0 or width <= 0:
                raise ValueError
        except ValueError:
            print("The length and the width must be a natural numbers bigger then 0")
        temp_list = PointRepository([])
        for i in range(self.get_length()):
            if up_left_corner.get_x() + length >= self._points[i].get_x() >= up_left_corner.get_x() and \
                    up_left_corner.get_y() >= self._points[i].get_y() >= up_left_corner.get_y() - width:
                temp_list.add_point(self._points[i].get_x(), self._points[i].get_y(), self._points[i].get_color())
        return temp_list

    def get_maximum_distance_between_two_points(self):
        """
        #13 Gets the maximum distance between 2 _points in the repository.
        :return: maximum:the maximum distance between 2 _points in the repository
        """
        try:
            if len(self._points) < 2:
                raise IndexError
        except IndexError:
            print("The repository doesn't have at least 2 point.")

        maximum = 0
        for i in range(len(self._points)):
            for j in range(i + 1, len(self._points)):
                if get_the_length_between_two_points(self._points[i], self._points[j]) > maximum:
                    maximum = get_the_length_between_two_points(self._points[i], self._points[j])
        return maximum

    def get_the_number_of_points_of_given_color(self, color):
        """
        #14 Gets the number of _points of given color from the repository.
        :param color:the given color(string)
        :return:number_of_points:the number of _points of the given color from the repository
        """
        number_of_points = 0
        for i in range(len(self._points)):
            if self._points[i].get_color() == color:
                number_of_points += 1
        return number_of_points

    def update_the_color_of_a_point_given_its_coordinates(self, x_coord, y_coord, new_color):
        """
        #15 This function updates the color of the first point of the given coordinates.
        :param x_coord:(integer) the x coordinate of the point
        :param y_coord:(integer) the y coordinate of the point
        :param new_color:(string) the new color of the given point
        """
        ok = 0
        for i in range(self.get_length()):
            if self._points[i].get_y() == y_coord and self._points[i].get_x() == x_coord and ok == 0:
                self._points[i].set_color(new_color)
                ok = 1
        if ok == 0:
            print(f"There does not exist a point with the coordinate ({x_coord},{y_coord}) in the repository.")

    def shift_all_points_on_x_axis(self, value):
        """
        #16 This function shift all _points on x axis with a given value
        :param value:the amount to shift for the x axis for a point in repository
        """
        for i in range(len(self._points)):
            self._points[i].set_x(self._points[i].get_x() + value)

    def shift_all_points_on_y_axis(self, value):
        """
        #17 This function shift all _points on y axis with a given value
        :param value:the amount to shift for the y axis for a point in repository
        """
        for i in range(len(self._points)):
            self._points[i].set_y(self._points[i].get_y() + value)

    def delete_point_by_coordinate(self, x_coord, y_coord):
        """
        #18 This function deletes the first point
        :param x_coord:(integer) representing the x coordinate of the point
        :param y_coord:(integer) representing the y coordinate of the point
        """
        ok = 0
        for i in range(self.get_length()):
            if self._points[i].get_y() == y_coord and self._points[i].get_x() == x_coord and ok == 0:
                self.delete_point(i)
                ok = 1
                break
        if ok == 0:
            print(f"There does not exist a point of the coordinates ({x_coord},{y_coord})")

    def delete_all_points_inside_a_given_circle(self, center_of_the_circle, radius):
        """
        #19 This function deletes all points inside a given circle.
        :param center_of_the_circle: the point of the center of the circle (x(integer &>0),y(integer &>0, color)
        :param radius:(integer &>0) the radius of the given circle
        :return:
        """
        try:
            for i in range(self.get_length() - 1):
                if (self._points[i].get_x() - center_of_the_circle.get_x()) ^ 2 + (
                        self._points[i].get_y() - center_of_the_circle.get_y()) ^ 2 <= radius ^ 2:
                    self.delete_point(i)
        except IndexError:
            print("Index out of range")

    def delete_points_within_a_certain_distance(self, distance, index_of_point):
        """
        #20 Deletes the _points within a certain distance from a given point
        :param distance:the specified distance for the deletion
        :param index_of_point:the index of the given point
        """

        for i in range(self.get_length() - 1):
            if get_the_length_between_two_points(self.get_a_point_at_a_given_index(index_of_point),
                                                 self._points[i]) == distance:
                self.delete_point(i)


def get_the_length_between_two_points(point1, point2):
    """
    This function calculates the distance between two given _points.
    :param point1:(point with x,y,color)
    :param point2:(point with x,y,color)
    :return:distance(the minimum distance between two _points
    """
    try:
        distance = ((point1.get_x() - point2.get_x()) ** 2 + (point1.get_y() - point2.get_y()) ** 2) ** 0.5
    except AttributeError:
        print("Error")
    else:
        return distance


"""
    p = PointRepository([MyPoint(1, 2, 'red'), MyPoint(2, 3, 'blue'), MyPoint(1.5, 2, 'red')])

    print("Print all _points:")
    print(p.get_all_points())
    print('')
    print('')
    print("Print all _points of given color:")
    print(p.get_all_points_of_given_color('red'))
    print('')
    print('')
    print("The minimum distance between two _points is:", p.get_minimum_distance_between_two_points())
    print('')
    print('')
    print("The maximum distance between two _points is:", p.get_maximum_distance_between_two_points())
    print('')
    print('')
    print("Prints all _points inside a square:")
    print(p.get_all_points_inside_a_square(MyPoint(0, 4, 'red'), 3))
    print('')
    print('')
    print("The _points before shift:")
    print(p)
    print("The _points after shift:")
    p.shift_all_points_on_y_axis(4)
    print(p)
    print('')
    print('')
    index1 = 1
    print(f"The list after deleting point at index{index1}:")
    p.delete_point(index1)
    print(p)

    print("Adding some values to the list:")
    p.add_point(2, 4, 'red')
    p.add_point(3, 2, 'blue')
    p.add_point(1, 3, 'green')

    print(p)


    print('----------------------------------------------------------------------------')
    for i1 in range(len(p._points)):
        for j1 in range(len(p._points)):
            print(f'The distance between {p._points[i1]} and {p._points[j1]}:')
            print(get_minimum_distance_between_two_points(p._points[i1], p._points[j1]))
    
    print('----------------------------------------------------------------------------')
    
    d = 0.5
    index2 = 1
    print(f"Delete _points with the length {d} for {p.get_all_points()[index2]}")
    p.delete_points_within_a_certain_distance(d, index2)
    print(p)

    p.plot_points_in_chart()
"""
