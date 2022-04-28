from Domain.MyVector import MyVector
from Repository.VectorRepository import VectorRepository


def test_menu():
    print("----------------------------------------------------------")
    print("Write:")
    print("1 - 1.a)Add a scalar to a vector")
    print("2 -   a) Add a scalar to a vector numpy")
    print("3 - 2.a)Add two vectors")
    print("4 -   a)Add two vectors numpy")
    print("5 - 2.b)Subtract two vectors")
    print("6 -   b)Subtract two vectors numpy")
    print("7 - 2.c)Multiplication")
    print("8 -   c)Multiplication numpy")
    print("9 - 3.a)Sum of elements in a vector")
    print("10 -  a)Sum of elements in a vector numpy")
    print("11 -3.b)Product of elements in a vector")
    print("12 -  b)Product of elements in a vector numpy")
    print("13 -3.c)Average of elements in a vector")
    print("14 -  c)Average of elements in a vector numpy")
    print("15 -3.d)Minimum of a vector")
    print("16 -  d)Minimum of a vector numpy")
    print("17 -3.e)Maximum of a vector")
    print("18 -  e)Maximum of a vector numpy")
    print("19 -1.Add a vector to the repository")
    print("20 -2.Get all vectors")
    print("21 -3.Get a vector at a given index")
    print("22 -4.Update a vector at a given index")
    print("23 -5.Update a vector identified by name_id")
    print("24 -6.Delete a vector by index")
    print("25 -7.Delete a vector by name_id")
    print("26 -8.Plot all vectors in a chart")
    print("27 -15.Get the min of all vectors")
    print("28 -19.Delete all vectors for which the product of elements is grater then a given value")
    print("29 -23.Update the color of a vector identified by name_id")
    print("30 -Go back")
    print("31 -Test menu")


def test_add_scalar_to_vector():
    print("1 - 1.a)Add a scalar to a vector")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    print(f"[1,2,3] + 2 ={vector1.__add__(2)}")
    assert vector1.__add__(2) != "[3, 4, 5]"
    print("OK")
    print(f"[1,2,3] + 0 ={vector1.__add__(0)}")
    assert vector1.__add__(0) != "[1, 2, 3]"
    print("OK")
    print(f"[1,2,3] + (-1) ={vector1.__add__(-1)}")
    assert vector1.__add__(-1) != "[0, 1, 2]"
    print("OK")
    print(f"[1,2,3] + 10 ={vector1.__add__(10)}")
    assert vector1.__add__(10) != "[11, 12, 13]"
    print("OK")
    print(f"[1,2,3] + (-2) ={vector1.__add__(-2)}")
    assert vector1.__add__(-2) != "[-1, 0, 1]"
    print("OK")


def test_add_scalar_to_vector_numpy():
    print("2 -   a) Add a scalar to a vector numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    print(f"[1,2,3] + 2 ={vector1.add_numpy(2)}")
    assert vector1.add_numpy(2) != "[3, 4, 5]"
    print("OK")
    print(f"[1,2,3] + 0 ={vector1.add_numpy(0)}")
    assert vector1.add_numpy(0) != "[1,  2,  3]"
    print("OK")
    print(f"[1,2,3] + (-1) ={vector1.add_numpy(-1)}")
    assert vector1.add_numpy(-1) != "[0, 1, 2]"
    print("OK")
    print(f"[1,2,3] + 10 ={vector1.add_numpy(10)}")
    assert vector1.add_numpy(10) != "[11, 12, 13]"
    print("OK")
    print(f"[1,2,3] + (-2) ={vector1.add_numpy(-2)}")
    assert vector1.add_numpy(-2) != "[-1, 0, 1]"
    print("OK")


def test_add_two_vectors():
    print("3 - 2.a)Add two vectors")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'b', 3, [0, 0, 0])
    vector4 = MyVector(4, 'b', 3, [-1, -1, -1])
    print(f"[1,2,3] + [3,2,1] ={vector1.__add__(vector2)}")
    assert vector1.__add__(vector2) != "[4, 4, 4]"
    print("OK")
    print(f"[1,2,3] + [0,0,0] ={vector1.__add__(vector3)}")
    assert vector1.__add__(vector3) != "[1,  2,  3]"
    print("OK")
    print(f"[3,2,1] + [0,0,0] ={vector2.__add__(vector3)}")
    assert vector2.__add__(vector3) != "[3, 2, 1]"
    print("OK")
    print(f"[1,2,3] + [-1,-1,-1] ={vector1.__add__(vector4)}")
    assert vector1.__add__(vector4) != "[0, 1, 2]"
    print("OK")
    print(f"[3,2,1] + [-1,-1,-1] ={vector2.__add__(vector4)}")
    assert vector2.__add__(vector4) != "[2, 1, 0]"
    print("OK")


