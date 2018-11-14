class Patients():
    def __init__(self, patient_id, patient_name):
        self.patient_id = patient_id
        self.patient_name = patient_name


class UserAuthentication():
    def __init__(self, user_login, user_password, role):
        # super().__init__(user_login,role)
        self.user_login = user_login  # delete this
        self.user_password = user_password
        self.role = role


# Driver Code

emp1 = UserAuthentication("Chris", "w", "Nurse")
emp2 = UserAuthentication("John", "s", "Doctor")
emp3 = UserAuthentication("Bob", "a", "Super User")

employee_list = [emp1, emp2, emp3]

pat1 = Patients(123, 'James')
pat2 = Patients(456, 'Chris')
pat3 = Patients(789, 'Po')

patient_list = [pat1, pat2, pat3]


def login_function():

    input_login = input("Enter your First Name:")
    input_password = input("Enter your Password:")

    for employee in employee_list:
        if employee.user_login == input_login:
            if employee.user_password == input_password:
                print(
                    f'Welcome, {employee.user_login}. Your access level is: {employee.role}')
                return True
            else:
                print('invalid login')
                login_function()


a = login_function()
if a:
    for employee in employee_list:
        if employee.role == "Doctor":
            print("What would you like to do? \n Options: \n list_patients \n - view_records <patient_id> \n - add_record <patient_id> \n - remove_record <patient_id> <record_id> \n - view_records <employee_id> \n - add_record <employee_id> \n - remove_record <employee_id> <record_id> \n - exit")
            break
        elif employee.role == "Super User":
            print("What would you like to do? \n Options: \n list_patients \n - view_records <patient_id> \n - add_record <patient_id> \n - remove_record <patient_id> <record_id> \n - list_employees \n - view_records <employee_id> \n - add_record <employee_id> \n - remove_record <employee_id> <record_id> \n - exit")


# List patients
def list_patients():
    for x in patient_list:
        print(x.patient_id, x.patient_name)


# patient_id
def show_patient():
    input_patient_id = input("Type in patient_id:")
    for patient in patient_list:
        if int(patient.patient_id) == int(input_patient_id):
            print(patient.patient_name)
            break
        else:
            print('Invalid ID')


# add patient
def add_record():
    new_name = input("id: ")
    new_name = int(new_name)
    new_id = input("name: ")

    new_patient = Patients(new_name, new_id)
    patient_list.append(new_patient)

    print(patient_list[3])
    print(len(patient_list))


# remove patient
def remove_patient():
    input_remove_patient = input("Type in patient_id to remove:")

    for i, x in enumerate(patient_list):
        if int(x.patient_id) == int(input_remove_patient):
            patient_list.pop(i)
            break
        else:
            print('Invalid ID')


# INPUT TO ASK WHAT YOU WANT TO DO
input_function = input("What You Want?:")

if input_function == "list_patients":
    list_patients()
elif input_function == "show_patient":
    show_patient()
elif input_function == "remove_patient":
    remove_patient()
elif input_function == "add_record":
    add_record()
