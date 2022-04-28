from Repository.Point_Repository import PointRepository
from Domain.MyPoint_class import MyPoint
from Test_Functions.Test_Functions import test_menu


def print_menu():
    """
    Prints all the options in the console type interface.
    """
    print("----------------------------------------------------------")
    print("Write:")
    print("1 - Add a point to the repository")
    print("2 - Get all points")
    print("3 - Get a point at a given index")
    print("4 - Get all points of a given color")
    print("5 - Get all points that are inside a given square (up-left corner and length given)")
    print("6 - Get the minimum distance between two points")
    print("7 - Update a point at a given index")
    print("8 - Delete a point by index")
    print("9 - Delete all points that are inside a given square")
    print("10 - Plot all points in a chart (using library matplotlib)")
    print("11 - Get all points that are inside a given circle (center of circle, radius given)")
    print("12 - Get all points that are inside a given rectangle (up-left corner, length and width given)")
    print("13 - Get the maximum distance between two points")
    print("14 - Get the number of points of a given color")
    print("15 - Update the color of a point given its coordinates")
    print("16 - Shift all points on the x axis")
    print("17 - Shift all points on the y axis")
    print("18 - Delete a point by coordinates")
    print("19 - Delete all points that are inside a given circle")
    print("20 - Delete all points within a certain distance from a given point")
    print("21 - Test all functions with predefined examples ")
    print("22 - Print the Menu")