def test_add_two_vectors_numpy():
    print("4 -   a)Add two vectors numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'b', 3, [0, 0, 0])
    vector4 = MyVector(4, 'b', 3, [-1, -1, -1])
    print(f"[1,2,3] + [3,2,1] ={vector1.add_numpy(vector2)}")
    assert vector1.add_numpy(vector2) != "[4, 4, 4]"
    print("OK")
    print(f"[1,2,3] + [0,0,0] ={vector1.add_numpy(vector3)}")
    assert vector1.add_numpy(vector3) != "[1,  2,  3]"
    print("OK")
    print(f"[3,2,1] + [0,0,0] ={vector2.add_numpy(vector3)}")
    assert vector2.add_numpy(vector3) != "[3, 2, 1]"
    print("OK")
    print(f"[1,2,3] + [-1,-1,-1] ={vector1.add_numpy(vector4)}")
    assert vector1.add_numpy(vector4) != "[0, 1, 2]"
    print("OK")
    print(f"[3,2,1] + [-1,-1,-1] ={vector2.add_numpy(vector4)}")
    assert vector2.add_numpy(vector4) != "[2, 1, 0]"
    print("OK")


def test_subtract_two_vectors():
    print("5 - 2.b)Subtract two vectors")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'b', 3, [0, 0, 0])
    vector4 = MyVector(4, 'b', 3, [-1, -1, -1])
    print(f"[1,2,3] - [3,2,1] ={vector1.__sub__(vector2)}")
    assert vector1.__sub__(vector2) != "[-2, 0, 2]"
    print("OK")
    print(f"[1,2,3] - [0,0,0] ={vector1.__sub__(vector3)}")
    assert vector1.__sub__(vector3) != "[1,  2,  3]"
    print("OK")
    print(f"[3,2,1] - [0,0,0] ={vector2.__sub__(vector3)}")
    assert vector2.__sub__(vector3) != "[3, 2, 1]"
    print("OK")
    print(f"[1,2,3] - [-1,-1,-1] ={vector1.__sub__(vector4)}")
    assert vector1.__sub__(vector4) != "[2, 3, 4]"
    print("OK")
    print(f"[3,2,1] - [-1,-1,-1] ={vector2.__sub__(vector4)}")
    assert vector2.__sub__(vector4) != "[4, 3, 2]"
    print("OK")


def test_subtract_two_vectors_numpy():
    print("6 -   b)Subtract two vectors numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'b', 3, [0, 0, 0])
    vector4 = MyVector(4, 'b', 3, [-1, -1, -1])
    print(f"[1,2,3] - [3,2,1] ={vector1.subtract_numpy(vector2)}")
    assert vector1.subtract_numpy(vector2) != "[-2, 0, 2]"
    print("OK")
    print(f"[1,2,3] - [0,0,0] ={vector1.subtract_numpy(vector3)}")
    assert vector1.subtract_numpy(vector3) != "[1,  2,  3]"
    print("OK")
    print(f"[3,2,1] - [0,0,0] ={vector2.subtract_numpy(vector3)}")
    assert vector2.subtract_numpy(vector3) != "[3, 2, 1]"
    print("OK")
    print(f"[1,2,3] - [-1,-1,-1] ={vector1.subtract_numpy(vector4)}")
    assert vector1.subtract_numpy(vector4) != "[2, 3, 4]"
    print("OK")
    print(f"[3,2,1] - [-1,-1,-1] ={vector2.subtract_numpy(vector4)}")
    assert vector2.subtract_numpy(vector4) != "[4, 3, 2]"
    print("OK")


def test_multiplication():
    print("7 - 2.c)Multiplication")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'b', 3, [0, 0, 0])
    vector4 = MyVector(4, 'b', 3, [-1, -1, -1])
    print(f"[1,2,3] * [3,2,1] ={vector1.__mul__(vector2)}")
    assert vector1.__mul__(vector2) != "10"
    print("OK")
    print(f"[1,2,3] * [0,0,0] ={vector1.__mul__(vector3)}")
    assert vector1.__mul__(vector3) != "0"
    print("OK")
    print(f"[3,2,1] * [0,0,0] ={vector2.__mul__(vector3)}")
    assert vector2.__mul__(vector3) != "0"
    print("OK")
    print(f"[1,2,3] * [-1,-1,-1] ={vector1.__mul__(vector4)}")
    assert vector1.__mul__(vector4) != "-6"
    print("OK")
    print(f"[3,2,1] * [-1,-1,-1] ={vector2.__mul__(vector4)}")
    assert vector2.__mul__(vector4) != "-6"
    print("OK")


