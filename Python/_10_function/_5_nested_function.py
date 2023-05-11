def outer():
    print("Outer")
    def inner():
        print("Inner")
    inner()


outer()