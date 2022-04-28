from Repository.Department import Department
from Functions.Functions import sort_algorithm
from Functions.Functions import search_algorith
from Functions.Functions import combinations


class Hospital(object):
    def __init__(self, list_of_departments: list[Department]):
        self.__list_of_departments = list_of_departments

    def __str__(self):
        """
                Converting a Hospital object into a string.

        """
        try:
            repr_str = "------------------------------------------------------" + "\n"
            repr_str += f"The number of  departments in the hospital is:" + str(len(self.__list_of_departments)) + "\n"
            for department in self.__list_of_departments:
                repr_str += str(department) + "\n"
            return repr_str

        except TypeError:
            print("The hospital is empty.")

    def get_list_of_department(self):
        """
        Gets the list of the departments in the hospital.
        :return:
        """
        return self.__list_of_departments.copy()

    def add_department(self, department_id, name, number_of_beds, list_of_patients):
        """
        Add a department to the hospital.
        :param: department_id:the id of the department
        :param: name:the name of the department
        :param: number_of_beds:the number of beds of the department
        :param: list_of_patients:the list of patients in the department
        :return:
        """
        department = Department(department_id, name, number_of_beds, list_of_patients)
        self.__list_of_departments.append(department)

    def update_department(self, department_id, name, number_of_beds, list_of_patients):
        """
        Update the data of a department to the hospital.
        :param: department_id:the id of the department
        :param: name:the name of the department
        :param: number_of_beds:the number of beds of the department
        :param: list_of_patients:the list of patients in the department
        :return:
        """
        self.get_department_by_id(department_id).set_name(name)
        self.get_department_by_id(department_id).set_number_of_beds(number_of_beds)
        self.get_department_by_id(department_id).set_the_list_of_patients(list_of_patients)

    def delete_department(self, department_id):
        """
        Deletes a department from the hospital.
        :param: department_id:the id of the department
        :return:
        """
        for i in range(len(self.__list_of_departments)):
            if self.__list_of_departments[i].get_department_id() == department_id:
                del self.__list_of_departments[i]
                break

    def pnc_already_exist_in_the_hospital(self, pnc):
        """
        This function verifies if a patient with the same pnc exist in the hospital.
        :param: pnc:
        :return:
        """
        for i in range(len(self.__list_of_departments)):
            if self.__list_of_departments[i].does_department_contain_patient_with_a_pnc(pnc):
                return True
        return False

    def get_department_by_id(self, given_id):
        for i in range(len(self.__list_of_departments)):
            if self.__list_of_departments[i].get_department_id() == given_id:
                return self.__list_of_departments[i]
        return None

    def sort_the_departments_by_number_of_patients(self):
        """
        Sort the patients in a department by number of patients.
        :return:
        """

        def condition(i, j):
            if self.__list_of_departments[i].get_number_of_patients() <= \
                    self.__list_of_departments[j].get_number_of_patients():
                return False
            else:
                return True

        self.__list_of_departments = sort_algorithm(self.__list_of_departments, condition)
        return self

    def sort_the_departments_by_number_of_patients_and_the_patients_in_a_department_alphabetically(self):
        """
        Sort departments by the number of patients and the patients in a department alphabetically.
        :return:
        """

        def condition(index, j):
            if self.__list_of_departments[index].get_number_of_patients() <= \
                    self.__list_of_departments[j].get_number_of_patients():
                return False
            else:
                return True

        for i in range(len(self.__list_of_departments)):
            self.__list_of_departments[i].sort_the_patients_alphabetically()

        self.__list_of_departments = sort_algorithm(self.__list_of_departments, condition)

        return self

    def sort_departments_by_the_number_of_patients_having_the_age_above_a_given_limit(self, limit):
        """
        Sort departments by the number of patients having the age above a given limit.
        :return:
        """

        def condition(i, j):
            if self.__list_of_departments[i].get_number_of_patients_of_age_above_a_age_limit(limit) < \
                    self.__list_of_departments[j].get_number_of_patients_of_age_above_a_age_limit(limit):
                return False
            else:
                return True

        self.__list_of_departments = sort_algorithm(self.__list_of_departments, condition)
        return self

    def identify_departments_where_there_are_patients_under_a_given_age(self, limit):
        """
        Identify departments where there are patients under a given age.
        :param: limit:
        :return:
        """

        def condition(index):
            if self.__list_of_departments[index].get_number_of_patients_of_age_under_a_age_limit(limit) > 0:
                return True
            else:
                return False

        return search_algorith(self.__list_of_departments, condition)

    def identify_patients_from_a_department_for_which_the_f_name_or_l_name_contain_a_given_string(self, department_id,
                                                                                                  given_string):
        """
        Identify patients from a given department for which the first name or last name contain a given string.
        :param: given_string:
        :return:
        """
        list1 = self.get_department_by_id(department_id).get_list_of_patients()

        def condition(index):
            if given_string in list1[index].get_first_name() or given_string in \
                    list1[index].get_last_name():
                return True
            else:
                return False

        list_of_patients = search_algorith(list1, condition)
        str_representation = ""
        if list_of_patients:
            for i in range(len(list_of_patients)):
                str_representation += str(list_of_patients[i]) + '\n'
            return str_representation
        else:
            return None

    def identify_department_or_departments_where_there_are_patients_with_a_given_first_name(self, first_name):
        """
        Identify department/departments where there are patients with a given first name.
        :param: first_name:
        :return:
        """

        def condition(index):
            if self.__list_of_departments[index].does_department_contain_patient_with_a_given_first_name(first_name):
                return True
            else:
                return False

        list_of_departments = search_algorith(self.__list_of_departments, condition)
        str_representation = ""
        if list_of_departments:
            for i in range(len(list_of_departments)):
                str_representation += str(list_of_departments[i]) + '\n'
            return str_representation
        else:
            return None

    def form_groups_of_k_patience_from_the_same_department_and_the_same_disease(self, department_id, k):
        """
        Form groups of 𝒌 patients from the same department and the same disease (𝒌 is a value given by the user).
        :param: k:
        :return:
        """
        final = []
        for i in range(len(self.get_department_by_id(department_id).get_list_of_patients())):
            temp_list = []
            temp_list.append(self.get_department_by_id(department_id).get_list_of_patients()[i].__str__())
            for j in range(i + 1, len(self.get_department_by_id(department_id).get_list_of_patients())):
                if self.get_department_by_id(department_id).get_list_of_patients()[i].get_disease() == \
                        self.get_department_by_id(department_id).get_list_of_patients()[j].get_disease():
                    temp_list.append(self.get_department_by_id(department_id).get_list_of_patients()[j].__str__())
            final += combinations([x for x in temp_list], k)
        return final