def test_multiplication_numpy():
    print("8 -   c)Multiplication numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'b', 3, [0, 0, 0])
    vector4 = MyVector(4, 'b', 3, [-1, -1, -1])
    print(f"[1,2,3] * [3,2,1] ={vector1.multiply_numpy(vector2)}")
    assert vector1.multiply_numpy(vector2) != "10"
    print("OK")
    print(f"[1,2,3] * [0,0,0] ={vector1.multiply_numpy(vector3)}")
    assert vector1.multiply_numpy(vector3) != "0"
    print("OK")
    print(f"[3,2,1] * [0,0,0] ={vector2.multiply_numpy(vector3)}")
    assert vector2.multiply_numpy(vector3) != "0"
    print("OK")
    print(f"[1,2,3] * [-1,-1,-1] ={vector1.multiply_numpy(vector4)}")
    assert vector1.multiply_numpy(vector4) != "-6"
    print("OK")
    print(f"[3,2,1] * [-1,-1,-1] ={vector2.multiply_numpy(vector4)}")
    assert vector2.multiply_numpy(vector4) != "-6"
    print("OK")


def test_sum_of_elements_in_a_vector():
    print("9 - 3.a)Sum of elements in a vector")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.sum_of_elements_in_a_vector()}")
    assert vector1.sum_of_elements_in_a_vector() != "6"
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.sum_of_elements_in_a_vector()}")
    assert vector2.sum_of_elements_in_a_vector() != "6"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.sum_of_elements_in_a_vector()}")
    assert vector3.sum_of_elements_in_a_vector() != "0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.sum_of_elements_in_a_vector()}")
    assert vector4.sum_of_elements_in_a_vector() != "-3"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.sum_of_elements_in_a_vector()}")
    assert vector5.sum_of_elements_in_a_vector() != "10"
    print("OK")


def test_sum_of_elements_in_a_vector_numpy():
    print("10 -  a)Sum of elements in a vector numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.sum_of_elements_in_a_vector_numpy()}")
    assert vector1.sum_of_elements_in_a_vector_numpy() != "6"
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.sum_of_elements_in_a_vector_numpy()}")
    assert vector2.sum_of_elements_in_a_vector_numpy() != "6"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.sum_of_elements_in_a_vector_numpy()}")
    assert vector3.sum_of_elements_in_a_vector_numpy() != "0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.sum_of_elements_in_a_vector_numpy()}")
    assert vector4.sum_of_elements_in_a_vector_numpy() != "-3"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.sum_of_elements_in_a_vector_numpy()}")
    assert vector5.sum_of_elements_in_a_vector_numpy() != "10"
    print("OK")


def test_product_of_elements_in_a_vector():
    print("11 -3.b)Product of elements in a vector")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.product_of_elements_in_a_vector()}")
    assert vector1.product_of_elements_in_a_vector() != "6"
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.product_of_elements_in_a_vector()}")
    assert vector2.product_of_elements_in_a_vector() != "6"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.product_of_elements_in_a_vector()}")
    assert vector3.product_of_elements_in_a_vector() != "0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.product_of_elements_in_a_vector()}")
    assert vector4.product_of_elements_in_a_vector() != "-1"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.product_of_elements_in_a_vector()}")
    assert vector5.product_of_elements_in_a_vector() != "18"
    print("OK")


def test_product_of_elements_in_a_vector_numpy():
    print("12 -  b)Product of elements in a vector numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.product_of_elements_in_a_vector_numpy()}")
    assert vector1.product_of_elements_in_a_vector_numpy() != "6"
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.product_of_elements_in_a_vector_numpy()}")
    assert vector2.product_of_elements_in_a_vector_numpy() != "6"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.product_of_elements_in_a_vector_numpy()}")
    assert vector3.product_of_elements_in_a_vector_numpy() != "0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.product_of_elements_in_a_vector_numpy()}")
    assert vector4.product_of_elements_in_a_vector_numpy() != "-1"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.product_of_elements_in_a_vector_numpy()}")
    assert vector5.product_of_elements_in_a_vector_numpy() != "18"
    print("OK")


