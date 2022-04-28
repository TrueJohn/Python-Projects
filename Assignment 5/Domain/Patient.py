import datetime


class Patient(object):
    """Creates a Patient object."""

    def __init__(self, first_name, last_name, pnc, disease):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__pnc = pnc
        self.__disease = disease

    def __str__(self):
        """
        Returns the string representation of a patient object.
        :return:
        """
        age = self.get_patient_age()
        string_rep = "Patience:" + self.__first_name + " " + self.__last_name + " age " + str(age) + " with pnc:"
        string_rep += self.__pnc + " " + "and disease:" + self.__disease

        return string_rep

    def set_first_name(self, first_name):
        """
        Set the first name component of the patient class.
        :param: first_name:
        :return:
        """
        self.__first_name = first_name

    def set_last_name(self, last_name):
        """
        Set the last name component of the patient class.
        :param: last_name:
        :return:
        """
        self.__last_name = last_name

    def set_personal_numerical_code(self, personal_numerical_code):
        """
        Set the personal numerical code component of the patient class.
        :param: personal_numerical_code:
        :return:
        """
        self.__pnc = personal_numerical_code

    def set_disease(self, disease):
        """
        Set the disease component of the patient class.
        :param: disease:
        :return:
        """
        self.__disease = disease

    def get_first_name(self):
        """
        Get the first name component of the patient class.
        :return:
        """
        first_name_copy = self.__first_name
        return first_name_copy

    def get_last_name(self):
        """
        Get the first name component of the patient class.
        :return:
        """
        last_name_copy = self.__last_name
        return last_name_copy

    def get_personal_numerical_code(self):
        """
        Get the personal numerical code component of the patient class.
        :return:
        """
        personal_code_copy = self.__pnc
        return personal_code_copy

    def get_disease(self):
        """
        Get the disease component of the patient class.
        :return:
        """
        disease_copy = self.__disease
        return disease_copy

    def get_patient_age(self):
        """
        Get the patience age based on the personal identification number.
        :return:
        """
        s = self.__pnc[0]
        aa = self.__pnc[1] + self.__pnc[2]
        ll = self.__pnc[3] + self.__pnc[4]
        zz = self.__pnc[5] + self.__pnc[6]

        if s == "1" or s == "2":
            aa = "19" + aa
        elif s == "3" or s == "4":
            aa = "18" + aa
        elif s == "5" or s == "6":
            aa = "20" + aa

        if int(ll) > 12:
            ll = ll[0]
        if int(zz) > 31:
            zz = zz[0]
        date = datetime.datetime(int(aa), int(ll), int(zz))
        current_date = datetime.datetime.now()
        age = (current_date - date).days // 365
        if age < 0:
            age = age * (-1)
        return age
