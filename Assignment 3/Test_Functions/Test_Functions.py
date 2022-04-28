from Repository.Point_Repository import PointRepository
from Domain.MyPoint_class import MyPoint


def print_test_menu():
    """
    Prints all the options in the console type interface.
    """
    print("----------------------------------------------------------")
    print("Test the:")
    print("0 -to go back to the main menu")
    print("1 -Add a point to the repository")
    print("2 -Get all points")
    print("3 -Get a point at a given index")
    print("4 -Get all points of a given color")
    print("5 -Get all points that are inside a given square (up-left corner and length given)")
    print("6 -Get the minimum distance between two points")
    print("7 -Update a point at a given index")
    print("8 -Delete a point by index")
    print("9 -Delete all points that are inside a given square")
    print("10 -Plot all points in a chart (using library matplotlib)")
    print("11 -Get all points that are inside a given circle (center of circle, radius given)")
    print("12 -Get all points that are inside a given rectangle (up-left corner, length and width given)")
    print("13 -Get the maximum distance between two points")
    print("14 -Get the number of points of a given color")
    print("15 -Update the color of a point given its coordinates")
    print("16 -Shift all points on the x axis")
    print("17 -Shift all points on the y axis")
    print("18 -Delete a point by coordinates")
    print("19 -Delete all points that are inside a given circle")
    print("20 -Delete all points within a certain distance from a given point")
    print("21 -Show test menu")


def test_function_for_adding_a_point():
    """This function test the function of adding a point into the repository."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    try:
        print("Ex 1:(1,2,red)")
        test_list.add_point(1, 2, 'red')
        print(test_list)
    except ValueError:
        print("ValueError")
    else:
        try:
            print("Ex 2:(2,3,green)")
            test_list.add_point(2, 3, 'green')
            print(test_list)
        except ValueError:
            print("ValueError")
        else:
            try:
                print("Ex 3:(0,2,lime)")
                test_list.add_point(0, 2, 'lime')
                print(test_list)
            except ValueError:
                print("ValueError")


def test_function_for_getting_all_points():
    """This function test getting all points from the repository."""
    print("--------------------")
    test_list1 = PointRepository(points_list=[])
    try:
        print("Ex 1:(4,3,blue)")
        test_list1.add_point(4, 3, 'blue')
        print(test_list1.get_all_points())
        test_list1.get_all_points()
    except ValueError:
        print("ValueError")
    else:
        try:
            test_list2 = PointRepository(points_list=[])
            print("Ex 2:(7,9,yellow)")
            test_list2.add_point(7, 9, 'yellow')
            temporary_list = test_list2.get_all_points()
            print(temporary_list)
        except ValueError:
            print("ValueError")
        else:
            try:
                test_list3 = PointRepository(points_list=[])
                print("Ex 3:(12,4,blue)")
                test_list3.add_point(0, 2, 'blue')
                print(test_list3.get_all_points())
            except ValueError:
                print("ValueError")


def test_function_for_getting_a_point_at_a_given_index():
    """This function test getting a point by index from the repository."""
    test_list1 = PointRepository(points_list=[])
    print("--------------------")
    try:
        print("Ex 1:(17,15,red)")
        test_list1.add_point(17, 15, 'red')
        print("Get point at index 0:")
        print(test_list1.get_a_point_at_a_given_index(0))
    except ValueError:
        print("ValueError")
    else:
        try:
            test_list2 = PointRepository(points_list=[])
            print("Ex 2:(9,9,blue),(17,9,red),(9,8,blue)")
            test_list2.add_point(9, 9, 'blue')
            test_list2.add_point(17, 9, 'red')
            test_list2.add_point(9, 8, 'blue')
            print("Get point at index 1:")
            print(test_list2.get_a_point_at_a_given_index(1))
        except ValueError:
            print("ValueError")
        else:
            try:
                test_list3 = PointRepository(points_list=[])
                print("Ex 3:(12,5,yellow),(9,4,blue),(4,7,green),(9,8,blue)")
                test_list3.add_point(12, 5, 'yellow')
                test_list3.add_point(9, 4, 'blue')
                test_list3.add_point(4, 7, 'green')
                test_list3.add_point(9, 8, 'blue')
                print("Get a point at index 4")
                print(test_list3.get_a_point_at_a_given_index(4))
            except IndexError:
                print("IndexError")


def test_get_all_points_of_given_color():
    """This function verifies the get all points of given color function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(3, 1.5, 'red')
    test_list.add_point(1, 2, 'red')
    test_list.add_point(2, 4, 'green')
    test_list.add_point(1.5, 2, 'green')
    test_list.add_point(1.5, 3, 'yellow')
    print(test_list)
    print("Gets all points of color red")
    print(test_list.get_all_points_of_given_color('red'))
    print("Gets all points of color blue")
    print(test_list.get_all_points_of_given_color('blue'))
    print("Gets all points of color yellow")
    print(test_list.get_all_points_of_given_color('yellow'))


