class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def change_id(self, id):
        self.id = id

    def print(self):
        print("{} - {}".format(self.name, self.id))


name = input("Tên của bạn là gì? ")
id = input("Mã sinh viên của bạn là gì? ")
student = Student(name, int(id))
student.print()

student.change_id(int(input("Đổi mã sinh viên của bạn? ")))
student.print()
