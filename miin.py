import random
from prompt_toolkit import prompt


class Hospital():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employee = {}
        self.patient = {}

    def add_employee(self, user):
        return self.employee.update(user)

    def add_patient(self, user):
        return self.patient.update(user)


class Patient():
    def __init__(self, id_number, name, assigned_doctor, diagnosis):
        self.id_number = id_number
        self.name = name
        self.assigned_doctor = assigned_doctor
        self.diagnosis = diagnosis

    def __str__(self):
        return (f"ID number: {self.id_number} \nName: {self.name} \nDiagnosis: {self.diagnosis} \nAssigned Doctor: {self.assigned_doctor}")


class Employee():
    def __init__(self, id_number, name, position, department, username, password):
        self.id_number = id_number
        self.name = name
        self.position = position
        self.department = department
        self.username = username
        self.password = password

    def __str__(self):
        return (f"ID number:{self.id_number} \nName: {self.name} \nPosition: {self.position} \nDepartment: {self.department}")


hospital = Hospital("Hospital ABC", "1, Street 9, Smartsville")

e_one = Employee("E1", "Sophie Tan", "SuperAdmin",
                 "Administration", "Sophie", "654321")
sophie = {"Sophie": e_one}
hospital.add_employee(sophie)

e_two = Employee("E2", "Nic Alexander", "Doctor", "Oncology", "Nic", "246801")
nic = {"Nic": e_two}
hospital.add_employee(nic)

p_one = Patient("P1", "Lee Chong Wah", "Nic", "nose cancer")
lee = {"Lee": p_one}
hospital.add_patient(lee)

p_two = Patient("P2", "Mary Han", "Nic", "breast cancer")
mary = {"Mary": p_two}
hospital.add_patient(mary)


def authentication():
    access = False
    while access == False:
        try:
            get_username = input("Please enter your username: " + "\n")
            userobj = hospital.employee.get(get_username)
            if get_username == userobj.username:
                get_password = prompt(
                    "Please enter your password: " + "\n", is_password=True)
                if get_password == userobj.password:
                    access = True
                    print("-"*40)
                    print(
                        f"Welcome, {get_username}. Your access level is: {userobj.position}")
                    print("-"*40)
                    if userobj.position == "SuperAdmin":
                        print("> Options: \n > 1. list_patients \n > 2. view_patient_records \n > 3. add_patient_record \n > 4. remove_pateint_record \n > 5. list_employees \n > 6. view_employee_records \n > 7. add_employee_record \n > 8. remove_employee_record \n > type 'exit' to exit database")

                    elif userobj.position == "Doctor":
                        print("> Options: \n > 1. list_patients \n > 2. view_patient_records \n > 3. add_patient_record \n > 4. remove_pateint_record \n > type 'exit' to exit database")
                else:
                    access == False
                    print("That doesn't seem right, try again.")
        except:
            print("Please input a valid username.")


def generate_em_id():
    random_e_id = "E" + str(random.randint(3, 501))
    return random_e_id


def generate_p_id():
    random_p_id = "P" + str(random.randint(3, 2001))
    return random_p_id


def options():
    get_choice = input("What would you like to do? ")
    if get_choice == "1":
        print(hospital.patient)
        options()
    elif get_choice == "2":
        get_name = input("Please enter patient's name: " + "\n")
        patobj = hospital.patient.get(get_name)
        print(patobj)
        options()
    elif get_choice == "3":
        get_id = generate_p_id()
        get_name = input("Please enter patient's name: " + "\n")
        get_doctor = input("Please assign a doctor: " + "\n")
        get_diagnosis = input("Please input patient's diagnosis: " + "\n")
        new_p = Patient(get_id, get_name, get_doctor, get_diagnosis)
        new_p_dict = {get_name: new_p}
        hospital.add_patient(new_p_dict)
        print("New patient has been added to the patient database.")
        print(hospital.patient)
        options()
    elif get_choice == "4":
        get_name = input(
            "Please enter patient's name that you want to remove: " + "\n")
        if get_name in hospital.patient:
            del hospital.patient[get_name]
            print(hospital.patient)
        else:
            print("That patient doesn't exist.")
        options()
    elif get_choice == "5":
        print(hospital.employee)
        options()
    elif get_choice == "6":
        get_employee_name = input("Please enter employee's name: " + "\n")
        empobj = hospital.employee.get(get_employee_name)
        print(empobj)
        options()
    elif get_choice == "7":
        get_id = generate_em_id()
        get_e_name = input("Please enter new employee's name: " + "\n")
        get_position = input("Please input employee's position: " + "\n")
        get_department = input(
            "Which department will the employee be stationed? " + "\n")
        get_username = input(
            "Enter a username to access patient records:" + "\n")
        get_password = prompt(
            "Enter a 6 digit password to login" + "\n", is_password=True)
        new_e = Employee(get_id, get_e_name, get_position,
                         get_department, get_username, get_password)
        new_e_dict = {get_e_name: new_e}
        hospital.add_employee(new_e_dict)
        print("New employee has been added to the employee database.")
        print(hospital.employee)
        options()
    elif get_choice == "8":
        get_e_name = input(
            "Please enter employee's name that you want to remove: " + "\n")
        if get_e_name in hospital.employee:
            del hospital.employee[get_e_name]
            print(hospital.employee)
        else:
            print("That employee doesn't exist.")
        options()
    elif get_choice == "exit":
        exit()


def welcome():
    print(f"Welcome to {hospital.name}")
    print("-"*40)
    authentication()
    options()


welcome()