def test_get_all_points_that_are_inside_a_given_square():
    """This function verifies the get all points that are inside a given square function"""
    test_list = PointRepository(points_list=[])
    test_list.add_point(1, 2, 'red')
    test_list.add_point(2, 4, 'green')
    test_list.add_point(3, 1.5, 'red')
    test_list.add_point(1.5, 2, 'green')
    test_list.add_point(1.5, 3, 'yellow')
    print(test_list)
    print("The points inside the square with the upper_left_corner coordinate (3,3) and length 3:")
    print(test_list.get_all_points_inside_a_square(MyPoint(3, 3, 'red'), 5))
    print("The points inside the square with the upper_left_corner coordinate (1,2) and length 2:")
    print(test_list.get_all_points_inside_a_square(MyPoint(1, 2, 'yellow'), 2))
    print("The points inside the square with the upper_left_corner coordinate (1.5,2) and length 3:")
    print(test_list.get_all_points_inside_a_square(MyPoint(1.5, 2, 'blue'), 3))


def test_get_the_minimum_distance_between_two_points():
    """This function verifies the get minimum distance between two points in the repository function."""
    test_list1 = PointRepository(points_list=[])

    test_list1.add_point(1, 2, 'red')
    test_list1.add_point(2, 4, 'green')
    test_list1.add_point(3, 1.5, 'red')
    test_list1.add_point(3, 2, 'green')
    print(test_list1)
    print("The minimum distance between 2 points is:")
    print(test_list1.get_minimum_distance_between_two_points())
    test_list2 = PointRepository(points_list=[])

    test_list2.add_point(1, 2, 'red')
    test_list2.add_point(4, 2, 'blue')
    test_list2.add_point(3, 1, 'red')
    test_list2.add_point(8, 2, 'red')
    print(test_list2)
    print("The minimum distance between 2 points is:")
    print(test_list2.get_minimum_distance_between_two_points())
    test_list3 = PointRepository(points_list=[])

    test_list3.add_point(3, 9, 'yellow')
    test_list3.add_point(7, 2, 'blue')
    test_list3.add_point(1, 5, 'blue')
    test_list3.add_point(4, 6, 'yellow')
    print(test_list3)
    print("The minimum distance between 2 points is:")
    print(test_list3.get_minimum_distance_between_two_points())


def test_delete_a_point_by_index():
    """This function verifies the delete a point by index from the repository function."""
    test_list1 = PointRepository(points_list=[])

    test_list1.add_point(1, 2, 'red')
    test_list1.add_point(2, 4, 'green')
    test_list1.add_point(3, 1.5, 'red')
    test_list1.add_point(3, 2, 'green')
    print(test_list1)
    test_list1.delete_point(0)
    print("Deletes the point at index 0")
    print(test_list1)
    test_list1.delete_point(2)
    print("Deletes the point at index 2")
    print(test_list1)
    test_list1.delete_point(1)
    print("Deletes the point at index 1 ")
    print(test_list1)
    print("Deletes the point at index 0 ")
    test_list1.delete_point(0)
    try:
        print(test_list1)
    except TypeError:
        print("The repository is empty.")


