import pdb
import random
from subprocess import Popen, PIPE
import pexpect
import sys
import fileinput


class Hospital():
    def __init__(self, name, number_beds, number_rooms, number_clinics, location, phone_number):
        self.name = name
        self.number_beds = number_beds
        self.number_rooms = number_rooms
        self.number_clinics = number_clinics
        self.doctors = []
        self.nurses = []
        self.employees = self.all_employees()
        self.location = location
        self.phone_number = phone_number
        self.departments = ['A&E', 'Cardiac Centre', 'Critical Care Centre', 'Diabetes Care Centre', 'Dietetics', 'Endoscopy',
                            'Health Screening Centre', 'Imaging', 'Laboratory', 'Maternity Services', 'Oncology Centre', 'Pharmacy', 'Rehabilitation']

    def all_employees(self):
        employees = self.doctors + self.nurses
        return employees

    def get_number_employees(self):
        self.number_employees = len(self.doctors) + len(self.nurses)
        return self.number_employees

    def hire_doctor(self, name, age='None', department='General'):
        name = Doctor(name, age, department)
        self.doctors.append(name)
        return name

    def hire_nurse(self, name, age='None', department='General'):
        name = Nurse(name, age, department)
        self.nurses.append(name)
        return name

    def fire_doctor(self, name):
        for doctor in self.doctors:
            if doctor.name == name:
                self.doctors.remove(doctor)
                return self.doctors
        else:
            print('Name not found!')

    def fire_nurse(self, name):
        for nurse in self.nurses:
            if nurse.name == name:
                self.nurses.remove(nurse)
                return self.nurses
        else:
            print('Name not found!')

    def search_employee(self, name):
        for employee in self.all_employees():
            if employee.name == name:
                return True
        else:
            print('Name not found! Try again!')

    def __str__(self):
        hospital_summary = str({
            'Name': self.name,
            'Location': self.location,
            # 'Departments': self.departments,
            'Clinics': self.number_clinics,
            'Rooms': self.number_rooms,
            'Beds': self.number_beds,
            'Doctors': len(self.doctors),
            'Nurses': len(self.nurses),
        })
        return hospital_summary


class Patient():
    def __init__(self, name, case, age, department='General'):
        self.name = name
        self.department = department
        self.age = age
        self.case = case
        self.id = self.generate_patient_id()

    def generate_patient_id(self):
        return f'P-{self.department[0:3]}-{random.randint(1000,9999)}'

    def __str__(self):
        patient_summary = str({
            'Name': self.name,
            'Case': self.case,
            'Department': self.department,
            'Age': self.age,
        })
        return patient_summary


class Report():
    def __init__(self, patient, report):
        self.patient = patient
        self.report = report

    def __str__(self):
        report_summary = str({
            'Name': self.patient,
            # 'Case': self.case,
            # 'Department': self.department,
            'Report': self.report,
        })
        return report_summary


class Employee():
    def __init__(self, name, age=None, department='General'):
        self.name = name
        self.age = age
        self.department = department
        self.patients = []
        self.reports = []
        self.id = self.generate_employee_id()

    def __str__(self):
        employee_summary = str({
            'Name': self.name,
            'Age': self.age,
            'Department': self.department,
            'Patients': len(self.patients),
            'Reports': len(self.reports),
            'ID': self.id
        })
        return employee_summary

    # def generate_doctor_id(self):
    #     return f'D-{self.department[0:3].upper()}-{random.randint(10,99)}'

    def generate_employee_id(self):
        return f'E-{self.department[0:3].upper()}-{random.randint(100,999)}'

    def get_number_patients(self):
        self.number_patients = len(self.patients)
        return self.number_patients


class Doctor(Employee):

    def admit_patient(self, name, case, age, department=None):
        department = self.department
        new_patient = Patient(name, case, age, department)
        self.patients.append(new_patient)
        return new_patient

    def view_patients(self, name):
        for patient in self.patients:
            if patient.name == name:
                print(patient)
                return self.patients
        else:
            print('No patients found!')

    def write_report(self, Patient, report):
        new_report = Report(Patient, report)
        self.reports.append(new_report)
        return new_report

    def view_report(self, Patient):
        for report in self.reports:
            if report.name == Patient:
                print(report)
                return self.reports
        else:
            print('No reports found!')

    def delete_report(self, Patient):
        for report in self.reports:
            if report.name == Patient:
                self.reports.remove(report)
                return self.reports
        else:
            print('No reports found!')

    def discharge_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                self.patients.remove(patient)
                return self.patients
        else:
            print('Patient name not found!')


class Nurse(Employee):
    # def __init__(self):
    #     super().__init__(name, age, department)
    #     self.id = self.generate_nurse_id

    def admit_patient(self, name, case, age, department=None):
        department = self.department
        new_patient = Patient(name, case, age, department)
        self.patients.append(new_patient)
        return new_patient

    def discharge_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                self.patients.remove(patient)
                return self.patients
        else:
            print('Patient name not found!')

    def view_patient(self, name):
        for patient in self.patients:
            if patient.name == name:
                print(patient)
                return self.patients
        else:
            print('No patients found!')

    def view_report(self, Patient):
        for report in self.reports:
            if report.name == Patient:
                print(report)
                return self.reports
        else:
            print('No reports found!')


kpj = Hospital('KPJ', 500, 300, 20, 'Damansara', '+603-5555-3333')
sunway = Hospital('Sunway', 1000, 600, 40, 'Sunway', '+603-1111-3333')

ahmed = kpj.hire_doctor('Ahmed Ramzi', 28, 'General')
josh = kpj.hire_doctor('Josh Teng', 30, 'Imaging')
edwin = ahmed.admit_patient('Edwin', 'Flu', 28)
Nicolas = ahmed.admit_patient('Nicolas', 'Chicken Pox', 27)
edwin_report = ahmed.write_report(
    'Edwin', 'Mild flu. Plenty of rest and fluids')
edwin_report = ahmed.write_report(
    'Nicolas', 'Chicken Pox. Medications and bedrest')
sophie = kpj.hire_nurse('Sophie Smith', 25, 'General')
dan = kpj.hire_nurse('Dan White', 32, 'Imaging')


# print(kpj)
# print(sunway)
# print(ahmed)
# print(edwin)
# print(dan)


print('\n----------------------------------------\n'
      '\nWelcome to the Hospital Interface\n'
      '\nPlease insert your Hospital name')

hospital = input('\n----------------------------------------\n')
if hospital.lower() == 'kpj' or hospital.lower() == 'sunway':
    print(f'\nWelcome to the system of {hospital.upper()}\n'
          '\nPlease insert your full name\n')
    full_name = input('Full Name:\n')
    if kpj.search_employee(full_name) is True:
        print(f'\nWelcome, {full_name}!\n'
              '\nPlease insert your password\n')
        password = input('Password:\n')
        if password == '0000':

            while True:

                print('\nCorrect Password!'
                      f'\n What do you want to do, {full_name}?'
                      '\n Type the number:'
                      '\n1- Hospital Summary'
                      '\n2- Show Patients'
                      '\n3- Show Reports'
                      '\n4- Other')

                command = input('Command\n')

                if command == '1':
                    print(kpj)
                elif command == '2':
                    for patient in ahmed.patients:
                        print(patient.__dict__)
                elif command == '3':
                    for report in ahmed.reports:
                        print(report.__dict__)
                else:
                    print(
                        'This feature is still being built. Thank you for your patience!')

        else:
            print('The password is not correct!')

else:
    print('Hospital is not in this system. Please check the spelling and try again')


# while True:
#     command = input('inser your command \n')