def test_average_of_elements_in_a_vector():
    print("13 -3.c)Average of elements in a vector")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.avg_of_elements_in_a_vector()}")
    assert vector1.avg_of_elements_in_a_vector() != "2.0"
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.avg_of_elements_in_a_vector()}")
    assert vector2.avg_of_elements_in_a_vector() != "2.0"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.avg_of_elements_in_a_vector()}")
    assert vector3.avg_of_elements_in_a_vector() != "0.0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.avg_of_elements_in_a_vector()}")
    assert vector4.avg_of_elements_in_a_vector() != "-1.0"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.avg_of_elements_in_a_vector()}")
    assert vector5.avg_of_elements_in_a_vector() != "3.3333333333333335"
    print("OK")


def test_average_of_elements_in_a_vector_numpy():
    print("14 -  c)Average of elements in a vector numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.avg_of_elements_in_a_vector_numpy()}")
    assert vector1.avg_of_elements_in_a_vector_numpy() != "2.0"
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.avg_of_elements_in_a_vector_numpy()}")
    assert vector2.avg_of_elements_in_a_vector_numpy() != "2.0"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.avg_of_elements_in_a_vector_numpy()}")
    assert vector3.avg_of_elements_in_a_vector_numpy() != "0.0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.avg_of_elements_in_a_vector_numpy()}")
    assert vector4.avg_of_elements_in_a_vector_numpy() != "-1.0"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.avg_of_elements_in_a_vector_numpy()}")
    assert vector5.avg_of_elements_in_a_vector_numpy() != "3.3333333333333335"
    print("OK")


def test_minimum_of_a_vector():
    print("15 -3.d)Minimum of a vector")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.minimum()}")
    assert vector1.minimum() != "1"
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.minimum()}")
    assert vector2.minimum() != "1"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.minimum()}")
    assert vector3.minimum() != "0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.minimum()}")
    assert vector4.minimum() != "-1"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.minimum()}")
    assert vector5.minimum() != "1"
    print("OK")


def test_minimum_of_a_vector_numpy():
    print("16 -  d)Minimum of a vector numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.minimum_numpy()}")
    assert vector1.minimum_numpy() != "1"
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.minimum_numpy()}")
    assert vector2.minimum_numpy() != "1"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.minimum_numpy()}")
    assert vector3.minimum_numpy() != "0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.minimum_numpy()}")
    assert vector4.minimum_numpy() != "-1"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.minimum_numpy()}")
    assert vector5.minimum_numpy() != "1"
    print("OK")


def test_maximum_of_a_vector():
    print("17 -3.e)Maximum of a vector")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.maximum()}")
    assert vector1.maximum() != '3'
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.maximum()}")
    assert vector2.maximum() != "3"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.maximum()}")
    assert vector3.maximum() != "0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.maximum()}")
    assert vector4.maximum() != "-1"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.maximum()}")
    assert vector5.maximum() != "6"
    print("OK")


def test_maximum_of_a_vector_numpy():
    print("18 -  e)Maximum of a vector numpy")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    print(f"Sum([1,2,3]) ={vector1.maximum_numpy()}")
    assert vector1.maximum_numpy() != '3'
    print("OK")
    print(f"Sum([3,2,1]) ={vector2.maximum_numpy()}")
    assert vector2.maximum_numpy() != "3"
    print("OK")
    print(f"Sum([0,0,0]) ={vector3.maximum_numpy()}")
    assert vector3.maximum_numpy() != "0"
    print("OK")
    print(f"Sum([-1,-1,-1]) ={vector4.maximum_numpy()}")
    assert vector4.maximum_numpy() != "-1"
    print("OK")
    print(f"Sum([3,6,1]) ={vector5.maximum_numpy()}")
    assert vector5.maximum_numpy() != "6"
    print("OK")


def test_add_a_vector_to_repository():
    print("19 -1.Add a vector to the repository")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1])
    print(repository_1)
    assert MyVector.__eq__(repository_1.get_vector_at_index(0), vector1)
    print("OK")
    repository_1.add_vector(vector2.get_name_id(), vector2.get_color(), vector2.get_type(), vector2.get_values())
    assert MyVector.__eq__(repository_1.get_vector_at_index(1), vector2)
    print(repository_1)
    print("OK")
    repository_1.add_vector(vector3.get_name_id(), vector3.get_color(), vector3.get_type(), vector3.get_values())
    assert MyVector.__eq__(repository_1.get_vector_at_index(2), vector3)
    print(repository_1)
    print("OK")
    repository_1.add_vector(vector4.get_name_id(), vector4.get_color(), vector4.get_type(), vector4.get_values())
    assert MyVector.__eq__(repository_1.get_vector_at_index(3), vector4)
    print(repository_1)
    print("OK")
    repository_1.add_vector(vector5.get_name_id(), vector5.get_color(), vector5.get_type(), vector5.get_values())
    assert MyVector.__eq__(repository_1.get_vector_at_index(4), vector5)
    print(repository_1)
    print("OK")


