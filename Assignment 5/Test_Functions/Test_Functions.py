from Domain.Patient import Patient
from Repository.Department import Department
from Repository.Hospital import Hospital


def test_menu():
    print("----------------------------------------------------------")
    print("Write:")
    print("1.Add a patient to a department ")
    print("2.Deletes a patient from a department ")
    print("3.Update a patient information from a department ")
    print("4.Add a department to the hospital ")
    print("5.Deletes a department from the hospital ")
    print("6.Updates a department information ")
    print("7.Sort patients in a department by personal numerical code ")
    print("8.Sort departments by the number of patients ")
    print("9.Sort departments by the number of patients having the age above a given limit ")
    print("10.Sort departments by the number of patients and the patients in a department alphabetically ")
    print("11.Identify departments where there are patients under a given age ")
    print("12.Identify patients from a given department for which the first name or last name contain a given string ")
    print("13.Identify department/departments where there are patients with a given first name ")
    print("14.Form groups of 𝒌 patients from the same department and the same disease ")
    print("15.Form groups of 𝒌 departments having at most 𝒑 patients suffering from the same disease ")
    print("16 -Test menu ")
    print("17 -Go back ")


def test_add_a_patient_to_a_department():
    print("1 - 1.a)Add a patient to a department")
    department1 = Department(2, "Department 2", 20, [Patient("John", "Deer", "5001229047507", "Covid-19"),
                                                     Patient("Bruh", "John", "1990504134735", "Covid-19")])


def test_functions():
    test_menu()

    command = input(">>> ")
    while command != "0":
        if command == "16":
            test_menu()

        elif command == "17":
            break
        else:
            print("Invalid command!")
        command = input(">>> ")