def test_plot_all_points_inside_a_chart():
    """This function verifies the plot all points from the repository function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(1, 2, 'red')
    test_list.add_point(2, 4, 'green')
    test_list.add_point(1.5, 3, 'yellow')
    test_list.add_point(1.5, 2, 'green')
    test_list.add_point(3, 1.5, 'red')
    test_list.plot_points_in_chart()


def test_delete_all_points_that_are_inside_a_given_square():
    """This function verifies the delete all points that are inside a given square from the repository function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(1, 2, 'red')
    test_list.add_point(2, 4, 'green')
    test_list.add_point(3, 2, 'blue')
    test_list.add_point(4, 5, 'red')
    print(test_list)
    print("Deletes all the points that are inside the square with the up_left_corner(1,2) and length 3")
    print(test_list.delete_all_points_inside_a_square(MyPoint(1, 2, 'red'), 3))

    print("Deletes all the points that are inside the square with the up_left_corner(2,1) and length 3")
    print(test_list.delete_all_points_inside_a_square(MyPoint(2, 1, 'blue'), 3))
    print("Deletes all the points that are inside the square with the up_left_corner(1,1) and length 1")
    print(test_list.delete_all_points_inside_a_square(MyPoint(1, 1, 'red'), 1))


def test_get_all_points_inside_a_given_circle():
    """This function verifies the get all points that are inside a given circle from the repository function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(3, 2, 'red')
    test_list.add_point(2, 4, 'green')
    test_list.add_point(1, 2, 'blue')
    test_list.add_point(4, 5, 'red')
    print(test_list)
    print("Gets all the points that are inside the circle with the up_left_corner(3,2) and radius 2")
    print(test_list.get_all_points_inside_of_a_given_circle(MyPoint(3, 2, 'red'), 2))
    print("Gets all the points that are inside the circle with the up_left_corner(2,1) and radius 3")
    print(test_list.get_all_points_inside_of_a_given_circle(MyPoint(2, 1, 'blue'), 3))
    print("Gets all the points that are inside the circle with the up_left_corner(2,2) and radius 4")
    print(test_list.get_all_points_inside_of_a_given_circle(MyPoint(2, 2, 'red'), 4))


def test_get_all_points_inside_a_given_rectangle():
    """This function verifies the get all points that are inside a given rectangle from the repository function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(3, 2, 'red')
    test_list.add_point(4, 4, 'green')
    test_list.add_point(2, 2, 'blue')
    test_list.add_point(1, 5, 'red')
    print(test_list)
    print("Gets all the points that are inside the rectangle with the up_left_corner(2,2) and length 4 and width 2")
    print(test_list.get_all_points_inside_a_given_rectangle(MyPoint(2, 2, 'red'), 4, 2))
    print("Gets all the points that are inside the rectangle with the up_left_corner(1,2) and length 3 and width 3")
    print(test_list.get_all_points_inside_a_given_rectangle(MyPoint(1, 2, 'blue'), 3, 3))
    print("Gets all the points that are inside the rectangle with the up_left_corner(3,2) and length 1 and width 4")
    print(test_list.get_all_points_inside_a_given_rectangle(MyPoint(3, 2, 'red'), 1, 4))


def test_get_the_maximum_distance_between_two_points():
    """This function verifies the get maximum distance between two points in the repository function."""
    test_list1 = PointRepository(points_list=[])

    test_list1.add_point(2, 2, 'blue')
    test_list1.add_point(2, 2, 'green')
    test_list1.add_point(3, 1.5, 'red')
    test_list1.add_point(2, 3, 'green')
    print(test_list1)
    print("The maximum distance between 2 points is:")
    print(test_list1.get_maximum_distance_between_two_points())
    test_list2 = PointRepository(points_list=[])

    test_list2.add_point(1, 2, 'red')
    test_list2.add_point(4, 2, 'blue')
    test_list2.add_point(3, 2, 'yellow')
    test_list2.add_point(4, 3, 'red')
    print(test_list2)
    print("The maximum distance between 2 points is:")
    print(test_list2.get_maximum_distance_between_two_points())
    test_list3 = PointRepository(points_list=[])

    test_list3.add_point(3, 9, 'yellow')
    test_list3.add_point(2, 2, 'red')
    test_list3.add_point(3, 5, 'blue')
    test_list3.add_point(5, 6, 'yellow')
    print(test_list3)
    print("The maximum distance between 2 points is:")
    print(test_list3.get_maximum_distance_between_two_points())


