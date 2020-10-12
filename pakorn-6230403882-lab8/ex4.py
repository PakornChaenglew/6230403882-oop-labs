class ComENStudent:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def __str__(self):
        return f"{self.name} has taken these courses:{self.courses}"

    def take_courses(self, *courses):
        a = self.courses
        for i in courses:
            a.append(i)
        self.courses = a


class CoEStudent(ComENStudent):
    def __init__(self, name, course_ids):
        super().__init__(name, course_ids)

class DMEStudent(ComENStudent):
    def __init__(self, name, course_ids):
        super().__init__(name, course_ids)

    def make_content_type(self, name):
        self.name2 = name

    def __str__(self):
        return super().__str__() + f"\n specialized in creating content type:{self.name2}"


if __name__ == '__main__':
    com_student = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_student.append(manee)
    com_student.append(mana)
    for com_student in com_student:
        com_student.take_courses("SC401206")
        print(com_student)
