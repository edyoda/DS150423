class division:
    def div(self):
        res = 0
        no1 = 10
        no2 = 0
        try:
            res = no1 / no2
        except:
            print("Error Occured")
        print(res)
        print("End of method")

obj = division()
obj.div()

# try    - block which is use to store suspicous code
# except - block where you can write handling code