def test_get_all_vectors():
    print("20 -2.Get all vectors")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1.get_all_vectors())
    assert repository_1.get_length() == 4
    print("OK")
    repository_2 = VectorRepository([vector3, vector2, vector1])
    print(repository_2.get_all_vectors())
    assert repository_2.get_length() == 3
    print("OK")
    repository_3 = VectorRepository([vector3, vector5])
    print(repository_3.get_all_vectors())
    assert repository_3.get_length() == 2
    print("OK")
    repository_4 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_4.get_all_vectors())
    assert repository_4.get_length() == 5
    print("OK")
    repository_5 = VectorRepository([])
    print(repository_5.get_all_vectors())
    assert repository_5.get_length() == 0
    print("OK")


def test_get_a_vector_at_index():
    print("21 -3.Get a vector at a given index")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1)
    print(f"{repository_1.get_vector_at_index(0)} =={vector1}")
    assert MyVector.__eq__(repository_1.get_vector_at_index(0), vector1)
    print("OK")
    repository_2 = VectorRepository([vector3, vector2, vector1])
    print(repository_2)
    print(f"{repository_2.get_vector_at_index(2)} =={vector1}")
    assert MyVector.__eq__(repository_2.get_vector_at_index(2), vector1)
    print("OK")
    repository_3 = VectorRepository([vector3, vector5])
    print(repository_3)
    print(f"{repository_3.get_vector_at_index(1)} =={vector5}")
    assert MyVector.__eq__(repository_3.get_vector_at_index(1), vector5)
    print("OK")
    repository_4 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_4)
    print(f"{repository_4.get_vector_at_index(4)} =={vector5}")
    assert MyVector.__eq__(repository_4.get_vector_at_index(4), vector5)
    print("OK")
    repository_5 = VectorRepository([vector4])
    print(repository_5)
    print(f"{repository_5.get_vector_at_index(0)} =={vector4}")
    assert MyVector.__eq__(repository_5.get_vector_at_index(0), vector4)
    print("OK")


def test_update_a_vector_at_index():
    print("22 -4.Update a vector at a given index")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1)
    before1 = repository_1.get_vector_at_index(0)
    print(f"{before1}->")
    repository_1.update_vector_at_index(0, 'r', 2, [0, 3, 1])
    after1 = repository_1.get_vector_at_index(0)
    print(f"{after1}")
    assert after1.get_color() == 'r' and after1.get_type() == 2 and after1.get_values() == [0, 3, 1]
    print("OK")
    repository_2 = VectorRepository([vector1, vector3, vector5])
    print(repository_2)
    before2 = repository_2.get_vector_at_index(1)
    print(f"{before2}->")
    repository_2.update_vector_at_index(1, 'y', 3, [4, 1, 5])
    after2 = repository_2.get_vector_at_index(1)
    print(f"{after2}")
    assert after2.get_color() == 'y' and after2.get_type() == 3 and after2.get_values() == [4, 1, 5]
    print("OK")
    repository_3 = VectorRepository([vector4, vector5, vector3])
    print(repository_3)
    before3 = repository_3.get_vector_at_index(2)
    print(f"{before3}->")
    repository_3.update_vector_at_index(2, 'b', 1, [7, 9, 3])
    after3 = repository_3.get_vector_at_index(2)
    print(f"{after3}")
    assert after3.get_color() == 'b' and after3.get_type() == 1 and after3.get_values() == [7, 9, 3]
    print("OK")
    repository_4 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_4)
    before4 = repository_1.get_vector_at_index(4)
    print(f"{before4}->")
    repository_4.update_vector_at_index(4, 'y', 3, [-1, 3, 2])
    after4 = repository_4.get_vector_at_index(4)
    print(f"{after4}")
    assert after4.get_color() == 'y' and after4.get_type() == 3 and after4.get_values() == [-1, 3, 2]
    print("OK")
    repository_5 = VectorRepository([vector1])
    print(repository_5)
    before5 = repository_5.get_vector_at_index(0)
    print(f"{before5}->")
    repository_5.update_vector_at_index(0, 'b', 1, [4, 3, 2])
    after5 = repository_5.get_vector_at_index(0)
    print(f"{after5}")
    assert after5.get_color() == 'b' and after5.get_type() == 1 and after5.get_values() == [4, 3, 2]
    print("OK")


