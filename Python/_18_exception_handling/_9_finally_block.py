try:
    print(10/0)
finally:
    print("Finally Block got executed!")

# finally block will get executed no matter what, even when there no exception, with exception, and exception which didnot get handled.
# finally block are mainly used for closing the file and database.