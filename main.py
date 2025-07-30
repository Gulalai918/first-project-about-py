print("Hello world")


name : str = "Gulalai"
father_name : str = "dayar khan"
age : int = 23

student_card = "student card\nname = " + name+  "\nfather name = "   + father_name+ "\nage = "     +str(age)
print(student_card)

student_card = """student card
name = %s
father name = %s
age = %d"""  % (name, father_name, age)
print(student_card)


student_card = f"""student card
name = {name}
father name = {father_name}
age = {age}"""
print(student_card)