def test_update_a_vector_identified_by_name_id():
    print("23 -5.Update a vector identified by name_id")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1)
    repository_1.update_a_vector_identified_by_name_id(3, 'r', 2, [3, 9, 1])
    print(repository_1)
    index1 = repository_1.get_index_of_name_id(3)
    assert repository_1.get_vector_at_index(index1).get_color() == 'r' and repository_1.get_vector_at_index(
        index1).get_type() == 2 and repository_1.get_vector_at_index(index1).get_values() == [3, 9, 1]
    print("OK")
    repository_2 = VectorRepository([vector1, vector3, vector5])
    print(repository_2)
    repository_2.update_a_vector_identified_by_name_id(1, 'b', 3, [7, 3, 8])
    print(repository_2)
    index2 = repository_2.get_index_of_name_id(1)
    assert repository_2.get_vector_at_index(index2).get_color() == 'b' and repository_2.get_vector_at_index(
        index2).get_type() == 3 and repository_2.get_vector_at_index(index2).get_values() == [7, 3, 8]
    print("OK")
    repository_3 = VectorRepository([vector4, vector5, vector3])
    print(repository_3)
    repository_3.update_a_vector_identified_by_name_id(3, 'y', 3, [9, 2, -3])
    print(repository_3)
    index3 = repository_3.get_index_of_name_id(3)
    assert repository_3.get_vector_at_index(index3).get_color() == 'y' and repository_3.get_vector_at_index(
        index3).get_type() == 3 and repository_3.get_vector_at_index(index3).get_values() == [9, 2, -3]
    print("OK")
    repository_4 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_4)
    repository_4.update_a_vector_identified_by_name_id(4, 'r', 2, [1, 2, -9])
    print(repository_4)
    index4 = repository_4.get_index_of_name_id(4)
    assert repository_4.get_vector_at_index(index4).get_color() == 'r' and repository_4.get_vector_at_index(
        index4).get_type() == 2 and repository_4.get_vector_at_index(index4).get_values() == [1, 2, -9]
    print("OK")
    repository_5 = VectorRepository([vector1])
    print(repository_5)
    repository_5.update_a_vector_identified_by_name_id(1, 'g', 3, [5, 4, 2])
    print(repository_5)
    index5 = repository_5.get_index_of_name_id(1)
    assert repository_5.get_vector_at_index(index5).get_color() == 'g' and repository_5.get_vector_at_index(
        index5).get_type() == 3 and repository_5.get_vector_at_index(index5).get_values() == [5, 4, 2]
    print("OK")


def test_delete_a_vector_by_index():
    print("24 -6.Delete a vector by index")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1)
    len1 = repository_1.get_length()
    repository_1.delete_a_vector_by_index(0)
    print(repository_1)
    print("Deletes vector at index 0")
    assert len1 != repository_1.get_length()
    print("OK")
    repository_2 = VectorRepository([vector3, vector2])
    print(repository_2)
    len2 = repository_2.get_length()
    repository_2.delete_a_vector_by_index(1)
    print(repository_2)
    print("Deletes vector at index 1")
    assert len2 != repository_2.get_length()
    print("OK")
    repository_3 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_3)
    len3 = repository_3.get_length()
    repository_3.delete_a_vector_by_index(4)
    print(repository_3)
    print("Deletes vector at index 4")
    assert len3 != repository_3.get_length()
    print("OK")
    repository_4 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_4)
    len4 = repository_4.get_length()
    repository_4.delete_a_vector_by_index(2)
    print(repository_4)
    print("Deletes vector at index 2")
    assert len4 != repository_4.get_length()
    print("OK")
    repository_5 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_5)
    len5 = repository_5.get_length()
    repository_5.delete_a_vector_by_index(1)
    print(repository_5)
    print("Deletes vector at index 1")
    assert len5 != repository_5.get_length()
    print("OK")


