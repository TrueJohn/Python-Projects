def test_add():
    """
    This function tests the add() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    from P2.functions import add
    print("add([],3)==3?")
    if add([], 3) == [3]:
        print("Yes")
    else:
        assert add([], 3) == [3], "Mismatch"

    print("add([2],7)==[7,2]?")

    if add([2], 7) == [2, 7]:
        print("Yes")
    else:
        assert add([2], 7) == [2, 7], "Mismatch"

    print("add([1,8],9)==[1,8,7]?")

    if add([1, 8], 9) == [1, 8, 9]:
        print("Yes")
    else:
        assert add([1, 8], 9) == [1, 8, 9], "Mismatch"

    print("add([3,6,4],5)==[3,6,4,5]?")

    if add([3, 6, 4], 5) == [3, 6, 4, 5]:
        print("Yes")
    else:
        assert add([3, 6, 4], 5) == [3, 6, 4, 5], "Mismatch"

    print("add([1,2,3],4)==[4,3,1,2]?")
    if add([1, 2, 3], 4) == [4, 3, 1, 2]:
        print("Yes")
    else:
        assert add([1, 2, 3], 4) == [4, 3, 1, 2], "Mismatch"


def test_insert():
    from P2.functions import insert
    """
    This function tests the insert() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("insert([], 0, 2) == [2]?")
    if insert([], 0, 2) == [2]:
        print("Yes")
    else:
        assert insert([], 0, 2) == [2], "Mismatch"

    print("insert([1], 1, 2) == [1, 2]?")
    if insert([1], 1, 2) == [1, 2]:
        print("Yes")
    else:
        assert insert([1], 1, 2) == [1, 2], "Mismatch"

    print("insert([1, 8], 1, 7) == [1, 7, 8]?")
    if insert([1, 8], 1, 7) == [1, 7, 8]:
        print("Yes")
    else:
        assert insert([1, 8], 1, 7) == [1, 7, 8], "Mismatch"

    print("insert([3, 5, 4], 3, 7) == [3, 5, 4, 7]?")
    if insert([3, 5, 4], 3, 7) == [3, 5, 4, 7]:
        print("Yes")
    else:
        assert insert([3, 5, 4], 3, 7) == [3, 5, 4, 7], "Mismatch"

    print("insert([3, 3, 3], 0, 7) == [3, 3, 3]?")
    if insert([3, 3, 3], 0, 7) == [3, 3, 3]:
        print("Yes")
    else:
        assert insert([3, 3, 3], 0, 7) == [3, 3, 3], "Mismatch"


def test_remove():
    from P2.functions import remove
    """
    This function tests the remove() function with predefined examples
    """
    print("-------------------------------------------------------------------")

    print("remove([1 ,2 ,3], 0) == [2,3]?")
    if remove([1, 2, 3], 0) == [2, 3]:
        print("Yes")
    else:
        assert remove([1, 2, 3], 0) == [2, 3], "Mismatch"

    print("remove([8, 7, 10], 1) == [8, 10]?")
    if remove([8, 7, 10], 1) == [8, 10]:
        print("Yes")
    else:
        assert remove([8, 7, 10], 1) == [8, 10], "Mismatch"

    print("remove([4, 5, 8], 1) == [4, 8]?")
    if remove([4, 5, 8], 1) == [4, 8]:
        print("Yes")
    else:
        assert remove([4, 5, 8], 1) == [4, 8], "Mismatch"

    print("remove([3, 5, 4, 7, 5, 6], 4) == [3, 5, 4, 7, 6]?")
    if remove([3, 5, 4, 7, 5, 6], 4) == [3, 5, 4, 7, 6]:
        print("Yes")
    else:
        assert remove([3, 5, 4, 7, 5, 6], 4) == [3, 5, 4, 7, 6], "Mismatch"

    print("remove([3], 0) == [3, 3]?")
    if remove([3], 0) == [3, 3]:
        print("Yes")
    else:
        assert remove([3, 0], 1) == [3, 3], "Mismatch"


