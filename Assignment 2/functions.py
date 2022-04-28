Score_board = [10, 20, 13, 14, 15]
Saved_list = []


def add(score_list, value):
    """
    This function Adds a grade of a new participant to the end of the array
    :param score_list:integer list representing the grates of the participants
    :param value:integer representing the grade which would be added in the list of grades
    :return: score_list:list of integers representing the scores of the participants after the modification
    """

    score_list.append(value)
    return score_list


def insert(score_list, index, value):
    """
    This function Inserts a grade of a new participant at a given index
    :param score_list:integer list representing the grates of the participants
    :param index:integer representing the index at which would be inserted the grade
    :param value:integer representing the grade which would be added in the list of grades
    :return:score_list:list of integers representing the scores of the participants after the modification
    """
    score_list.insert(index, value)
    return score_list


def f1(run):
    from P2.UI import main
    """
    This function is used to add the grade of a new participant to the array
    """
    print("-----------------------------------------------------------------------------------------")
    print('')
    print("1-add result at the end of the list")
    print("2-insert number at a given index")
    print('3-print Score_Board')
    print("4-return to menu")

    number = int(input("Choice="))
    if number == 1:
        print("Please input a value between 0 and 100")
        value = int(input('value='))
        if 0 <= value <= 100:
            l1 = add(Score_board, value)
            confirm(1, l1, run)
        else:
            print("Please give a valid value")
            f1(run)

    elif number == 2:
        print("Please input a value between 0 and 100 and an index which respects the bounds of the list")
        value = int(input('value='))
        if 0 <= value <= 100:
            index = int(input('index='))
            if 0 <= index <= len(Score_board):
                l2 = insert(Score_board, index, value)
                confirm(1, l2, run)
            else:
                print("Please give a valid index")
                f1(run)
        else:
            print("Please give a valid value")
            f1(run)

    elif number == 3:
        print("Score_board:", Score_board)
        f1(run)
    elif number == 4:
        main(run)
    else:
        print("Error , please give a valid input")
        f1(run)


def remove(score_list, index):
    """
    This function removes a grade at a given index
    :param score_list:integer list representing the grates of the participants
    :param index:integer representing the index were the grade will be remove
    :return: score_list:list of integers representing the scores of the participants after the modification
    """

    del score_list[index]

    return score_list


def remove2(score_list, from_index, to_index):
    """
    This function removes a grades from a starting index to an ending index
    :param score_list: integer list representing the grates of the participants
    :param from_index: integer representing the starting index
    :param to_index: integer representing the ending index
    :return:score_list:list of integers representing the scores of the participants after the modification
    """
    del score_list[from_index:to_index]
    return score_list


def replace(score_list, index, new_value):
    """
    This function replaces a grade at a given index
    :param score_list: integer list representing the grates of the participants
    :param index: integer representing the index at which the grade will be replaced
    :param new_value: integer representing the grade which would replace the old one
    :return: score_list:list of integers representing the scores of the participants after the modification
    """

    score_list[index] = new_value
    return score_list


def f2(run):
    from P2.UI import main
    """
    This function is used to modify the scores in the array
    """
    print("-----------------------------------------------------------------------------------------")
    print('')
    print("1-remove the element at given index")
    print("2-remove the elements between two given indexes")
    print("3-replaces the score on index with new_value")
    print('4-print Score_Board')
    print("5-return to menu")
    number = int(input("Choice="))
    if number == 1:
        print("Please input an index which respects the bounds of the list")
        index = int(input('index='))
        if 0 <= index <= len(Score_board):
            l1 = remove(Score_board, index)
            confirm(2, l1, run)
        else:
            print("Please give a valid index")
            f2(run)

    elif number == 2:
        print("Please input a starting index and and stopping index")
        starting_index = int(input('starting index='))
        if 0 <= starting_index <= len(Score_board):
            stopping_index = int(input('stopping index='))
            if 0 <= stopping_index <= len(Score_board):
                l2 = remove2(Score_board, starting_index, stopping_index)
                confirm(2, l2, run)
            else:
                print("Please give a valid stopping index")
                f2(run)
        else:
            print("Please give a valid starting index")
            f2(run)

    elif number == 3:
        print("Please input a new value which is between 0 and 100 and an index which respects the bounds of the list")
        new_value = int(input('value='))
        if 0 <= new_value <= 100:
            index = int(input('index='))
            if 0 <= index <= len(Score_board):
                l3 = replace(Score_board, index, new_value)
                confirm(2, l3, run)
            else:
                print("Please give a valid index")
                f2(run)
        else:
            print("Please give a valid value")
            f2(run)
    elif number == 4:
        print("Score_board:", Score_board)
        f2(run)
    elif number == 5:
        main(run)
    else:
        print("Error , please give a valid input")
        f2(run)


