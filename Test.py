#student_crud 
class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRegistrationSystem:
    def __init__(self):
        self.students = {}

    # CREATE
    def create_student(self, student_id, name, age, major):
        if student_id in self.students:
            print("Student with this ID already exists.")
            return False
        else:
            self.students[student_id] = Student(student_id, name, age, major)
            print("Student created successfully.")
            return True

    # READ
    def read_student(self, student_id):
        if student_id in self.students:
            print(str(self.students[student_id]) + "\n")
            return student_id
        else:
            print("Student not found.")

    def read_all_students(self):
        if not self.students:
            print("No students registered.")
            return []
        else:
            for student in self.students.values():
                print(str(student))
            return self.students.values()

    # UPDATE
    def update_student(self, student_id, name=None, age=None, major=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if major:
                student.major = major
            print("Student updated successfully.")
            return True
        else:
            print("Student not found.")
            return False

    # DELETE
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
            return True
        else:
            print("Student not found.")
            return False

import unittest

class TestStudentRegistrationSystem(unittest.TestCase):
    
    def setUp(self):
        self.registration = StudentRegistrationSystem()
        # Add a student for initial setup
        self.registration.create_student(1, 'Doug', 18, 'Biochemistry')

    def test_create_student_success(self):
        result = self.registration.create_student(2, 'Mary', 22, 'Finance')
        self.assertTrue(result)
        self.assertIn(2, self.registration.students)
        self.assertEqual(self.registration.students[2].name, 'Mary')
        self.assertEqual(self.registration.students[2].age, 22)
        self.assertEqual(self.registration.students[2].major, 'Finance')

    def test_create_student_duplicate_id(self):

        result = self.registration.create_student(1, 'Dylan', 18, 'Biology')
        self.assertFalse(result)
        self.assertEqual(self.registration.students[1].name, 'Doug')  

    def test_read_student_success(self):
        result = self.registration.read_student(1)
        self.assertEqual(result, 1)

    def test_read_student_not_found(self):
        result = self.registration.read_student(99)
        self.assertIsNone(result)

    def test_read_all_students(self):
        result = self.registration.read_all_students()
        self.assertEqual(len(result), 1)  

    def test_read_all_students_empty(self): 
        self.registration.delete_student(1)  
        result = self.registration.read_all_students()
        self.assertEqual(len(result), 0) 

    def test_update_student_success(self):
        result = self.registration.update_student(1, name='Andy', age=19, major='Computer Science')
        self.assertTrue(result)
        self.assertEqual(self.registration.students[1].name, 'Andy')
        self.assertEqual(self.registration.students[1].age, 19)
        self.assertEqual(self.registration.students[1].major, 'Computer Science')

    def test_update_student_not_found(self):
        result = self.registration.update_student(99, name='Paul')
        self.assertFalse(result)

    def test_update_student_partial_data(self):
        result = self.registration.update_student(1, major='Mathematics')
        self.assertTrue(result)
        self.assertEqual(self.registration.students[1].major, 'Mathematics')
        self.assertEqual(self.registration.students[1].name, 'Doug')  

    def test_delete_student_success(self):
        result = self.registration.delete_student(1)
        self.assertTrue(result)
        self.assertNotIn(1, self.registration.students)

    def test_delete_student_not_found(self):
        result = self.registration.delete_student(99)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

