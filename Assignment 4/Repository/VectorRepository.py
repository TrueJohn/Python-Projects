import numpy as np

from Domain.MyVector import MyVector
import matplotlib.pyplot as plt


class VectorRepository:
    """Creates a list of vectors."""

    def __init__(self, vector_list):
        """
        Initialising the point repository.
        :param vector_list: a list of vectors
        """
        self.__vectors = vector_list.copy()

    def __str__(self):
        """
        Converting a VectorRepository object into a string.
        """
        try:
            repr_str = f"The number of vectors in the repository is: {len(self.__vectors)}\n"
            for vector in self.__vectors:
                repr_str += str(vector) + "\n"
            return repr_str
        except TypeError:
            print("The repository is empty.")

    def is_name_id_of_vector_already_in_repository(self, name_id):
        """
        Verifies if a given name_id is already in the repository.
        :param name_id:integer representing given name_id
        :return:True if it's in repository
                False if it's not in the repository
        """
        for i in range(len(self.__vectors)):
            if self.__vectors[i].get_name_id() == name_id:
                return True
        return False

    def get_index_of_name_id(self, name_id):
        """
        Gets the index of a vector for a given name_id.
        :param name_id:
        :return:
        """
        for i in range(len(self.__vectors)):
            if self.__vectors[i].get_name_id() == name_id:
                return i
        return None

    def add_vector(self, name_id, color, type_of_vector, values):
        """
        #1 Add a new vector to the repository.

        """
        try:
            name_id1 = int(name_id)
            if self.is_name_id_of_vector_already_in_repository(name_id):
                raise IndexError
        except ValueError:
            print("The name_id must be an integer.")
        except IndexError:
            print("The name_id is already in the repository.")
        else:
            try:
                type_of_vector1 = int(type_of_vector)
            except ValueError:
                print("The type_of_vector coordinate must be an integer")
            else:
                try:
                    colors = ["r", "g", "b", "y", "m"]
                    ok = 0
                    for item in colors:
                        if color == item:
                            ok = 1
                    if ok == 0:
                        raise ValueError
                except ValueError:
                    print('Colors must be one of the following : r , g , b, y, m')
                else:
                    vector = MyVector(name_id1, color, type_of_vector1, values)
                    self.__vectors.append(vector)

    def get_length(self):
        return len(self.__vectors)

    def get_all_vectors(self):
        """
        #2 Gets all the vectors in the repository.
        :return:all the vectors in the repository
        """
        copy_list = VectorRepository(self.__vectors)
        return copy_list

    def get_vector_at_index(self, index):
        """
        #3 Gets a vector at a given index.
        :param index:positive integer representing the index of the needed vector
        :return:the vector at the given index
        """
        if index >= len(self.__vectors) or index < 0:
            print("The index is outside of the bounds of the repository.")
        else:
            vector_at_index = self.__vectors[index]
            return vector_at_index

    def update_vector_at_index(self, index, color, type_of_vector, values):
        """
        #4 Updates a vector at a given index
        :param index:positive integer representing the index of the vector to be updated
        :param color:string representing the new color of the vector
        :param type_of_vector:string representing the new type of the vector
        :param values:list representing the
        :return:
        """
        try:
            if index >= len(self.__vectors) or index < 0:
                raise ValueError
        except ValueError:
            print("Index outside of the bounds of the repository")
        else:
            try:
                type_of_vector1 = int(type_of_vector)
            except ValueError:
                print("The type_of_vector coordinate must be an integer")
            else:
                try:
                    colors = ["r", "g", "b", "y", "m"]
                    ok = 0
                    for item in colors:
                        if color == item:
                            ok = 1
                    if ok == 0:
                        raise ValueError
                except ValueError:
                    print('Colors must be one of the following : r , g , b, y, m')
                else:
                    self.__vectors[index].set_color(color)
                    self.__vectors[index].set_type(type_of_vector1)
                    self.__vectors[index].set_values(values)

    def update_a_vector_identified_by_name_id(self, name_id, color, type_of_vector, values):
        """
        #5 Updates a vector identified by name_id
        :return:
        """
        try:
            if not self.is_name_id_of_vector_already_in_repository(name_id):
                raise ValueError
        except ValueError:
            print("There doesn't exist a vector with the given name_id in the repository.")
        else:
            try:
                type_of_vector1 = int(type_of_vector)
            except ValueError:
                print("The type_of_vector coordinate must be an integer")
            else:
                try:
                    colors = ["r", "g", "b", "y", "m"]
                    ok = 0
                    for item in colors:
                        if color == item:
                            ok = 1
                    if ok == 0:
                        raise ValueError
                except ValueError:
                    print('Colors must be one of the following : r , g , b, y, m')
                else:
                    for i in range(len(self.__vectors)):
                        if self.__vectors[i].get_name_id() == name_id:
                            self.__vectors[i].set_color(color)
                            self.__vectors[i].set_type(type_of_vector1)
                            self.__vectors[i].set_values(values)

    def delete_a_vector_by_index(self, index):
        """
        #6 Deletes a vector by index
        :return:
        """
        try:
            if index >= len(self.__vectors) or index < 0:
                raise ValueError
        except ValueError:
            print("Index outside of the bounds of the repository")
        else:
            del self.__vectors[index]

    def delete_a_vector_by_name_id(self, name_id):
        """
        #7 Deletes a vector by name_id.
        :param name_id:
        :return:
        """
        try:
            ok = 0
            index = -1
            for i in range(len(self.__vectors)):
                if self.__vectors[i].get_name_id() == name_id:
                    ok = 1
                    index = i
            if ok == 0:
                raise ValueError
        except ValueError:
            print("The given name_id doesn't exist in the repository.")
        else:
            del self.__vectors[index]

    def plot_all_vectors_in_a_chart(self):
        """
        #8 Plots all vectors in a chart
        :return:
        """
        if len(self.__vectors) == 0:
            return "The vector repository is empty."
        else:
            for vector in self.__vectors:
                if vector.get_type() == 1:
                    values = vector.get_values()
                    t = np.arange(values[0], values[1])
                    plt.plot(t, t, f'{vector.get_color()}o')
                elif vector.get_type() == 2:
                    values = vector.get_values()
                    t = np.arange(values[0], values[1])
                    plt.plot(t, t, f'{vector.get_color()}s')
                elif vector.get_type() == 3:
                    values = vector.get_values()
                    t = np.arange(values[0], values[1])
                    plt.plot(t, t, f'{vector.get_color()}^')

                else:
                    values = vector.get_values()
                    t = np.arange(values[0], values[1])
                    plt.plot(t, t, f'{vector.get_color()}D')
        plt.show()

    def get_minimum_of_all_vector(self):
        """
        #15 Gets the minimum value from the repository.
        :return:
        """
        minimum_value_from_repository = self.__vectors[1].minimum()
        for vector in self.__vectors:
            if vector.minimum() < minimum_value_from_repository:
                minimum_value_from_repository = vector.minimum()

        return minimum_value_from_repository

    def delete_all_vectors_for_which_the_product_is_greater_than_a_given_value(self, value):
        """
        #20 Delete all vectors for which the product of elements is greater than a given value.
        :return:
        """
        for i in range(len(self.__vectors)-1):
            if self.__vectors[i].get_product() > value:
                del self.__vectors[i]

    def update_color_for_vector_with_name_id(self, name_id, new_color):
        """
        #23 Update the color of a vector identified by name_id.
        :param name_id:
        :param new_color:
        :return:
        """
        for vector in self.__vectors:
            if vector.get_name_id() == name_id:
                vector.set_color(new_color)
                break