def test_remove2():
    from P2.functions import remove2
    """
    This function tests the remove2() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("remove2([4, 2, 6], 0, 1) == [6]?")
    if remove2([4, 2, 6], 0, 1) == [6]:
        print("Yes")
    else:
        print(remove2([4, 2, 6], 0, 1))
        assert remove2([4, 2, 6], 0, 1) == [6], "Mismatch"

    print("remove2([3, 9, 2], 1, 2) == [3]")
    if remove2([3, 9, 2], 1, 2) == [3]:
        print("Yes")
    else:
        assert remove2([3, 9, 2], 1, 2) == [3], "Mismatch"

    print("remove2([4, 5, 8, 3, 4, 5], 0, 5) == []?")
    if remove2([4, 5, 8, 3, 4, 5], 0, 5):
        print("Yes")
    else:
        assert remove2([4, 5, 8, 3, 4, 5], 0, 5) == [], "Mismatch"

    print("remove2([9, 5, 7, 1, 5, 8], 2, 4) == [9, 5, 8]?")
    if remove2([9, 5, 7, 1, 5, 8], 2, 4) == [9, 5, 8]:
        print("Yes")
    else:
        assert remove2([9, 5, 7, 1, 5, 8], 2, 4) == [9, 5, 8], "Mismatch"

    print("remove2([4, 6], 0, 7) == [9, 10, 4]?")
    if remove2([4, 6], 0, 7) == [9, 10, 4]:
        print("Yes")
    else:
        assert remove2([4, 6], 0, 7) == [9, 10, 4], "Mismatch"


def test_replace():
    from P2.functions import replace
    """
    This function tests the replace() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("replace([7, 9, 2], 0, 1) == [1, 9, 2]?")
    if replace([7, 9, 2], 0, 1) == [1, 9, 2]:
        print("Yes")
    else:
        assert replace([7, 9, 2], 0, 1) == [1, 9, 2], "Mismatch"

    print("replace([4, 9, 3], 1, 2) == [4, 2, 3]")
    if replace([4, 9, 3], 1, 2) == [4, 2, 3]:
        print("Yes")
    else:
        assert replace([4, 9, 3], 1, 2) == [4, 2, 3], "Mismatch"

    print("replace([4, 5, 8, 3, 4, 5], 5, 10) == [4, 5, 8, 3, 4, 10]?")
    if replace([4, 5, 8, 3, 4, 5], 5, 10) == [4, 5, 8, 3, 4, 10]:
        print("Yes")
    else:
        assert replace([4, 5, 8, 3, 4, 5], 5, 10) == [4, 5, 8, 3, 4, 10], "Mismatch"

    print("replace([7, 1, 3, 2, 7, 8], 2, 4) == [7, 1, 4, 2, 7, 8]?")
    if replace([7, 1, 3, 2, 7, 8], 2, 4) == [7, 1, 4, 2, 7, 8]:
        print("Yes")
    else:
        assert replace([7, 1, 3, 2, 7, 8], 2, 4) == [7, 1, 4, 2, 7, 8], "Mismatch"

    print("replace([4, 6], 0, 7) == [9, 10, 4]?")
    if replace([4, 6], 0, 7) == [9, 10, 4]:
        print("Yes")
    else:
        assert replace([4, 6], 0, 7) == [9, 10, 4], "Mismatch"


