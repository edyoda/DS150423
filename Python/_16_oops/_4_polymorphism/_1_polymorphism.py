# Polymorphism

# poly - many
# morphism - form
# single entity and many forms

# types of polymorphism
# 1. Compile Time Polymorphism (overloading) - this is not supported in python
# 2. Runtime Polymorphism (overriding)

# 1. Compile Time Polymorphism
# Overloading - same name method with different parameters (seq, type, no. of parameters)

class human:

    def behaviour(self,friends):
        print("Masti!")

    def behaviour(self,parents,home):
        print("Sajjan")

obj = human()
obj.behaviour("Diksha")