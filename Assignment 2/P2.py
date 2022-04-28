Score_board = []
Run = True


def Menu():
    """
    This function has the description of all the function

    """
    print("Write:")
    print("1 - Add the result of a new participant to the array")
    print("2 - Modify the scores in the array (as a result of appeals)")
    print("5 - Stop the program")


def Command():
    """
    This function is used to navigate between the different functions

    """
    n = int(input("Choice="))
    if n == 1:
        f1()
    elif n == 2:
        f2()
    elif n == 5:
        global Run
        Run = False
    else:
        print("Please give a valid command:")
        Command()


def add(score_list, value):
    """

    :param score_list:list
    :param value:integer
    :return: add a value at the end of the list
    """
    score_list.append(value)


def insert(score_list, index, value):
    """

    :param score_list:list
    :param index:integer
    :param value:integer
    :return: add a value at a given index
    """
    score_list.insert(index, value)


def f1():
    """
    This function is used to add the result of a new participant to the array

    """
    print("1-add result at the end of the list")
    print("2-insert number at a given index")
    print("3-return to menu")
    number = int(input("Choice="))
    if number == 1:
        print("Please input a value")
        value = int(input('value='))
        add(Score_board, value)
        print("The scoreboard array is [", *Score_board, "], make another operation?(y/n)")
    elif number == 2:
        print("Please input a value and an index")
        value = int(input('value='))
        index = int(input('index='))
        insert(Score_board, index, value)
        print("The scoreboard array is [", *Score_board, "], make another operation?(y/n)")
    elif number == 3:
        Main()
    else:
        input("error please try again")

    vf(1)


def remove(score_list, index):
    """
    :param score_list:
    :param index:
    :return: removes an element at given index
    """
    copy = score_list[index:]
    del score_list[index]
    score_list = score_list + copy


def remove2(score_list, from_index, index):
    """

    :param score_list: list
    :param from_index: integer
    :param index: integer
    :return: removes elements between the two given index
    """
    del score_list[from_index:index]


def replace(score_list, index, new_value):
    """

    :param score_list: list
    :param index: integer
    :param new_value: integer
    :return: replaces the score on a given index with a new_value
    """

    score_list[index] = new_value


def f2():
    """
        This function is used to modify the scores in the array

        """
    print("1-remove the element at given index")
    print("2-remove the elements between two given indexes")
    print("3-replaces the score on index with new_value")
    number = int(input("Choice="))
    if number == 1:
        print("Please input an index")
        index = int(input('index='))
        remove(Score_board, index)
        print("The scoreboard array is [", *Score_board, "], make another operation?(y/n)")
    elif number == 2:
        print("Please input a starting index and and stopping index")
        starting_index = int(input('starting index='))
        stopping_index = int(input('stopping index='))
        remove2(Score_board, starting_index, stopping_index)
        print("The scoreboard array is [", *Score_board, "], make another operation?(y/n)")
    elif number == 3:
        print("Please input an index")
        new_value = int(input('value='))
        index = int(input('index='))
        replace(Score_board, index, new_value)
        print("The scoreboard array is [", *Score_board, "], make another operation?(y/n)")
    elif number == 4:
        Main()
    else:
        input("error please try again")



    vf(2)


def vf(i):
    """
    This function verifies if a command is valid

    """
    verify = input("Choice=")
    if verify == 'y':
        if i == 1:
            f1()
        elif i == 2:
            f2()
    elif verify == 'n':
        Main()
    else:
        print("Please give a valid command:")
        vf()


def Main():
    """
    This is the main function of the program
    """

    while Run == True:
        try:
            Menu()
            Command()
        except:
            print("ERROR: INVALID COMMAND")


Main()
