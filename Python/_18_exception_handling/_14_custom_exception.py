class InvalidAgeError(Exception):
    def __str__(self):
        return "you are still a kid"

    # def __init__(self):
    #     print("you are still a kid")