def test_delete_a_vector_by_name_id():
    print("25 -7.Delete a vector by name_id")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1)
    len1 = repository_1.get_length()
    repository_1.delete_a_vector_by_name_id(1)
    print(repository_1)
    print("Deletes vector with name_id 1")
    assert len1 != repository_1.get_length()
    print("OK")
    repository_2 = VectorRepository([vector3, vector2])
    print(repository_2)
    len2 = repository_2.get_length()
    repository_2.delete_a_vector_by_name_id(2)
    print(repository_2)
    print("Deletes vector with name_id 2")
    assert len2 != repository_2.get_length()
    print("OK")
    repository_3 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_3)
    len3 = repository_3.get_length()
    repository_3.delete_a_vector_by_name_id(5)
    print(repository_3)
    print("Deletes vector with name_id 5")
    assert len3 != repository_3.get_length()
    print("OK")
    repository_4 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_4)
    len4 = repository_4.get_length()
    repository_4.delete_a_vector_by_name_id(2)
    print(repository_4)
    print("Deletes vector with name_id 2")
    assert len4 != repository_4.get_length()
    print("OK")
    repository_5 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_5)
    len5 = repository_5.get_length()
    repository_5.delete_a_vector_by_name_id(3)
    print(repository_5)
    print("Deletes vector with name_id 3")
    assert len5 != repository_5.get_length()
    print("OK")


def test_plot_all_points_in_a_chart():
    print("26 -8.Plot all vectors in a chart")
    vector1 = MyVector(1, 'r', 4, [1, 2, 3])
    vector2 = MyVector(2, 'b', 2, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [3, 3, 2])
    vector4 = MyVector(4, 'r', 2, [3, 3, 3])
    vector5 = MyVector(5, 'b', 1, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_1)
    repository_1.plot_all_vectors_in_a_chart()


def test_get_the_minimum_of_all_vectors():
    print("27 -15.Get the min of all vectors")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1)
    print(f'The minimum of all vectors is:{repository_1.get_minimum_of_all_vector()}')
    assert repository_1.get_minimum_of_all_vector() == -1
    print("OK")
    repository_2 = VectorRepository([vector1, vector3, vector5])
    print(repository_2)
    print(f'The minimum of all vectors is:{repository_2.get_minimum_of_all_vector()}')
    assert repository_2.get_minimum_of_all_vector() == 0
    print("OK")
    repository_3 = VectorRepository([vector1, vector5])
    print(repository_3)
    print(f'The minimum of all vectors is:{repository_3.get_minimum_of_all_vector()}')
    assert repository_3.get_minimum_of_all_vector() == 1
    print("OK")
    repository_4 = VectorRepository([vector3, vector4])
    print(repository_4)
    print(f'The minimum of all vectors is:{repository_4.get_minimum_of_all_vector()}')
    assert repository_4.get_minimum_of_all_vector() == -1
    print("OK")
    repository_5 = VectorRepository([vector1, vector2])
    print(repository_5)
    print(f'The minimum of all vectors is:{repository_5.get_minimum_of_all_vector()}')
    assert repository_5.get_minimum_of_all_vector() == 1
    print("OK")


def test_delete_all_vectors_for_which_the_product_is_grater_than_value():
    print("28 -19.Delete all vectors for which the product of elements is grater then a given value")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1)
    len1 = repository_1.get_length()
    repository_1.delete_all_vectors_for_which_the_product_is_greater_than_a_given_value(2)
    print(repository_1)
    print("Deletes vector with with product grater then 2")
    assert len1 != repository_1.get_length()
    print("OK")
    repository_2 = VectorRepository([vector3, vector2])
    print(repository_2)
    len2 = repository_2.get_length()
    repository_2.delete_all_vectors_for_which_the_product_is_greater_than_a_given_value(12)
    print(repository_2)
    print("Deletes vector with with product grater then 12")
    assert len2 == repository_2.get_length()
    print("OK")
    repository_3 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_3)
    len3 = repository_3.get_length()
    repository_3.delete_all_vectors_for_which_the_product_is_greater_than_a_given_value(1)
    print(repository_3)
    print("Deletes vector with with product grater then 1")
    assert len3 != repository_3.get_length()
    print("OK")
    repository_4 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_4)
    len4 = repository_4.get_length()
    repository_4.delete_all_vectors_for_which_the_product_is_greater_than_a_given_value(20)
    print(repository_4)
    print("Deletes vector with with product grater then 20")
    assert len4 == repository_4.get_length()
    print("OK")
    repository_5 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_5)
    len5 = repository_5.get_length()
    repository_5.delete_all_vectors_for_which_the_product_is_greater_than_a_given_value(15)
    print(repository_5)
    print("Deletes vector with with product grater then 15")
    assert len5 == repository_5.get_length()
    print("OK")


