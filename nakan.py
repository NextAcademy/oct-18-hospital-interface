class Employee:
    def __init__(self, first, last, position, username):
        self.first = first
        self.last = last
        self.position = position
        self.username = username


class Patient:
    def __init__(self, p_id, name, gender):
        self.id = p_id
        self.name = name
        self.gender = gender


user_pass = {
    'nakan': 'pass123',
    'tim': 'pass',
    'admin': 'pass234'
}

pat_1 = Patient('12345', 'blah blah', 'male')
pat_2 = Patient('12312', 'blah bsdf', 'female')
pat_3 = Patient('28461', 'blah asdgd', 'male')

patient_list = [pat_1, pat_2, pat_3]

doc_1 = Employee('tim', 'duncan', 'doctor', 'login')
doc_2 = Employee('admin', 'kjlsda', 'nurse', 'asdf')
doc_3 = Employee('nakan', 'kjlsasdda', 'nursadfse', 'sdf')

employee_list = [doc_1, doc_2, doc_3]


def login():
    print("Welcome to Hospital")
    userInput = input("Please enter your username: ")
    passInput = input("Please enter your password: ")

    if user_pass.get(userInput) == passInput:
        for x in employee_list:
            if x.first == userInput:
                print("\n Welcome, " + userInput +
                      " your access level is  Employee.position\n")
                choose_option()
    else:
        print("\n invalid login, please try again\n")
        login()

# Option 1: List Patients


def list_patients():
    for x in patient_list:
        print(x.id, x.name, x.gender)

# Option 2: View Specific Record


def view_records():
    print("which patient record would you like to view?")
    id_input = input("Patient id: ")
    for x in patient_list:
        if int(x.id) == int(id_input):
            print("Patient name is: " + x.name +
                  "\nPatient gender is: " + x.gender + "\n")
            break
    else:
        print("invalid id, please try again")
        view_records()

# Option 3: Add A Record


def add_record():
    print("\n to add a new patient, fill in the following information")
    new_id = input("New Patient id: ")
    new_name = input("New Patient name: ")
    new_gender = input("New Patient gender: ")

    new_record = (new_id, new_name, new_gender)
    patient_list.append(new_record)
    print("new record has been added: ")
    print(new_record)
    print("total number of records: ")
    print(len(patient_list))

# Option 4: Remove Record


def remove_record():
    remove_id = input("which patient record would you like to remove? id: ")

    for i, x in enumerate(patient_list):
        if x.id == remove_id:
            patient_list.pop(i)
            print("\n patient removed \n")

# Choose Options after Login Successful


def choose_option():
    select_option = input(
        "What would you like to do? Please select a number: \n 1. list_patients \n 2. view-records \n 3. add_record \n 4. remove_record \n 5. exit \n your pick: ")
    if select_option == "1":
        list_patients()
        choose_option()
    elif select_option == "2":
        view_records()
        choose_option()
    elif select_option == "3":
        add_record()
        choose_option()
    elif select_option == "4":
        remove_record()
        choose_option()
    elif select_option == "5":
        exit()
    else:
        print("\n option not available \n")
        choose_option()


login()
