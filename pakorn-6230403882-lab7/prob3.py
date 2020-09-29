class student:
    university_name = "Khon Kaen University"

    def __init__(self, name, *course_ids):
        self.name = name
        self.course_ids = course_ids

    def print(self):
        return print(f"{self.name} registered courses {self.course_ids}")

    @classmethod
    def set_university_name(cls, university):
        cls.university_name = university

    @classmethod
    def get_university_name(cls):
        return cls.university_name

if __name__ == '__main__':
    manee = student("Manee", "842004")
    mana = student("Mana", "842004", "842005", "813701")
    chujai = student("Chujai", "842004", "842005")
    manee.print()
    mana.print()
    chujai.print()
    manee.set_university_name("KKU")
    print(f"These students are in {mana.get_university_name()}")
