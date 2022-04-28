from Repository.Hospital import Hospital
from Repository.Department import Department
from Repository.Department import Patient


class HospitalController:
    def __init__(self, hospital: Hospital(list_of_departments=None)):
        """
        Constructor of the class.Creating a new controller
        :param: hospital:
        """
        self.__hospital = hospital

    def __str__(self) -> str:
        """
        Returns the string representation of the controller.
        """
        return str(self.__hospital)

    def add_department(self, department_id, name, number_of_beds, list_of_patients):
        """
        Add a department to the hospital.s
        :param department_id:
        :param name:
        :param number_of_beds:
        :param list_of_patients:
        :return:
        """
        self.__hospital.add_department(department_id, name, number_of_beds, list_of_patients)

    def delete_department(self, department_id):
        """
        Deletes a department from hospital.
        :param department_id:
        :return:
        """
        self.__hospital.delete_department(department_id)

    def update_department(self, department_id, name, number_of_beds, list_of_patients):
        """
        Updates a department in the hospital.
        :param: department_id:
        :param: name:
        :param: number_of_beds:
        :param: list_of_patients:
        :return:
        """
        self.__hospital.update_department(department_id, name, number_of_beds, list_of_patients)


class DepartmentController:
    def __init__(self,
                 department: Department(department_id=None, name=None, number_of_beds=None, list_of_patients=None)):
        """
        Constructor of the class.Creating a new controller
        :param: hospital:
        """
        self.__department = department

    def __str__(self) -> str:
        """
        Returns the string representation of the controller.
        """
        return str(self.__department)

    def add_patient(self, first_name, last_name, pnc, disease):
        """
        Adds a patient to a department if is not full.
        :param: first_name:the first name of the person(string)
        :param: last_name:the last name of the person(string)
        :param: pnc:the personal numerical code(string)
        :param: disease:the disease of the person(string)
        :return:
        """
        self.__department.add_patient(first_name, last_name, pnc, disease)

    def delete_patient_from_department(self, patient_pnc):
        """
        Removes a patient from a department.
        :param: patient_pnc:
        :return:
        """
        self.__department.delete_patient_from_department(patient_pnc)


class PatientController:
    def __init__(self, patient: Patient(first_name=None, last_name=None, pnc=None, disease=None)):
        """
        Constructor of the class.Creating a new controller
        :param: hospital:
        """
        self.__patient = patient

    def __str__(self) -> str:
        """
        Returns the string representation of the controller.
        """
        return str(self.__patient)

    def get_patient_age(self):
        """
        Get the patience age based on the personal identification number.
        :return:
        """
        return self.get_patient_age()

    def get_disease(self):
        """
        Get the disease component of the patient class.
        :return:
        """
        return self.get_disease()

    def get_personal_numerical_code(self):
        """
        Get the personal numerical code component of the patient class.
        :return:
        """
        return self.get_personal_numerical_code()

    def get_last_name(self):
        """
        Get the first name component of the patient class.
        :return:
        """
        return self.get_last_name()

    def get_first_name(self):
        """
        Get the first name component of the patient class.
        :return:
        """
        return self.get_first_name()

    def set_disease(self, disease):
        """
        Set the disease component of the patient class.
        :param: disease:
        :return:
        """
        self.__patient.set_disease(disease)

    def set_personal_numerical_code(self, personal_numerical_code):
        """
        Set the personal numerical code component of the patient class.
        :param: personal_numerical_code:
        :return:
        """
        self.__patient.set_personal_numerical_code(personal_numerical_code)

    def set_last_name(self, last_name):
        """
        Set the last name component of the patient class.
        :param: last_name:
        :return:
        """
        self.__patient.set_last_name(last_name)

    def set_first_name(self, first_name):
        """
        Set the first name component of the patient class.
        :param: first_name:
        :return:
        """
        self.__patient.set_first_name(first_name)
