import numpy as np


class MyVector(object):
    """Creates a vector object."""

    def __init__(self, name_id, color, type_of_vector, values):

        try:
            name_id1 = int(name_id)
        except ValueError:
            print("The name id must be an integer")
        else:
            try:
                type_of_vector1 = int(type_of_vector)
                if type_of_vector1 < 1:
                    raise ValueError
            except ValueError:
                print("Type must be a positive integer grater or equal to 1")
            else:
                try:
                    if not isinstance(values, list) or isinstance(values, list) and len(values) == 0:
                        raise ValueError
                    else:
                        for i in range(len(values)):
                            if not isinstance(values[i], int):
                                raise ValueError
                except ValueError:
                    print("Values must be a non empty list of numbers")
                else:
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
                    else:
                        self.__name_id = name_id1
                        self.__type = type_of_vector1
                        self.__color = color
                        self.__values = values

    def set_name_id(self, new_name_id):
        """
        Set the new name id for a vector .
        :param new_name_id :string/integer representing the new name id of the vector
        :except ValueError if the param x is not an integer
        """
        try:
            new_name_id = int(new_name_id)
        except ValueError:
            print("The new name_id value must be an integer.")
        else:
            self.__name_id = new_name_id

    def set_type(self, new_type):
        """
        Set the new type for a vector .
        :param new_type :string/integer representing the new name id of the vector
        :except ValueError if the param new_type is not an integer positive integer
        """
        try:
            new_type = int(new_type)
            if new_type < 1:
                raise ValueError
        except ValueError:
            print("The new type value must be an integer.")
        else:
            self.__type = new_type

    def set_color(self, new_color):
        """
        Set the color of the vector.
        :param new_color:the new color of the point
        :ValueError if the color parameter is not a string or if it's not word from the predefined colors
        """
        try:
            colors = ["r", "g", "b", "y", "m"]
            ok = 0
            for item in colors:
                if new_color == item:
                    ok = 1
            if ok == 1:
                self.__color = new_color
            else:
                raise ValueError
        except ValueError:
            print('Colors must be one of the following : r , g , b, y, m')

    def set_values(self, new_values):
        """
        Set the new values for the vector
        :param new_values: list of integers
        """
        self.__values = new_values

    def get_name_id(self):
        """
        Returns the name_id of the vector.
        :return: name_id :integer representing the name_id of the vector.
        """
        return self.__name_id

    def get_type(self):
        """
        Returns the type of the vector.
        :return:  type:integer representing the type of the vector
        """
        return self.__type

    def get_color(self):
        """
        Returns the color of the vector.
        :return: color :string representing the color of the vector
        """
        return self.__color

    def get_values(self):
        """
        Returns the values of the vector.
        :return: values :list representing the values of the vector
        """
        return self.__values.copy()

    def __str__(self):
        """
        This function converts the point into a string representation.
        :return: the string representation of the point.
        """

        return "Name_id:" + str(self.__name_id) + " Values:" + str(
            self.__values) + " Color:" + self.__color + " Type:" + str(self.__type)

    def __add__(self, other):
        """
        #1,2 a)This function adds a scalar to a vector or a vector to a vector depending on the type of the parameter.
        :param other: integer or vector
        """
        try:
            if isinstance(other, MyVector) and len(other.__values) == len(self.__values):
                result = self.__values.copy()
                for i in range(len(self.__values)):
                    result[i] += other.__values[i]
                return result
            if isinstance(other, int):
                result = self.__values.copy()
                for i in range(len(self.__values)):
                    result[i] += other
                return result
        except ValueError:
            print("The scalar must be an integer or a vector with the same number of elements.")

    def __eq__(self, other):
        if self.__values == other.get_values() and self.__type == other.get_type() and self.__color == other.get_color() and self.__name_id == other.get_name_id():
            return True
        else:
            return False

    def get_product(self):
        product = 1
        for i in range(len(self.__values)):
            product *= self.__values[i]
        return product

    def add_numpy(self, other):
        """
        #1,2 a) This function adds a scalar to a vector or a vector to a vector depending on the type of the parameter.
        :param other: integer or vector
        """
        try:
            if isinstance(other, MyVector) and len(other.__values) == len(self.__values):
                result = np.add(self.__values, other.__values)
                return result.tolist()
            if isinstance(other, int):
                result = np.add(self.__values, other)
                return result.tolist()
        except ValueError:
            print("The scalar must be an integer or a vector with the same number of elements.")

    def __sub__(self, other):
        """
        #2 b)This function subtracts a vector from another vector.
        :param other:
        :return:
        """
        try:
            if isinstance(other, MyVector) and len(other.__values) == len(self.__values):
                result = self.__values.copy()
                for i in range(len(self.__values)):
                    result[i] -= other.__values[i]
                return result
        except ValueError:
            print("The parameter must be an vector and have the same number of elements.")

    def subtract_numpy(self, other):
        """
        #2 b)This function subtracts a vector from another vector using numpy.
        :param other:
        :return:
        """
        try:
            if isinstance(other, MyVector) and len(other.__values) == len(self.__values):
                result = np.subtract(self.__values, other.__values)
                return result.tolist()

        except ValueError:
            print("The parameter must be an vector and have the same number of elements.")

    def __mul__(self, other):
        """
        #2 c)This function multiplies the values of 2 vectors and returns the result.
        :param other: other :vector
        :return: result :the resulting number after the multiplication
        """
        try:
            if isinstance(other, MyVector) and len(other.__values) == len(self.__values):
                copy_list = self.__values.copy()
                product = 0
                for i in range(len(self.__values)):
                    product += copy_list[i] * other.__values[i]
                return product
            else:
                raise ValueError
        except ValueError:
            print("The parameter must be an vector and have the same number of elements.")

    def multiply_numpy(self, other):
        """
        #2 c)This function multiplies the values of 2 vectors and returns the result.
        :param other: other :vector
        :return: result :the resulting number after the multiplication
        """
        try:
            if isinstance(other, MyVector) and len(other.__values) == len(
                    self.__values):
                result = np.sum(np.multiply(other.__values, self.__values))
                return result.tolist()
            else:
                raise ValueError
        except ValueError:
            print("The parameter must be an vector and have the same number of elements.")

    def sum_of_elements_in_a_vector(self):
        """
        #3 a)This function returns the sum of the elements of the vector
        """
        sum1 = 0
        for i in range(len(self.__values)):
            sum1 += self.__values[i]
        return sum1

    def sum_of_elements_in_a_vector_numpy(self):
        """
        #3 a)This function returns the sum of the elements of the vector using numpy library.
        """
        return np.sum(self.__values)

    def product_of_elements_in_a_vector(self):
        """
        #3 b)This function returns the product of the elements of the vector.
        """
        pro1 = 1
        for i in range(len(self.__values)):
            pro1 *= self.__values[i]
        return pro1

    def product_of_elements_in_a_vector_numpy(self):
        """
        #3 b)This function returns the product of the elements of the vector using numpy library.
        """
        return np.product(self.__values)

    def avg_of_elements_in_a_vector(self):
        """
        #3 c)This function returns the average of the elements of the vector.
        """
        return self.sum_of_elements_in_a_vector() / len(self.__values)

    def avg_of_elements_in_a_vector_numpy(self):
        """
        #3 c)This function returns the average of the elements of the vector using numpy.
        """
        return np.average(self.__values)

    def minimum(self):
        """
        #3 d)This function returns the minimum element of the vector.
        :return minimum:the minimum element of the vector
        """
        minimum = self.__values[0]
        for i in range(len(self.__values)):
            if self.__values[i] < minimum:
                minimum = self.__values[i]
        return minimum

    def minimum_numpy(self):
        """
        #3 d)This function returns the minimum element of the vector using numpy.
        """
        return np.amin(self.__values)

    def maximum(self):
        """
        #3 e)This function returns the maximum element of the vector.
        :return:maximum representing the maximum element of the vector
        """
        maximum = self.__values[0]
        for i in range(len(self.__values)):
            if self.__values[i] > maximum:
                maximum = self.__values[i]
        return maximum

    def maximum_numpy(self):
        """
        #3 e)This function returns the maximum element of the vector using numpy.
        """
        return np.amax(self.__values)
