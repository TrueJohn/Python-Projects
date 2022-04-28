from Domain.Patient import Patient
from Repository.Hospital import Hospital
from Repository.Department import Department

"""
from Test_Functions.Test_Functions import test_functions
"""


def print_menu():
    """
    Prints all the options in the console type interface.
    """
    print("---------------------------------------------------------")
    print("Write: ")
    print("1.Add a patient to a department")
    print("2.Deletes a patient from a department")
    print("3.Update a patient information from a department")
    print("4.Add a department to the hospital")
    print("5.Deletes a department from the hospital")
    print("6.Updates a department information")
    print("7.Sort patients in a department by personal numerical code")
    print("8.Sort departments by the number of patients")
    print("9.Sort departments by the number of patients having the age above a given limit")
    print("10.Sort departments by the number of patients and the patients in a department alphabetically")
    print("11.Identify departments where there are patients under a given age")
    print("12.Identify patients from a given department for which the first name or last name contain a given string")
    print("13.Identify department/departments where there are patients with a given first name")
    print("14.Form groups of 𝒌 patients from the same department and the same disease")
    print("15.Form groups of 𝒌 departments having at most 𝒑 patients suffering from the same disease")
    print("16.Print Hospital")
    print("17 -Test_Functions functions")
    print("18 -Print menu")
    print("19 -Stop the program")


