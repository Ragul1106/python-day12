import unittest
from gradesystem.marks import calculate_cgpa
from gradesystem.grade import get_grade

class TestGradeSystem(unittest.TestCase):
    def test_cgpa(self):
        self.assertEqual(calculate_cgpa([95, 85, 75]), round((95+85+75)/3/9.5, 2))

    def test_grades(self):
        self.assertEqual(get_grade(9.1), 'A+')
        self.assertEqual(get_grade(8.2), 'A')
        self.assertEqual(get_grade(7.1), 'B')
        self.assertEqual(get_grade(6.5), 'C')
        self.assertEqual(get_grade(5.5), 'D')
        self.assertEqual(get_grade(4.9), 'F')

if __name__ == '__main__':
    unittest.main()
