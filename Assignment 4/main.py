from Repository.VectorRepository import VectorRepository
from Domain.MyVector import MyVector
from Utility.Functions import verify_vector
from Test_Functions.Test_Functions import test_functions


def print_menu():
    """
    Prints all the options in the console type interface.
    """
    print("----------------------------------------------------------")
    print("Write:")
    print("1.Add a vector to the repository")
    print("2.Get all vectors")
    print("3.Get a vector at a given index")
    print("4.Update a vector at a given index")
    print("5.Update a vector identified by name_id")
    print("6.Delete a vector by index")
    print("7.Delete a vector by name_id")
    print("8.Plot all vectors in a chart")
    print("15.Get the min of all vectors")
    print("19.Delete all vectors for which the product of elements is grater then a given value")
    print("23.Update the color of a vector identified by name_id")
    print("30 -Test functions")
    print("31 -Print menu")
    print("32 -Stop the program")


def start():
    """
    Start the console type interface.
    :return:
    """
    print_menu()
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    repository = VectorRepository([vector1, vector2])
    command = input(">>> ")
    while command != "0":
        if command == "31":
            print_menu()
        elif command == "1":
            try:
                name_id = int(input("Name_id:"))
                if repository.is_name_id_of_vector_already_in_repository(name_id):
                    print("There already exist this name_id in the repository.")
                    raise ValueError
                color = input("Color:")
                type_of_vector = int(input("Type_of_vector:"))
                amount = input("The amount of values to read:")
                values = []
                for i in range(int(amount)):
                    values.append(int(input(f"v[{i}]=")))
                if not verify_vector(name_id, color, type_of_vector, values):
                    raise ValueError
            except ValueError:
                print("")
            else:
                repository.add_vector(name_id, color, type_of_vector, values)
                print(repository)
                command = input(">>> ")
        elif command == "2":
            print(repository.get_all_vectors())
            command = input(">>> ")
        elif command == "3":
            index = int(input("Index:"))
            print(repository.get_vector_at_index(index))
            command = input(">>> ")
        elif command == "4":
            try:
                index = int(input("Index_id:"))
                color = input("Color:")
                type_of_vector = int(input("Type_of_vector:"))
                amount = input("The amount of values to read:")
                values = []
                for i in range(int(amount)):
                    values.append(int(input(f"v[{i}]=")))
                if not verify_vector(repository.get_vector_at_index(index).get_name_id(), color, type_of_vector,
                                     values):
                    raise ValueError
            except ValueError:
                print("")
            else:
                repository.update_vector_at_index(index, color, type_of_vector, values)
                print(repository)
                command = input(">>> ")
        elif command == "5":
            try:
                name_id = int(input("Name_id:"))
                color = input("Color:")
                type_of_vector = int(input("Type_of_vector:"))
                amount = input("The amount of values to read:")
                values = []
                for i in range(int(amount)):
                    values.append(int(input(f"v[{i}]=")))
                if not verify_vector(name_id, color, type_of_vector,
                                     values):
                    raise ValueError
            except ValueError:
                print("")
            else:
                repository.update_a_vector_identified_by_name_id(name_id, color, type_of_vector, values)
                print(repository)
                command = input(">>> ")
        elif command == "6":
            try:
                index = int(input("Index_id:"))
            except ValueError:
                print("")
            else:
                repository.delete_a_vector_by_index(index)
                print(repository)
                command = input(">>> ")
        elif command == "7":
            try:
                name_id = int(input("Name_id:"))
            except ValueError:
                print("")
            else:
                repository.delete_a_vector_by_name_id(name_id)
                print(repository)
                command = input(">>> ")
        elif command == "8":
            repository.plot_all_vectors_in_a_chart()
            command = input(">>> ")
        elif command == "15":
            print(f"The minimum of all vectors is :{repository.get_minimum_of_all_vector()}")
            command = input(">>> ")
        elif command == "19":
            try:
                value = int(input("Value:"))
            except ValueError:
                print("Plase input an integer.")
            else:
                copy = repository.get_all_vectors()
                repository.delete_all_vectors_for_which_the_product_is_greater_than_a_given_value(value)
                print("Before:", copy)
                print("After", repository.get_all_vectors())
                command = input(">>> ")
        elif command == "23":
            try:
                name_id = int(input("Name_id:"))
                if not repository.is_name_id_of_vector_already_in_repository(name_id):
                    print("There name_id doesn't exist this name_id in the repository.")
                    raise ValueError
                color = input("Color:")
                try:
                    colors = ['r', 'g', 'b', 'y', 'm']
                    ok = 0
                    for item in colors:
                        if color == item:
                            ok = 1
                    if ok == 0:
                        raise ValueError
                except ValueError:
                    print('Colors must be one of the following : r , g , b, y, m')
                    raise ValueError
            except ValueError:
                print("")
            else:
                repository.update_color_for_vector_with_name_id(name_id, color)
                print(repository)
                command = input(">>> ")
        elif command == "30":
            test_functions()
        elif command == "32":
            break
        else:
            print("Invalid command!")
            command = input(">>> ")


start()
