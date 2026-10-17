import json

with open("students.json", "r") as file:
    students = json.load(file)


while True:
    print("==== Student Management System ====")
    print("1. Display Students")
    print("2. Add Students")
    print("3. Search Students")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice :"))
    if choice == 1:
        for student in students:
            print("\033[1;36m\n========== STUDENT DETAILS ==========\033[0m")

            print("\033[1;33m------------------------------------\033[0m")
            print("\033[1;32mRoll Number  :\033[0m", student["roll"])
            print("\033[1;32mName         :\033[0m", student["name"])
            print("\033[1;32mAge          :\033[0m", student["age"])
            print("\033[1;32mCourse       :\033[0m", student["course"])
            print("\033[1;32mSemester     :\033[0m", student["semester"])
            print("\033[1;32mPhone Number :\033[0m", student["phone_number"])
            print("\033[1;32mE-mail       :\033[0m", student["E-mail"])
            print("\033[1;32mMarks        :\033[0m", student["marks"])
            print("\033[1;33m------------------------------------\033[0m")

            print("\033[1;36m====================================\033[0m\n")
            
    elif choice == 2:
        roll = int(input("Enter Roll number :"))
        n = input("Enter name :")
        a = int(input("Enter age :"))
        co = input("Enter course :")
        sem = int(input("Enter Semester :"))
        p = int(input("Enter Phone number :"))
        em = input("Enter Email :")
        m = int(input("Enter marks :"))

        new = {"roll":roll,"name":n,"age":a,"course":co,"semester":sem,"phone_number":p,"E-mail":em,"marks":m}
        students.append(new)

        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Student added successfully.")

    elif choice == 3:
        Found = False
        search_st = int(input("Enter Roll Number :"))

        for student in students:
            if search_st == student["roll"]:
                print("Roll number :",student["roll"])
                print("Name :",student["name"])
                print("Age :",student["age"])
                print("Course :",student["course"])
                print("Semester :",student["semester"])
                print("Phone Number :",student["phone_number"])
                print("E-mail :",student["E-mail"])
                print("Marks :",student["marks"])
                Found = True
                print("Student Found.")

        if Found == False:
            print("No student found")
    elif choice == 4:
        Found = False

        for_update = int(input("Enter Roll number for updation :"))
        for student in students:
            if student["roll"] == for_update:
                new_m = int(input("Enter new marks for update :"))
                student["marks"] = new_m
                with open("students.json", "w") as file:
                    json.dump(students, file, indent=4)
                Found = True
                print("Marks update successfully")

        if Found == False:
            print("No student found")
    elif choice == 5:
        Found = False
        for_del = int(input("Enter Roll Number for deletion :"))
        for student in students:
            if student["roll"] == for_del:
                students.remove(student)
                with open("students.json", "w") as file:
                    json.dump(students, file, indent=4)
                Found = True
                print("Student Deleted Successfully")
                
        if Found == False:
            print("No student found")

    elif choice == 6:
        print("Thank youh")
        break

    else:
        print("Invalid choice! Please select number (1 to 6)")