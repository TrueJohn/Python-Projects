from Domain.Patient import Patient
from Functions.Functions import sort_algorithm
from Functions.Functions import search_algorith


class Department(object):

    def __init__(self, department_id, name, number_of_beds, list_of_patients: list[Patient]):
        self.__department_id = department_id
        self.__name = name
        self.__number_of_beds = number_of_beds
        self.__list_of_patients = list_of_patients

    def __str__(self):
        """
        Converting a Department object into a string.
        """
        try:
            repr_str = "\n" + f"Department:[" + self.__name + \
                       f"] with the number of patients:[" + f"{len(self.__list_of_patients)}]\n"
            repr_str += f"with departament_id:[" + str(self.__department_id) + "] and number of beds:[" + \
                        str(self.__number_of_beds) + "]\n"

            for i in range(len(self.__list_of_patients)):
                repr_str += str(self.__list_of_patients[i]) + "\n"

            return repr_str

        except TypeError:
            print("The department is empty.")

    def add_patient(self, first_name, last_name, pnc, disease):
        """
        Adds a patient to a department if is not full.
        :param: first_name:the first name of the person(string)
        :param: last_name:the last name of the person(string)
        :param: pnc:the personal numerical code(string)
        :param: disease:the disease of the person(string)
        :return:
        """
        if self.__number_of_beds == len(self.__list_of_patients):
            print("The department is full.")
        else:
            ok = 1
            for i in range(len(self.__list_of_patients)):
                if self.__list_of_patients[i].get_personal_numerical_code() == pnc:
                    print("A patient with the pnc:" + pnc + " already exist in the department.")
                    ok = 0
            if ok == 1:
                patient = Patient(first_name, last_name, pnc, disease)
                self.__list_of_patients.append(patient)

    def update_patient(self, first_name, last_name, pnc, disease):
        """
        Updates the details of a person in a department by pnc
        :param: first_name:the first name of the person(string)
        :param: last_name:the last name of the person(string)
        :param: pnc:the personal numerical code(string)
        :param: disease:the disease of the person(string)
        :return:
        """
        for i in range(len(self.__list_of_patients)):
            if self.__list_of_patients[i].get_personal_numerical_code() == pnc:
                self.__list_of_patients[i].set_first_name(first_name)
                self.__list_of_patients[i].set_last_name(last_name)
                self.__list_of_patients[i].set_disease(disease)
                break

    def delete_patient_from_department(self, patient_pnc):
        """
        Removes a patient from a department.
        :param: patient_pnc:
        """
        for i in range(len(self.__list_of_patients)):
            if self.__list_of_patients[i].get_personal_numerical_code() == patient_pnc:
                del self.__list_of_patients[i]
                break

    def set_department_id(self, department_id):
        """
        Set the department id.
        :param: department_id
        """
        self.__department_id = department_id

    def set_name(self, name):
        """
        Set the name of the department
        :param name:
        """
        self.__name = name

    def set_number_of_beds(self, number_of_beds):
        """
        Set the number of beds of the department.
        :param: number_of_beds:
        """
        self.__number_of_beds = number_of_beds

    def set_the_list_of_patients(self, list_of_patients):
        """
        Set the list of patients of the department
        :param list_of_patients:
        """
        self.__list_of_patients = list_of_patients

    def get_department_id(self):
        """
        Get the id of the department.
        :return:
        """
        department_id_copy = self.__department_id
        return department_id_copy

    def get_name(self):
        """
        Get the name of the department.
        :return:
        """
        name_copy = self.__name
        return name_copy

    def get_number_of_beds(self):
        """
        Get the number of beds of the department.
        :return:
        """
        number_of_beds_copy = self.__number_of_beds
        return number_of_beds_copy

    def get_list_of_patients(self):
        """
        Get the number of patients of the department.
        :return:
        """
        list_of_patients_copy = self.__list_of_patients
        return list_of_patients_copy

    def get_number_of_patients(self):
        """
        Get the number of patients of the department.
        :return:
        """
        return len(self.__list_of_patients)

    def sort_the_patients_in_a_department_by_numerical_code(self):
        """
        Sort the patients in a department by numerical code.
        :return:
        """

        def condition(i, j):
            if self.__list_of_patients[i].get_personal_numerical_code() <= \
                    self.__list_of_patients[j].get_personal_numerical_code():
                return False
            else:
                return True

        self.__list_of_patients = sort_algorithm(self.__list_of_patients, condition)
        return self

    def sort_the_patients_alphabetically(self):
        """
        Sort the patients in a department alphabetically.
        :return:
        """

        def condition(i, j):
            if self.__list_of_patients[i].get_first_name() <= \
                    self.__list_of_patients[j].get_first_name() and self.__list_of_patients[i].get_last_name() <= \
                    self.__list_of_patients[j].get_last_name():
                return True
            else:
                return False

        self.__list_of_patients = sort_algorithm(self.__list_of_patients, condition)
        return self

    def get_number_of_patients_of_age_above_a_age_limit(self, limit):
        """
        Get number of patients of age above a limit.
        :param: limit:
        :return:
        """
        nb = 0
        for i in range(len(self.__list_of_patients)):
            if self.__list_of_patients[i].get_patient_age() > limit:
                nb += 1
        return nb

    def get_number_of_patients_of_age_under_a_age_limit(self, limit):
        """
        Get number of patients of age under a limit.
        :param: limit:
        :return:
        """
        nb = 0
        for i in range(len(self.__list_of_patients)):
            if self.__list_of_patients[i].get_patient_age() < limit:
                nb += 1
        return nb

    def does_department_contain_patient_with_a_given_first_name(self, first_name):
        """
        Verifies if a department contain a person with a given first name.
        :param: name:
        :return:
        """

        def condition(index):
            if self.__list_of_patients[index].get_first_name() == first_name:
                return True
            else:
                return False

        if len(search_algorith(self.__list_of_patients, condition)) > 0:
            return True
        else:
            return False

    def does_department_contain_patient_with_a_pnc(self, pnc):
        """
        Verifies if a department contain a person with a given pnc.
        :param: name:
        :return:
        """

        def condition(index):
            if self.__list_of_patients[index].get_personal_numerical_code() == pnc:
                return True
            else:
                return False

        if len(search_algorith(self.__list_of_patients, condition)) > 0:
            return True
        else:
            return False