def test_less1():
    from P2.functions import less1
    """
    This function tests the less1() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("less1([7, 9, 2], 9) == [7, 2]?")
    if less1([7, 9, 2], 9) == [7, 2]:
        print("Yes")
    else:
        print(less1([7, 9, 2], 9))
        assert less1([7, 9, 2], 9) == [7, 2], "Mismatch"

    print("less1([4, 9, 3], 3) == []")
    if less1([4, 9, 3], 3):
        print("Yes")
    else:
        assert less1([4, 9, 3], 3) == [], "Mismatch"

    print("less1([4, 5, 8, 3, 4, 5], 6) == [4, 5, 3, 4]?")
    if less1([4, 5, 8, 3, 4, 5], 6) == [4, 5, 3, 4]:
        print("Yes")
    else:
        assert less1([4, 5, 8, 3, 4, 5], 6) == [4, 5, 3, 4], "Mismatch"

    print("less1([7, 1, 3, 2, 7, 8], 7) == [1, 3, 2]?")
    if less1([7, 1, 3, 2, 7, 8], 7) == [1, 3, 2]:
        print("Yes")
    else:
        assert less1([7, 1, 3, 2, 7, 8], 7) == [1, 3, 2], "Mismatch"

    print("less1([4, 6], 3) == [4, 6]?")
    if less1([4, 6], 3) == [4, 6]:
        print("Yes")
    else:
        assert less1([4, 6], 3) == [4, 6], "Mismatch"


def test_sorted1():
    from P2.functions import sorted1
    """
    This function tests the sorted1() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("sorted1([7, 9, 2]) == [2, 7, 9]?")
    if sorted1([7, 9, 2]) == [2, 7, 9]:
        print("Yes")
    else:
        assert sorted1([7, 9, 2]) == [2, 7, 9], "Mismatch"

    print("sorted1([4, 9, 3]) == [3, 4, 9]")
    if sorted1([4, 9, 3]) == [3, 4, 9]:
        print("Yes")
    else:
        assert sorted1([4, 9, 3]) == [3, 4, 9], "Mismatch"

    print("sorted1([4, 5, 8, 3, 4, 5]) == [3, 4, 4, 5, 5, 8]?")
    if sorted1([4, 5, 8, 3, 4, 5]) == [3, 4, 4, 5, 5, 8]:
        print("Yes")
    else:
        assert sorted1([4, 5, 8, 3, 4, 5]) == [3, 4, 4, 5, 5, 8], "Mismatch"

    print("sorted1([7, 1, 3, 2, 7, 8]) == [1, 2, 3, 7, 7, 8]?")
    if sorted1([7, 1, 3, 2, 7, 8]) == [1, 2, 3, 7, 7, 8]:
        print("Yes")
    else:
        assert sorted1([7, 1, 3, 2, 7, 8]) == [1, 2, 3, 7, 7, 8], "Mismatch"

    print("sorted1([4, 6]) == [6, 4]?")
    if sorted1([4, 6]) == [6, 4]:
        print("Yes")
    else:
        assert sorted1([4, 6]) == [6, 4], "Mismatch"


