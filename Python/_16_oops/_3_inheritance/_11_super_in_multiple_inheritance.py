class C:
    def __init__(self):
        print("C = Parent Class")

    def functional(self):
        print("Functional")

    def language(self):
        print("C")

class Cpp:
    def __init__(self):
        print("Cpp = Parent Class")

    def procedural(self):
        print("Procedural")

    def language(self):
        print("Cpp")

class Python(Cpp,C):
    def __init__(self):
        C.__init__(self)
        Cpp.__init__(self)
        print("Python = Child Class")

    def both(self):
        print("Functional and Procedural")

    def language(self):
        C.language(self)
        Cpp.language(self)
        print("Python")

python = Python()
python.functional()
python.procedural()
python.both()
python.language()