def less1(score_list, value):
    """
    This function prints the participants with their score less than a given value
    :param score_list:integer list representing the grates of the participants
    :param value:integer representing the grade which the grades of the participants will be compared to
    :return: score_list:list of integers representing the scores of the participants after the modification
    """
    l1 = []
    for item in score_list:
        if item < value:
            l1.append(item)
    return l1


def sorted1(score_list):
    """
    This function get the participants sorted by their grades
    :param score_list:integer list representing the grates of the participants
    :return:index_list:list of integers representing the index of the participants
    :return:copy_list:list of integers representing the scores of the participants sorted by their score
    """
    score_list.sort()
    print("-------------------------------------------------")
    print("The participants sorted by the their score are:")
    print(score_list)

    return score_list


def sorted2(score_list, value):
    """
    This function gets the participants with scores higher than value sorted
    :param score_list:integer list representing the grates of the participants
    :param value:integer representing the value which would be use in the comparing of the sorted grades
    :return:score_list:list of integers representing the scores of the participants after the modification
    """
    print("")
    score_list = sorted1(score_list)
    l2 = []
    for item in score_list:
        if item > value:
            l2.append(item)
    print(l2)
    return l2


def f3(run):
    from P2.UI import main
    """
    This function is used to get the participants with scores having some properties
    """
    print("-----------------------------------------------------------------------------------------")
    print('')
    print("1-get the participants with score less than value")
    print("2-get all participants sorted by their score")
    print("3-get the participants with scores higher than value sorted")
    print('4-print Score_Board')
    print("5-return to menu")
    number = int(input("Choice="))
    if number == 1:
        print("Please input a new value which is between 0 and 100")
        value = int(input('value='))
        if 0 <= value <= 100:
            l1 = less1(Score_board, value)
            print(l1)
            f3(run)
        else:
            print("Please give a valid value")
            f3(run)
    elif number == 2:
        sorted1(Score_board)
        f3(run)

    elif number == 3:
        print("Please input a new value which is between 0 and 100")
        value = int(input('value='))
        if 0 <= value <= 100:
            sorted2(Score_board, value)
            f3(run)
        else:
            print("Please give a valid value")
            f3(run)
    elif number == 4:
        print("Score_board:", Score_board)
        f3(run)
    elif number == 5:
        main(run)
    else:
        print("Error , please give a valid input")
        f3(run)


def avg1(score_list, from_index, to_index):
    """
    This function compute the average score for participants between the two given indexes
    :param score_list:integer list representing the grates of the participants
    :param from_index:integer representing the starting index
    :param to_index:integer representing the ending index
    :return:average:float number representing the average of the grades between the from_index and to_index
    """
    sum1 = 0
    number_of_elements = len(score_list[from_index:to_index])
    i = from_index
    while i <= to_index:
        sum1 = sum1 + score_list[i]
        i = i + 1

    average = sum1 / number_of_elements
    return average


def min1(score_list, from_index, to_index):
    """
    This function finds the minimum score from a starting index to a ending index
    :param score_list:integer list representing the grates of the participants
    :param from_index:integer representing the starting index
    :param to_index:integer representing the ending index
    :return:minimum:integer representing the lowest score between the starting index and ending index
    """
    minimum = score_list[from_index]
    for i in range(from_index, to_index):
        if score_list[i] < minimum:
            minimum = score_list[i]
    return minimum


def mul(score_list, value, from_index, to_index):
    """
    This function gets the score of participants between the two given index, which are multiples of a given value
    :param score_list:integer list representing the grates of the participants
    :param value:integer representing the comparing value
    :param from_index:integer representing the starting index
    :param to_index:integer representing the ending index
    :return:lis1:integer list representing the grades which are multiples of the given value
    :return:index_list:integer list of index representing the participants
    """
    list1 = []
    index_list = []
    for i in range(from_index, to_index):
        if score_list[i] % value == 0:
            index_list.append(i)
    print("Values:")
    print(list1)
    print("Participants:")
    print(index_list)

    return list1, index_list