def test_sorted2():
    from P2.functions import sorted2
    """
    This function tests the sorted2() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("sorted2([7, 9, 2], 3) == [7, 9]?")
    if sorted2([7, 9, 2], 3) == [7, 9]:
        print("Yes")
    else:
        assert sorted2([7, 9, 2], 3) == [7, 9], "Mismatch"

    print("sorted2([4, 9, 3], 4) == [9]")
    if sorted2([4, 9, 3], 4) == [9]:
        print("Yes")
    else:
        assert sorted2([4, 9, 3], 4) == [9], "Mismatch"

    print("sorted2([4, 5, 8, 3, 4, 5], 4) == [5, 5, 8]?")
    if sorted2([4, 5, 8, 3, 4, 5], 4) == [5, 5, 8]:
        print("Yes")
    else:
        assert sorted2([4, 5, 8, 3, 4, 5], 4) == [5, 5, 8], "Mismatch"

    print("sorted2([7, 1, 3, 2, 7, 8], 4) == [7, 7, 8]?")
    if sorted2([7, 1, 3, 2, 7, 8], 4) == [7, 7, 8]:
        print("Yes")
    else:
        assert sorted2([7, 1, 3, 2, 7, 8], 4) == [7, 7, 8], "Mismatch"

    print("sorted2([4, 6], 9) == [4, 6]?")
    if sorted2([4, 6], 9) == [4, 6]:
        print("Yes")
    else:
        assert sorted2([4, 6], 9) == [4, 6], "Mismatch"


def test_avg():
    from P2.functions import avg
    """
    This function tests the avg() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("avg([7, 9, 2], 0, 2) == 6?")
    if avg([7, 9, 2], 0, 2) == 6:
        print("Yes")
    else:
        assert avg([7, 9, 2], 0, 2) == 6, "Mismatch"

    print("avg([4, 9, 3], 0, 3) == 5.33")
    if avg([4, 9, 3], 0, 3) == 5.33:
        print("Yes")
    else:
        assert avg([4, 9, 3], 0, 3) == 5.33, "Mismatch"

    print("avg([4, 5, 8, 3, 4, 5], 0, 3) == 5.25?")
    if avg([4, 5, 8, 3, 4, 5], 0, 3) == 5.25:
        print("Yes")
    else:
        assert avg([4, 5, 8, 3, 4, 5], 0, 3) == 5.25, "Mismatch"

    print("avg([7, 1, 3, 2, 7, 8, 3], 0, 7) == 4.57?")
    if avg([7, 1, 3, 2, 7, 8, 3], 0, 7) == 4.57:
        print("Yes")
    else:
        assert avg([7, 1, 3, 2, 7, 8, 3], 0, 7) == 4.57, "Mismatch"

    print("avg([5, 6], 0, 1) == 2?")
    if avg([5, 6], 0, 1) == 2:
        print("Yes")
    else:
        assert avg([5, 6], 0, 1) == 2, "Mismatch"


def test_min1():
    from P2.functions import min1
    """
    This function tests the min1() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("min1([7, 9, 2], 0, 2) == 2?")
    if min1([7, 9, 2], 0, 2) == 2:
        print("Yes")
    else:
        assert min1([7, 9, 2], 0, 2) == 2, "Mismatch"

    print("min1([4, 9, 3], 0, 3) == 3")
    if min1([4, 9, 3], 0, 3) == 3:
        print("Yes")
    else:
        assert min1([4, 9, 3], 0, 3) == 3, "Mismatch"

    print("min1([4, 5, 8, 3, 4, 5], 0, 3) == 3?")
    if min1([4, 5, 8, 3, 4, 5], 0, 3) == 3:
        print("Yes")
    else:
        assert min1([4, 5, 8, 3, 4, 5], 0, 3) == 3, "Mismatch"

    print("min1([7, 1, 3, 2, 7, 8, 3], 0, 7) == 1?")
    if min1([7, 1, 3, 2, 7, 8, 3], 0, 7) == 1:
        print("Yes")
    else:
        assert min1([7, 1, 3, 2, 7, 8, 3], 0, 7) == 1, "Mismatch"

    print("min1([2, 3, 9], 0, 1) == 9?")
    if min1([2, 3, 9], 0, 1) == 9:
        print("Yes")
    else:
        assert min1([2, 3, 9], 0, 1) == 9, "Mismatch"


def test_mul():
    from P2.functions import mul
    """
    This function tests the mul() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("mul([7, 9, 2], 2, 0, 2) == [2]?")
    if mul([7, 9, 2], 2, 0, 2) == [2]:
        print("Yes")
    else:
        assert mul([7, 9, 2], 2, 0, 2) == [2], "Mismatch"

    print("mul([4, 9, 3], 2, 0, 3) == [4]")
    if mul([4, 9, 3], 2, 0, 3) == [4]:
        print("Yes")
    else:
        assert mul([4, 9, 3], 2, 0, 3) == [4], "Mismatch"

    print("mul([4, 5, 8, 3, 4, 5], 4, 0, 3) == [4, 8, 4]?")
    if mul([4, 5, 8, 3, 4, 5], 4, 0, 3) == [4, 8, 4]:
        print("Yes")
    else:
        assert mul([4, 5, 8, 3, 4, 5], 4, 0, 3) == [4, 8, 4], "Mismatch"

    print("mul([7, 1, 3, 2, 7, 8, 3], 3, 1, 5) == [3]?")
    if mul([7, 1, 3, 2, 7, 8, 3], 3, 1, 5) == [3]:
        print("Yes")
    else:
        assert mul([7, 1, 3, 2, 7, 8, 3], 3, 1, 5) == [3], "Mismatch"

    print("mul([2, 3, 9], 2, 0, 1) == [2]?")
    if mul([2, 3, 9], 2, 0, 1) == [2]:
        print("Yes")
    else:
        assert mul([2, 3, 9], 2, 0, 1) == [2], "Mismatch"