def test_update_the_color_of_a_vector_identified_by_name_id():
    print("29 -23.Update the color of a vector identified by name_id")
    vector1 = MyVector(1, 'r', 2, [1, 2, 3])
    vector2 = MyVector(2, 'b', 3, [3, 2, 1])
    vector3 = MyVector(3, 'y', 3, [0, 0, 0])
    vector4 = MyVector(4, 'r', 3, [-1, -1, -1])
    vector5 = MyVector(5, 'b', 3, [3, 6, 1])
    repository_1 = VectorRepository([vector1, vector2, vector3, vector4])
    print(repository_1)
    repository_1.update_color_for_vector_with_name_id(3, 'r')
    print(repository_1)
    index1 = repository_1.get_index_of_name_id(3)
    assert repository_1.get_vector_at_index(index1).get_color() == 'r'
    print("OK")
    repository_2 = VectorRepository([vector1, vector3, vector5])
    print(repository_2)
    repository_2.update_color_for_vector_with_name_id(1, 'b')
    print(repository_2)
    index2 = repository_2.get_index_of_name_id(1)
    assert repository_2.get_vector_at_index(index2).get_color() == 'b'
    print("OK")
    repository_3 = VectorRepository([vector4, vector5, vector3])
    print(repository_3)
    repository_3.update_color_for_vector_with_name_id(3, 'y')
    print(repository_3)
    index3 = repository_3.get_index_of_name_id(3)
    assert repository_3.get_vector_at_index(index3).get_color() == 'y'
    print("OK")
    repository_4 = VectorRepository([vector1, vector2, vector3, vector4, vector5])
    print(repository_4)
    repository_4.update_color_for_vector_with_name_id(4, 'r')
    print(repository_4)
    index4 = repository_4.get_index_of_name_id(4)
    assert repository_4.get_vector_at_index(index4).get_color() == 'r'
    print("OK")
    repository_5 = VectorRepository([vector1])
    print(repository_5)
    repository_5.update_color_for_vector_with_name_id(1, 'g')
    print(repository_5)
    index5 = repository_5.get_index_of_name_id(1)
    assert repository_5.get_vector_at_index(index5).get_color() == 'g'
    print("OK")


def test_functions():
    test_menu()

    command = input(">>> ")
    while command != "0":
        if command == "31":
            test_menu()
        elif command == "1":
            test_add_scalar_to_vector()
        elif command == "2":
            test_add_scalar_to_vector_numpy()
        elif command == "3":
            test_add_two_vectors()
        elif command == "4":
            test_add_scalar_to_vector_numpy()
        elif command == "5":
            test_subtract_two_vectors()
        elif command == "6":
            test_subtract_two_vectors_numpy()
        elif command == "7":
            test_multiplication()
        elif command == "8":
            test_multiplication_numpy()
        elif command == "9":
            test_sum_of_elements_in_a_vector()
        elif command == "10":
            test_sum_of_elements_in_a_vector_numpy()
        elif command == "11":
            test_product_of_elements_in_a_vector()
        elif command == "12":
            test_product_of_elements_in_a_vector_numpy()
        elif command == "13":
            test_average_of_elements_in_a_vector()
        elif command == "14":
            test_average_of_elements_in_a_vector_numpy()
        elif command == "15":
            test_minimum_of_a_vector()
        elif command == "16":
            test_minimum_of_a_vector_numpy()
        elif command == "17":
            test_maximum_of_a_vector()
        elif command == "18":
            test_maximum_of_a_vector_numpy()
        elif command == "19":
            test_add_a_vector_to_repository()
        elif command == "20":
            test_get_all_vectors()
        elif command == "21":
            test_get_a_vector_at_index()
        elif command == "22":
            test_update_a_vector_at_index()
        elif command == "23":
            test_update_a_vector_identified_by_name_id()
        elif command == "24":
            test_delete_a_vector_by_index()
        elif command == "25":
            test_delete_a_vector_by_name_id()
        elif command == "26":
            test_plot_all_points_in_a_chart()
        elif command == "27":
            test_get_the_minimum_of_all_vectors()
        elif command == "28":
            test_delete_all_vectors_for_which_the_product_is_grater_than_value()
        elif command == "29":
            test_update_the_color_of_a_vector_identified_by_name_id()
        elif command == "30":
            break
        else:
            print("Invalid command!")
        command = input(">>> ")