def test_get_the_number_of_points_of_given_color():
    """This function verifies the get the number of points of given color."""
    test_list1 = PointRepository(points_list=[])

    test_list1.add_point(2, 1, 'blue')
    test_list1.add_point(2, 2.5, 'green')
    test_list1.add_point(7, 3, 'red')
    test_list1.add_point(9, 1, 'green')
    print(test_list1)
    print("The number of points of color magenta:")
    print(test_list1.get_the_number_of_points_of_given_color('magenta'))
    test_list2 = PointRepository(points_list=[])

    test_list2.add_point(8, 2, 'red')
    test_list2.add_point(1, 2, 'blue')
    test_list2.add_point(6, 2, 'yellow')
    test_list2.add_point(9, 3, 'red')
    print(test_list2)
    print("The number of points of color blue:")
    print(test_list2.get_the_number_of_points_of_given_color('blue'))
    test_list3 = PointRepository(points_list=[])

    test_list3.add_point(3, 9, 'yellow')
    test_list3.add_point(4, 1, 'red')
    test_list3.add_point(3, 2, 'blue')
    test_list3.add_point(4, 4, 'yellow')
    print(test_list3)
    print("The number of points of color yellow:")
    print(test_list3.get_the_number_of_points_of_given_color('yellow'))


def test_update_a_point_at_given_index_function():
    """This function verifies the update a point at a given index function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(1, 2, 'red')
    test_list.add_point(2, 4, 'green')
    print(test_list)
    print("Update the coordinates and color of point at index 0")
    test_list.update_point(0, 3, 4, 'yellow')
    print(test_list)
    print("Update the coordinates and color of point at index 1")
    test_list.update_point(1, 2, 3, 'red')
    print(test_list)
    print("Update the coordinates and color of point at index 0 again")
    test_list.update_point(0, 0, 1, 'blue')
    print(test_list)


def test_update_a_point_given_its_coordinate():
    """This function verifies the update a point given its coordinates function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(1, 2, 'red')
    test_list.add_point(5, 9, 'green')
    test_list.add_point(3, 2, 'magenta')
    test_list.add_point(1, 7, 'yellow')
    print(test_list)
    print("Update the color of point given the coordinates (1,2) and color yellow")
    test_list.update_the_color_of_a_point_given_its_coordinates(1, 2, 'yellow')
    print(test_list)
    print("Update the color of point given the coordinates (3,3) and color red")
    test_list.update_the_color_of_a_point_given_its_coordinates(3, 3, 'red')
    print(test_list)
    print("Update the color of point given the coordinates (1,7) and color magenta")
    test_list.update_the_color_of_a_point_given_its_coordinates(1, 7, 'magenta')
    print(test_list)