def test_filter_mul():
    from P2.functions import filter_mul
    """
    This function tests the filter_mul() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("filter_mul([7, 9, 2], 2) == [2]")
    if filter_mul([7, 9, 2], 2) == [2]:
        print("Yes")
    else:
        assert filter_mul([7, 9, 2], 2) == [2], "Mismatch"

    print("filter_mul([4, 9, 3], 3 ) == [9, 3]")
    if filter_mul([4, 9, 3], 3) == [9, 3]:
        print("Yes")
    else:
        assert filter_mul([4, 9, 3], 3) == [9, 3], "Mismatch"

    print("filter_mul([4, 5, 8, 3, 4, 5], 4) == [4, 8, 4]?")
    if filter_mul([4, 5, 8, 3, 4, 5], 4) == [4, 8, 4]:
        print("Yes")
    else:
        assert filter_mul([4, 5, 8, 3, 4, 5], 4) == [4, 8, 4], "Mismatch"

    print("filter_mul([7, 1, 3, 2, 7, 8, 3], 3) == [3, 3]?")
    if filter_mul([7, 1, 3, 2, 7, 8, 3], 3) == [3, 3]:
        print("Yes")
    else:
        assert filter_mul([7, 1, 3, 2, 7, 8, 3], 3) == [3, 3], "Mismatch"

    print("filter_mul([2, 3, 9], 2) == [3, 9]?")
    if filter_mul([2, 3, 9], 2) == [3, 9]:
        print("Yes")
    else:
        assert filter_mul([2, 3, 9], 2) == [3, 9], "Mismatch"


def test_filter_greater():
    from P2.functions import filter_greater
    """
    This function tests the filter_grater() function with predefined examples
    """
    print("-------------------------------------------------------------------")
    print("filter_grater([7, 9, 2], 2) == [7, 9]")
    if filter_greater([7, 9, 2], 2) == [7, 9]:
        print("Yes")
    else:
        assert filter_greater([7, 9, 2], 2) == [7, 9], "Mismatch"

    print("filter_greater([4, 9, 3], 3) == [4, 9]")
    if filter_greater([4, 9, 3], 3) == [4, 9]:
        print("Yes")
    else:
        assert filter_greater([4, 9, 3], 3) == [4, 9], "Mismatch"

    print("filter_greater([4, 5, 8, 3, 4, 5], 4) == [5, 8, 5]?")
    if filter_greater([4, 5, 8, 3, 4, 5], 4) == [5, 8, 5]:
        print("Yes")
    else:
        assert filter_greater([4, 5, 8, 3, 4, 5], 4) == [5, 8, 5], "Mismatch"

    print("filter_greater([7, 1, 3, 2, 7, 8, 3], 3) == [7, 7, 8]?")
    if filter_greater([7, 1, 3, 2, 7, 8, 3], 3) == [7, 7, 8]:
        print("Yes")
    else:
        assert filter_greater([7, 1, 3, 2, 7, 8, 3], 3) == [7, 7, 8], "Mismatch"

    print("filter_greater([2, 3, 9], 2) == [2]?")
    if filter_greater([2, 3, 9], 2) == [2]:
        print("Yes")
    else:
        assert filter_greater([2, 3, 9], 2) == [2], "Mismatch"


def test_undo():
    """
    The undo() function can be verify by running the program because it's using a global last-saved list
    """
    print("Please verify the undo() function in the program.")
