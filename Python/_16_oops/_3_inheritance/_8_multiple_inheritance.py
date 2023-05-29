class C:
    def functional(self):
        print("Functional")

    def language(self):
        print("C")

class Cpp:
    def procedural(self):
        print("Procedural")

    def language(self):
        print("Cpp")

class Python(Cpp,C):
    def both(self):
        print("Functional and Procedural")

    def language(self):
        print("Python")

python = Python()
python.functional()
python.procedural()
python.both()
python.language()

print(Python.mro()) # Method Resolution Order