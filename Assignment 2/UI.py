# P2

def menu():
    """
    This function has the description of all the features offered by the program

    """
    print("----------------------------------------------------------")
    print("Write:")
    print("1 - Add the result of a new participant to the array")
    print("2 - Modify the scores in the array (as a result of appeals)")
    print("3 - Get the participants with scores having some properties")
    print("4 - Obtain different characteristics of participant")
    print("5 - Filter values")
    print("6 - Verify functions")
    print("7 - Stop the program")


def test_menu(run):
    from P2.test_functions import test_add
    from P2.test_functions import test_insert
    from P2.test_functions import test_remove
    from P2.test_functions import test_remove2
    from P2.test_functions import test_replace
    from P2.test_functions import test_less1
    from P2.test_functions import test_sorted1
    from P2.test_functions import test_sorted2
    from P2.test_functions import test_avg
    from P2.test_functions import test_min1
    from P2.test_functions import test_mul
    from P2.test_functions import test_filter_mul
    from P2.test_functions import test_filter_greater
    from P2.test_functions import test_undo
    print("-------------------------------------------------------------------------------------")
    print("Write:")
    print("1 - Verify Add_function (adds a grade of a new participant to the end of the array)")
    print("2 - Verify Insert_function (Inserts a grade of a new participant at a given index)")
    print("3 - Verify Remove_function (Removes a grade at a given index)")
    print("4 - Verify Remove2_function (Removes grades between two indexes)")
    print("5 - Verify Replace function (Replaces a value at a given index)")
    print("6 - Verify Less function (Get all participants less then a given value)")
    print("7 - Verify Sorted1 function (Get all participants sorted by their score)")
    print("8 - Verify Sorted2 function (Get all the participants with scores higher than value sorted)")
    print("9 - Verify Avg function (Get the average score for participants between the two given index)")
    print("10 - Verify Min1 function (Get the minimum value between two indexes)")
    print("11 - Verify Mul function (Get the get the score of participants between the two given index, "
          "which are multiples of value)")
    print("12 - Verify Filter_mul function (Keeps only participants with scores multiple of value,"
          " removing the other participants)")
    print("13 - Verify Filter_grater function (Keep only participants with scores higher than value,"
          " removing the other participants)")
    print("14 - Undo()")
    print("15 - Return to main menu")
    n = int(input("Choice="))
    if n == 1:
        test_add()
    elif n == 2:
        test_insert()
    elif n == 3:
        test_remove()
    elif n == 4:
        test_remove2()
    elif n == 5:
        test_replace()
    elif n == 6:
        test_less1()
    elif n == 7:
        test_sorted1()
    elif n == 8:
        test_sorted2()
    elif n == 9:
        test_avg()
    elif n == 10:
        test_min1()
    elif n == 11:
        test_mul()
    elif n == 12:
        test_filter_mul()
    elif n == 13:
        test_filter_greater()
    elif n == 14:
        test_undo()
    elif n == 15:
        command(run)

    else:
        print(ValueError)
        print("Please give a valid value")
        test_menu(run)


def command(run):
    from P2.functions import f1
    from P2.functions import f2
    from P2.functions import f3
    from P2.functions import f4
    from P2.functions import f5

    """
    This function is used to navigate between the different functions

    """
    menu()
    n = int(input("Choice="))
    if n == 1:
        f1(run)
    elif n == 2:
        f2(run)
    elif n == 3:
        f3(run)
    elif n == 4:
        f4(run)
    elif n == 5:
        f5(run)
    elif n == 6:
        test_menu(run)
    elif n == 7:
        run = False
        main(run)
    else:
        print("Please give a valid command:")
        command(run)


def main(run):
    """
    This is the main function of the program
    """
    if run:
        command(run)
