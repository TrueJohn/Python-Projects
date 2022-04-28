from Domain.Patient import Patient
from Repository.Department import Department
from Repository.Hospital import Hospital
from Interface.Interface import start

hospital = Hospital([Department(1, "Department 1", 10, [Patient("John", "Cena", "1950125020791", "Covid-19")]),
                     Department(2, "Department 2", 20, [Patient("John", "Deen", "5001229047507", "Covid-19"),
                                                        Patient("Brun", "John", "1990504134735", "Covid-19")
                                                        ]),
                     Department(3, "Department 3", 20, [Patient("Bruh", "John", "1910924033405", "Covid-19")])
                     ])

department1 = Department(2, "Department 2", 20, [Patient("John", "Deer", "5001229047507", "Covid-19"),
                                                 Patient("Bruh", "John", "1990504134735", "Covid-19")
                                                 ])

"""
print(hospital)
print("------------------------")

print("------------------------")

print("------------------------")
print(hospital.sort_departments_by_the_number_of_patients_having_the_age_above_a_given_limit(26))

print(department1)
print("------------------------")

print(hospital.identify_patients_from_a_department_for_which_the_f_name_or_l_name_contain_a_given_string(2, "n"))

print(department1)
department1.delete_patient_from_department("5001229047507")
print(department1)

print(hospital)
print('-------------')
print(hospital.identify_department_or_departments_where_there_are_patients_with_a_given_first_name("John"))
print("--------------")
hospital.delete_department(1)
hospital.delete_department(2)
hospital.delete_department(3)
print(hospital)

"""
start()