def start():
    """
    Start the console type interface.
    :return:
    """
    print_menu()
    hospital = Hospital([Department(1, "Department 1", 10, [Patient("John", "Ken", "1950125020791", "Covid-19")]),
                         Department(2, "Department 2", 20, [Patient("Franklin", "Lamar", "5001229047507", "Covid-19"),
                                                            Patient("Karen", "Joe", "192904144735", "Covid-19"),
                                                            Patient("Carl", "Johnson", "5301249058507", "Covid-19"),
                                                            Patient("Silvester", "Arnold", "2394504534735", "Covid-19"),
                                                            Patient("Mike", "Armstrong", "5994524334735", "Covid-?"),
                                                            Patient("Bill", "Jeffrey", "5607224047507", "Covid-?"),
                                                            Patient("Alex", "Park", "1564684134735", "Covid-?")
                                                            ]),
                         Department(3, "Department 3", 20, [Patient("Michael", "Trevor", "1910924033405", "Covid-19")])
                         ])
    command = input(">>> ")
    while command != "0":
        if command == "18":
            print_menu()
        elif command == "1":
            try:
                first_name = input("First_name:")
                if not first_name.isalpha():
                    print("The first name must contain only letters.")
                    raise ValueError
                last_name = input("Last_name:")
                if not last_name.isalpha():
                    print("The last name must contain only letters.")
                    raise ValueError
                disease = input("Disease:")
                pnc = input("Pnc:")
                if len(pnc) < 13 or len(pnc) > 13 or pnc[0] not in ['1', '2', '3', '4', '5']:
                    print("The pnc is not valid.")
                    raise ValueError

                if hospital.pnc_already_exist_in_the_hospital(pnc):
                    print("There already exist a patient with the same pnc in the hospital.")
                    raise ValueError

                department_id = int(input("Department ID:"))
                if hospital.get_department_by_id(department_id) is None:
                    print("There doesn't exist a department with this ID in the hospital.")
                    raise ValueError
                if hospital.get_department_by_id(department_id).get_number_of_beds() == len(
                        hospital.get_department_by_id(department_id).get_list_of_patients()):
                    print("This department is full.")
                    raise ValueError

            except ValueError:
                print("")
            else:
                hospital.get_department_by_id(department_id).add_patient(first_name, last_name, pnc, disease)
                print(hospital)
                command = input(">>> ")
        elif command == "2":
            try:
                pnc = input("Pnc:")
                if len(pnc) < 13 or len(pnc) > 13 or pnc[0] not in ['1', '2', '3', '4', '5']:
                    print("The pnc is not valid.")
                    raise ValueError

                if hospital.pnc_already_exist_in_the_hospital(pnc):
                    print("There already exist a patient with the same pnc in the hospital.")
                    raise ValueError
                else:
                    department_id = int(input("Department ID:"))
                    if hospital.get_department_by_id(department_id) is None:
                        print("There doesn't exist a department with this ID in the hospital.")
                        raise ValueError

            except ValueError:
                print("")
            else:
                hospital.get_department_by_id(department_id).delete_patient_from_department(pnc)
                print(hospital)
                command = input(">>> ")
        elif command == "3":
            try:
                first_name = input("First name:")
                if not first_name.isalpha():
                    print("The first name must contain only letters.")
                    raise ValueError
                last_name = input("Last name:")
                if not last_name.isalpha():
                    print("The last name must contain only letters. ")
                    raise ValueError
                disease = input("Disease: ")
                pnc = input("Pnc: ")
                if len(pnc) > 13 or len(pnc) < 13 or pnc[0] not in ['1', '2', '3', '4', '5']:
                    print("The pnc is not valid.")
                    raise ValueError

                if hospital.pnc_already_exist_in_the_hospital(pnc):
                    print("There already exist a patient with the same pnc in the hospital.")
                    raise ValueError

                department_id = int(input("Department ID:"))
                if hospital.get_department_by_id(department_id) is None:
                    print("There doesn't exist a department with this ID in the hospital.")
                    raise ValueError

            except ValueError:
                print("")
            else:
                hospital.get_department_by_id(department_id).update_patient(first_name, last_name, pnc, disease)
                print(hospital)
                command = input(">>> ")
        elif command == "4":
            try:
                department_id = int(input("Department ID:"))
                if hospital.get_department_by_id(department_id):
                    print("There already exist a department with this ID in the hospital.")
                    raise ValueError
                name = input("Department name:")
                number_of_beds = int(input("Number of beds"))
                list_of_patience = []
            except ValueError:
                print("")
            else:
                hospital.add_department(department_id, name, number_of_beds, list_of_patience)
            command = input(">>> ")
        elif command == "5":
            try:
                department_id = int(input("Department ID:"))
                if hospital.get_department_by_id(department_id) is None:
                    print("There doesn't exist a department with this ID in the hospital.")
                    raise ValueError
            except ValueError:
                print("")
            else:
                hospital.delete_department(department_id)
            command = input(">>> ")
        elif command == "6":
            try:
                department_id = int(input("Department ID:"))
                if hospital.get_department_by_id(department_id) is None:
                    print("There doesn't exist a department with this ID in the hospital.")
                    raise ValueError
                name = input("Department name:")
                number_of_beds = int(input("Number of beds"))
                list_of_patience = hospital.get_department_by_id(department_id)
            except ValueError:
                print("")
            else:
                hospital.update_department(department_id, name, number_of_beds, list_of_patience)
            command = input(">>> ")
        elif command == "7":
            try:
                department_id = int(input("Department ID:"))
                if hospital.get_department_by_id(department_id) is None:
                    print("There doesn't exist a department with this ID in the hospital.")
                    raise ValueError
            except ValueError:
                print("")
            else:
                print(
                    hospital.get_department_by_id(department_id).sort_the_patients_in_a_department_by_numerical_code())
            command = input(">>> ")
        elif command == "8":
            print(hospital.sort_the_departments_by_number_of_patients())
            command = input(">>> ")
        elif command == "9":
            try:
                age_limit = int(input("Age limit:"))
                if age_limit > 110 or age_limit < 1:
                    print("The age limit must be real.(1-110)")
            except ValueError:
                print("The age limit must be a number.")
            else:
                print(hospital.sort_departments_by_the_number_of_patients_having_the_age_above_a_given_limit(age_limit))
            command = input(">>> ")
        elif command == "10":
            print(hospital.sort_the_departments_by_number_of_patients_and_the_patients_in_a_department_alphabetically())
            command = input(">>> ")
        elif command == "11":
            try:
                age_limit = int(input("Age limit:"))
                if age_limit > 110 or age_limit < 1:
                    print("The age limit must be real.(1-110)")
            except ValueError:
                print("The age limit must be a number.")
            else:
                print(hospital.identify_departments_where_there_are_patients_under_a_given_age(age_limit))
            command = input(">>> ")
        elif command == "12":
            try:
                department_id = int(input("Department ID:"))
                if hospital.get_department_by_id(department_id) is None:
                    print("There doesn't exist a department with this ID in the hospital.")
                    raise ValueError
                given_string = input("Given string:")
                if not given_string.isalpha():
                    print("The string must contain only letters.")
                    raise ValueError
            except ValueError:
                print("")
            else:
                print(
                    hospital.identify_patients_from_a_department_for_which_the_f_name_or_l_name_contain_a_given_string(
                        department_id,
                        given_string))
            command = input(">>> ")
        elif command == "13":
            try:
                first_name = input("First name:")
                if not first_name.isalpha():
                    print("The first name must contain only letters.")
                    raise ValueError
            except ValueError:
                print("")
            else:
                print(hospital.identify_department_or_departments_where_there_are_patients_with_a_given_first_name(
                    first_name))
            command = input(">>> ")
        elif command == "14":
            try:
                k = int(input("The number K:"))
            except ValueError:
                print("K must be a number positive number.")
            else:
                try:
                    department_id = int(input("Department ID:"))
                    if hospital.get_department_by_id(department_id) is None:
                        print("There doesn't exist a department with this ID in the hospital.")
                        raise ValueError
                except ValueError:
                    print("")
                else:
                    count=0
                    for group in hospital.form_groups_of_k_patience_from_the_same_department_and_the_same_disease(
                            department_id, k):
                        count+=1
                        print(f"{count}:{group}\n")
                command = input(">>> ")

        elif command == "15":

            command = input(">>> ")
        elif command == "16":
            print(hospital)
            command = input(">>> ")
        elif command == "17":
            """
            test_functions()
            """
        elif command == "19":
            break
        else:
            print("Invalid command!")
            command = input(">>> ")


start()