def f4(run):
    from P2.UI import main
    """
            This function is used to get the participants with scores having some properties

    """
    print("-----------------------------------------------------------------------------------------")
    print('')
    print("1-get the average score for participants between the two given index")
    print("2-get minimum score for participants between the two given index")
    print("3-get the score of participants between the two given index, which are multiples of value")
    print('4-print Score_Board')
    print("5-return to menu")

    number = int(input("Choice="))
    if number == 1:
        print("Please input an starting index which respects the bound of the list")
        from_index = int(input('starting index='))
        if 0 <= from_index <= len(Score_board):
            print("Please input an stopping index which respects the bound of the list")
            to_index = int(input('stopping index='))
            if 0 <= from_index <= len(Score_board):
                a = avg1(Score_board, from_index, to_index)
                print(a)
                f4(run)
            else:
                print("Please give a valid stopping index")
                f4(run)
        else:
            print("Please give a valid starting index")
            f4(run)
    elif number == 2:
        print("Please input an starting index which respects the bound of the list")
        from_index = int(input('starting index='))
        if 0 <= from_index <= len(Score_board):
            print("Please input an stopping index which respects the bound of the list")
            to_index = int(input('stopping index='))
            if 0 <= to_index <= len(Score_board):
                m = min1(Score_board, from_index, to_index)
                print(m)
                f4(run)
            else:
                print("Please give a valid stopping index")
                f4(run)
        else:
            print("Please give a valid starting index")
            f4(run)
    elif number == 3:
        print("Please input value which is between 0 and 100")
        value = int(input('value='))
        if 0 <= value <= 100:
            print("Please input an starting index which respects the bound of the list")
            from_index = int(input('starting index='))
            if 0 <= from_index <= len(Score_board):
                print("Please input an stopping index which respects the bound of the list")
                to_index = int(input('stopping index='))
                if 0 <= to_index <= len(Score_board):
                    mul(Score_board, value, from_index, to_index)
                else:
                    print("Please give a valid stopping value")
                    f4(run)
            else:
                print("Please give a valid starting index")
                f4(run)
        else:
            print("Please give a valid value")
            f4(run)
    elif number == 4:
        print("Score_board:", Score_board)
        f4(run)
    elif number == 5:
        main(run)
    else:
        print("Error , please give a valid input")
        f4(run)


def filter_mul(score_list, value):
    """
    This function filters the score list such that it keep only the participants with scores multiple of value,
    removing the other participants
    :param score_list:integer list representing the grates of the participants
    :param value:integer representing the comparing value
    :return:score_list:list of integers representing the scores of the participants after the modification
    """
    l1 = []
    for item in score_list:
        if item % value == 0:
            l1.append(item)
    return l1


def filter_greater(score_list, value):
    """
    This function filters the score list such that it keep only participants with scores higher than value,
    removing the other participants
    :param score_list: integer list representing the grates of the participants
    :param value:integer representing the comparing value
    :return:score_list:list of integers representing the scores of the participants after the modification
    """
    l1 = []
    for item in score_list:
        if item > value:
            l1.append(item)
    return l1


def f5(run):
    from P2.UI import main
    """
        This function is used to filter the participants with scores having some properties

    """
    print("-----------------------------------------------------------------------------------------")
    print("1-keep only participants with scores multiple of value,  removing the other participants")
    print("2-keep only participants with scores higher than value, removing the other participants ")
    print('3-print Score_Board')
    print("4-return to menu")
    number = int(input("Choice="))
    if number == 1:
        print("Please input a value between 0 and 100")
        value = int(input('value='))
        if 0 <= value <= 100:
            l1 = filter_mul(Score_board, value)
            print(l1)
            f5(run)
        else:
            print("Please give a valid value")
            f5(run)
    elif number == 2:
        print("Please input a value between 0 and 100")
        value = int(input('value='))
        if 0 <= value <= 100:
            l2 = filter_greater(Score_board, value)
            print(l2)
            f5(run)
        else:
            print("Please give a valid value")
            f5(run)
    elif number == 3:
        print("Score_board:", Score_board)
        f5(run)
    elif number == 4:
        main(run)

    else:
        print("Error , please give a valid input")
        f5(run)


def save(score_list):
    """
    This function saves the last operation.
    :param score_list: integer list representing the current list after the applied modifications
    :return:score_list:integer list representing the saved list
    """
    global Saved_list
    Saved_list = score_list

    return score_list


def undo():
    """
    This function undo the last operation.
    :return:Save_list:integer list representing the last known list before the last modification
    """
    global Saved_list

    return Saved_list


def function_selector(i, run):
    """
    This function goes back to the previous function
    :param i: the index of the function (1-5)
    :param run:true or false representing the state of the program
    """

    if i == 1:
        f1(run)
    if i == 2:
        f2(run)
    if i == 3:
        f3(run)
    if i == 4:
        f4(run)
    if i == 5:
        f4(run)


def confirm(i, score_list, run):
    """
    This function confirms the last choice of the user.
    :param i:integer representing last function's number
    :param score_list:integer list representing the scores of the participants
    :param run:true or false representing the state of the program
    """
    print("---------------------------------------------")
    print("Save the current operation ?")
    print("Yes or not ?(y/n):", end=' ')
    command = input()
    if command == 'y':
        save(score_list)
        function_selector(i, run)
    elif command == 'n':
        undo()
        function_selector(i, run)
    else:
        print("Please enter a valid command")
        confirm(i, score_list, run)