def test_shift_all_points_on_the_x_axis():
    """This function verifies the shift all points on the x axis from the repository function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(1, 1, 'yellow')
    test_list.add_point(5, 1, 'blue')
    test_list.add_point(3, 3, 'magenta')
    test_list.add_point(1, 0, 'red')
    print(test_list)
    print("Shift the x axis of the points in the repository by 3")
    test_list.shift_all_points_on_x_axis(3)
    print(test_list)
    print("Shift the x axis of the points in the repository by 2")
    test_list.shift_all_points_on_x_axis(2)
    print(test_list)
    print("Shift the x axis of the points in the repository by -4")
    test_list.shift_all_points_on_x_axis(-4)
    print(test_list)


def test_shift_all_points_on_the_y_axis():
    """This function verifies the shift all points on the y axis from the repository function."""
    print("--------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(2, 4, 'red')
    test_list.add_point(2, 3, 'magenta')
    test_list.add_point(0, 3, 'magenta')
    test_list.add_point(3, 5, 'blue')
    print(test_list)
    print("Shift the y axis of the points in the repository by 1")
    test_list.shift_all_points_on_y_axis(1)
    print(test_list)
    print("Shift the y axis of the points in the repository by -3")
    test_list.shift_all_points_on_y_axis(-3)
    print(test_list)
    print("Shift the y axis of the points in the repository by 6")
    test_list.shift_all_points_on_y_axis(6)
    print(test_list)


def test_delete_a_point_by_coordinate():
    """This function verifies the delete a point by coordinate from the repository function."""
    test_list1 = PointRepository(points_list=[])

    test_list1.add_point(2, 3, 'green')
    test_list1.add_point(5, 4, 'magenta')
    test_list1.add_point(3, 1.5, 'blue')
    test_list1.add_point(7, 2, 'green')
    print(test_list1)
    test_list1.delete_point_by_coordinate(2, 3)
    print("Deletes the point by coordinate(2,3)")
    print(test_list1)
    test_list1.delete_point_by_coordinate(7, 2)
    print("Deletes the point by coordinate(7,2)")
    print(test_list1)
    test_list1.delete_point_by_coordinate(3, 3)
    print("Deletes the point by coordinate(3,3)")
    print(test_list1)
    test_list1.delete_point_by_coordinate(2, 3)
    print("Deletes the point by coordinate(2,3)")


def test_delete_all_points_that_are_inside_a_given_circle():
    """This function verifies the delete all points that are inside a given circle from the repository function."""
    print("---------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(3, 2, 'red')
    test_list.add_point(2, 4, 'green')
    test_list.add_point(1, 2, 'blue')
    test_list.add_point(4, 5, 'red')
    print(test_list)
    print("Deletes all the points that are inside the circle with the up_left_corner(3,2) and radius 2")
    test_list.delete_all_points_inside_a_given_circle(MyPoint(3, 2, 'red'), 2)
    print(test_list)
    print("Deletes all the points that are inside the circle with the up_left_corner(2,1) and radius 3")
    test_list.delete_all_points_inside_a_given_circle(MyPoint(2, 1, 'blue'), 3)
    print(test_list)
    print("Deletes all the points that are inside the circle with the up_left_corner(2,2) and radius 4")
    test_list.delete_all_points_inside_a_given_circle(MyPoint(2, 2, 'red'), 4)
    print(test_list)


def test_delete_all_points_within_a_certain_distance_from_a_given_point():
    """This function test the delete all points within a certain distance from a given point function."""
    print("---------------------")
    test_list = PointRepository(points_list=[])
    test_list.add_point(3, 2, 'red')
    test_list.add_point(3, 4, 'green')
    test_list.add_point(4, 2, 'blue')
    test_list.add_point(5, 5, 'red')
    print(test_list)
    print("Deletes all the points that are within the distance 3 from the point at index 0")
    test_list.delete_points_within_a_certain_distance(3, 0)
    print(test_list)
    print("Deletes all the points that are within the distance 2 from the point at index 1")
    test_list.delete_points_within_a_certain_distance(2, 1)
    print(test_list)
    print("Deletes all the points that are within the distance 1 from the point at index 3")
    test_list.delete_points_within_a_certain_distance(1, 3)
    print(test_list)


def test_menu():
    print_test_menu()
    command = input(">>> ")
    while command != "0":
        if command == "21":
            print_test_menu()
        elif command == '1':
            test_function_for_adding_a_point()
        elif command == '2':
            test_function_for_getting_all_points()
        elif command == '3':
            test_function_for_getting_a_point_at_a_given_index()
        elif command == '4':
            test_get_all_points_of_given_color()
        elif command == '5':
            test_get_all_points_that_are_inside_a_given_square()
        elif command == '6':
            test_get_the_minimum_distance_between_two_points()
        elif command == '7':
            test_update_a_point_at_given_index_function()
        elif command == '8':
            test_delete_a_point_by_index()
        elif command == '9':
            test_delete_all_points_that_are_inside_a_given_square()
        elif command == '10':
            test_plot_all_points_inside_a_chart()
        elif command == '11':
            test_get_all_points_inside_a_given_circle()
        elif command == '12':
            test_get_all_points_inside_a_given_rectangle()
        elif command == '13':
            test_get_the_maximum_distance_between_two_points()
        elif command == '14':
            test_get_the_number_of_points_of_given_color()
        elif command == '15':
            test_update_a_point_given_its_coordinate()
        elif command == '16':
            test_shift_all_points_on_the_x_axis()
        elif command == '17':
            test_shift_all_points_on_the_y_axis()
        elif command == '18':
            test_delete_a_point_by_coordinate()
        elif command == '19':
            test_delete_all_points_that_are_inside_a_given_circle()
        elif command == '20':
            test_delete_all_points_within_a_certain_distance_from_a_given_point()
        else:
            print("Invalid command!")
        command = input(">>> ")