def start():
    """
    Start the console type interface.
    :return:
    """
    print_menu()
    point_list = PointRepository(points_list=[])
    point_list.add_point(1, 0, 'red')
    point_list.add_point(3, 3, 'blue')
    point_list.add_point(5, 3, 'green')
    command = input(">>> ")
    while command != "0":
        if command == "22":
            print_menu()
        elif command == "1":
            try:
                x_coord = int(input("X coordinate= "))
            except ValueError:
                print("The X coordinate must be an integer")
            else:
                try:
                    y_coord = int(input("Y coordinate= "))
                except ValueError:
                    print("The Y coordinate must be an integer")
                else:
                    try:
                        color = input("Color= ")
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
                        point_list.add_point(x_coord, y_coord, color)

        elif command == "2":
            print(point_list)
        elif command == "3":
            try:
                index = int(input("index of point="))
                if index < 0 or index > point_list.get_length() - 1:
                    raise IndexError
            except IndexError:
                print(f"The index must be between 0 and {point_list.get_length() - 1}")
            except TypeError:
                print(f"The index is not an integer.")
            else:
                print(point_list.get_a_point_at_a_given_index(index))

        elif command == '4':
            try:
                color = input("Color= ")
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
                print(point_list.get_all_points_of_given_color(color))
        elif command == '5':
            try:
                x_coord = int(input("X coordinate= "))
            except ValueError:
                print("The X coordinate must be an integer")
            else:
                try:
                    y_coord = int(input("Y coordinate= "))
                except ValueError:
                    print("The Y coordinate must be an integer")
                else:
                    try:
                        color = input("Color= ")
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
                        try:
                            length = int(input("length="))
                            if length <= 0:
                                raise ValueError
                        except ValueError:
                            print("The length must be bigger than 0.")
                        else:
                            up_left_corner = MyPoint(x_coord, y_coord, color)
                            print(point_list.get_all_points_inside_a_square(up_left_corner, length))

        elif command == '6':
            print(point_list.get_minimum_distance_between_two_points())
        elif command == '7':
            try:
                index = int(input("index of point="))
                if index < 0 or index > point_list.get_length() - 1:
                    raise IndexError
            except IndexError:
                print(f"The index must be between 0 and {point_list.get_length() - 1}")
            except TypeError:
                print(f"The index is not an integer.")
            else:
                try:
                    x_coord = int(input("X coordinate= "))
                except ValueError:
                    print("The X coordinate must be an integer")
                else:
                    try:
                        y_coord = int(input("Y coordinate= "))
                    except ValueError:
                        print("The Y coordinate must be an integer")
                    else:
                        try:
                            color = input("Color= ")
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
                            point_list.update_point(index, x_coord, y_coord, color)
        elif command == '8':
            try:
                index = int(input("index of point="))
                if index < 0 or index > point_list.get_length() - 1:
                    raise IndexError
            except IndexError:
                print(f"The index must be between 0 and {point_list.get_length() - 1}")
            except TypeError:
                print(f"The index is not an integer.")
            else:
                point_list.delete_point(index)
        elif command == '9':
            try:
                x_coord = int(input("X coordinate= "))
            except ValueError:
                print("The X coordinate must be an integer")
            else:
                try:
                    y_coord = int(input("Y coordinate= "))
                except ValueError:
                    print("The Y coordinate must be an integer")
                else:
                    try:
                        color = input("Color= ")
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
                        try:
                            length = int(input("length="))
                            if length <= 0:
                                raise ValueError
                        except ValueError:
                            print("The length must be bigger than 0.")
                        else:
                            up_left_corner = MyPoint(x_coord, y_coord, color)
                            point_list.delete_all_points_inside_a_square(up_left_corner, length)
        elif command == '10':
            point_list.plot_points_in_chart()
        elif command == '11':
            try:
                x_coord = int(input("X coordinate= "))
            except ValueError:
                print("The X coordinate must be an integer")
            else:
                try:
                    y_coord = int(input("Y coordinate= "))
                except ValueError:
                    print("The Y coordinate must be an integer")
                else:
                    try:
                        color = input("Color= ")
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
                        try:
                            radius = int(input("radius="))
                            if radius <= 0:
                                raise ValueError
                        except ValueError:
                            print("The radius must be bigger than 0.")
                        else:
                            the_center_of_circle = MyPoint(x_coord, y_coord, color)
                            print(point_list.get_all_points_inside_of_a_given_circle(the_center_of_circle, radius))
        elif command == '12':
            try:
                x_coord = int(input("X coordinate= "))
            except ValueError:
                print("The X coordinate must be an integer")
            else:
                try:
                    y_coord = int(input("Y coordinate= "))
                except ValueError:
                    print("The Y coordinate must be an integer")
                else:
                    try:
                        color = input("Color= ")
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
                        try:
                            length = int(input("length="))
                            if length <= 0:
                                raise ValueError
                        except ValueError:
                            print("The length must be bigger than 0.")
                        else:
                            try:
                                width = int(input("width="))
                                if length <= 0:
                                    raise ValueError
                            except ValueError:
                                print("The width must be bigger than 0.")
                            else:
                                up_left_corner = MyPoint(x_coord, y_coord, color)
                                print(point_list.get_all_points_inside_a_given_rectangle(up_left_corner, length, width))
        elif command == '13':
            print(point_list.get_maximum_distance_between_two_points())
        elif command == '14':
            try:
                color = input("Color = ")
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
                print(point_list.get_all_points_of_given_color(color))
        elif command == '15':
            try:
                x_coord = int(input("X coordinate= "))
            except ValueError:
                print("The X coordinate must be an integer")
            else:
                try:
                    y_coord = int(input("Y coordinate= "))
                except ValueError:
                    print("The Y coordinate must be an integer")
                else:
                    try:
                        new_color = input("Color = ")
                        colors = ["red", "green", "blue", "yellow", "magenta"]
                        ok = 0
                        for item in colors:
                            if new_color == item:
                                ok = 1
                        if ok == 0:
                            raise ValueError
                    except ValueError:
                        print('Colors must be one of the following : red , green , blue, yellow, magenta')
                    else:
                        point_list.update_the_color_of_a_point_given_its_coordinates(x_coord, y_coord, new_color)
        elif command == '16':
            try:
                value_to_shift_the_x_axis = int(input("value to shift the x axis="))

            except ValueError:
                print("The value must be an integer")
            else:
                point_list.shift_all_points_on_x_axis(value_to_shift_the_x_axis)
        elif command == '17':
            try:
                value_to_shift_the_y_axis = int(input("value to shift the y axis="))

            except ValueError:
                print("The value must be an integer")
            else:
                point_list.shift_all_points_on_y_axis(value_to_shift_the_y_axis)
        elif command == '18':
            try:
                x_coord = int(input("X coordinate= "))
            except ValueError:
                print("The X coordinate must be an integer")
            else:
                try:
                    y_coord = int(input("Y coordinate= "))
                except ValueError:
                    print("The Y coordinate must be an integer")
                else:
                    point_list.delete_point_by_coordinate(x_coord, y_coord)
        elif command == '19':
            try:
                x_coord = int(input("X coordinate= "))
            except ValueError:
                print("The X coordinate must be an integer")
            else:
                try:
                    y_coord = int(input("Y coordinate= "))
                except ValueError:
                    print("The Y coordinate must be an integer")
                else:
                    try:
                        color = input("Color= ")
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
                        try:
                            radius = int(input("radius="))
                            if radius <= 0:
                                raise ValueError
                        except ValueError:
                            print("The radius must be bigger than 0.")
                        else:
                            the_center_of_circle = MyPoint(x_coord, y_coord, color)
                            point_list.delete_all_points_inside_a_given_circle(the_center_of_circle, radius)
        elif command == '20':
            try:
                index = int(input("index of point="))
                if index < 0 or index > point_list.get_length() - 1:
                    raise IndexError
            except IndexError:
                print(f"The index must be between 0 and {point_list.get_length() - 1}")
            except TypeError:
                print(f"The index is not an integer.")
            else:
                try:
                    distance = float(input("distance="))
                    if distance <= 0:
                        raise ValueError
                except ValueError:
                    print("The radius must be a float number bigger than 0.")
                else:
                    point_list.delete_points_within_a_certain_distance(distance, index)
                    from Repository.Point_Repository import get_the_length_between_two_points
                    print(get_the_length_between_two_points(MyPoint(3, 3, 'red'), MyPoint(5, 3, 'red')))
        elif command == '21':
            test_menu()
        else:
            print("Invalid command!")
        command = input(">>> ")


start()
