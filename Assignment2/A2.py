"""
Steven Yang-Zong 1931679
420-LCU COmputer Programming, Section-01
S.Hilal, instructor
Assignment 2
"""

def cal_total_grade(x):
    """ Calculate the total grade of a student"""
    #Sum of all provided grade as all hold equal weight (25%) of the final grade
    total_grade = sum(x[2:])
    return total_grade

def cal_letter_grade(y):
    """Calculate the letter grade of a student"""
    #Determine letter grade according to provided table
    letter = ""
    if y >= 87:
        letter = "A"
    elif 75 <= y <= 86:
        letter = "B"
    elif 65 <= y <= 74:
        letter = "C"
    elif y < 65:
        letter = "F"
    else:
        return "Error with letter grade identification"
    return letter

def list_grade_avg(z):
    """Calculates the average of the class, assignments, or test using the grades of the students in the list"""
    sum_all_grades = 0
    for i in range(len(list_of_students)):
        sum_all_grades += list_of_students[i][z]
    grade_avg = sum_all_grades/len(list_of_students)
    return grade_avg


#initializing the list of all the students
list_of_students = []

while True:
    #Program menu
    print("""
    Welcome to the Simple Class Calculator. Here's the list of available options:
        1- Enter a student record (Name, ID, and 4 grades seperated by commas and no spaces).
        2- Display the full class data sorted in alphabetical order based on name.
        3- Display the class descriptive statistics.
        4- Display a chosen student record.
        5- Exit
    """)
    #Menu input
    menu_opt = input("Select an option by entering its number or 5 to exit: ")

    #Option 1
    if menu_opt == "1":
        #asking for user input
        user_inp = input("\nEnter Student Record (Name, Id, and 4 grades seperated by commas and no spaces): ")
        #converting user input (string) into a list with all the elements
        user_list = user_inp.split(",")
        #initializing student list that would be temporary list for current student
        student_list = []
        #initialize a variable (validity) used later on to see if the input has passed all requirements, modified to 0 if requirement not met
        validity = 1

        #saving the user input into student_list
        for i in user_list:
            #appending name to student_list as is
            if i == user_list[0]:
                student_list.append(user_list[0])
            #converting ID from string to int and appending to student_list
            elif i == user_list[1]:
                student_list.append(user_list[1])
            #converting the rest of elements (4 of them) to floats and appending them to student_list
            else:
                student_list.append(float(i))

        #verify if there are exactly 6 elements in the list
        if len(student_list) != 6:
            print("\nRecord Incomplete, Record rejected.")
            #modifying to 0 means that it is not valid anymore. The value of validity will be used later on
            validity = 0

        #verifying if the ID number has exactly 7 digits
        elif len(student_list[1]) != 7:
            print("\nID must have 7 digits. Record rejected.")
            validity = 0

        #initiallization of variable starting value representing the position of the element to be analyzed
        index = 0
        #loop to iterate through all elements of the list to see if there are identical ID numbers to the current student
        #comparing the position of the current position to the length of the whole list of students
        while index < len(list_of_students):
            #If matching student ID
            if list_of_students[index][1] == student_list[1]:
                print("\nDuplicate ID number. Record rejected.")
                validity = 0
                break
            #Continuing the loop through the rest of the elements
            elif list_of_students[index][1] != student_list[1]:
                index += 1

        #using the variable Validity to see if the input is valid as if it wasns't, the value would have been different
        if validity == 1:
            print("Record Accepted")

            #appending the value of the total grade to the student_list
            student_list.append(cal_total_grade(student_list))

            #appending the value of the letter grade to the student_list
            student_list.append(cal_letter_grade(student_list[-1]))
            #appending the student_list to the list of all students
            list_of_students.append(student_list)

    elif menu_opt == "2":
        if list_of_students:
            #sorting the list of students according to name, then student ID if they have the same name
            list_of_students.sort()
            #prints out all saved data in list_of_students could improve visual of this by removing []
            print(list_of_students)
        else:
            print("ERROR, unable to process option 2, list_of_students is empty")

    elif menu_opt == "3":
        if list_of_students:
            #shows number of students in the list
            print("Number of students entered:", len(list_of_students))
            #shows class, test1, test2, assignment1, assignment2 averages by putting the average that we want through the function (list_grade_avg(z))
            print("Class average:", list_grade_avg(6), "\nAssignment 1 average:", list_grade_avg(2), "Assignment 2 average:", list_grade_avg(3), "\nTest 1 average:", list_grade_avg(4), "Test 2 average:", list_grade_avg(5))

            #initializing count of the people in each letter grade
            grade_a, grade_b, grade_c, grade_f = 0, 0, 0, 0

            #iterizing through all students to count the number of students in each letter grade
            for i in range(len(list_of_students)):

                if list_of_students[i][7] == "A":
                    grade_a += 1
                elif list_of_students[i][7] == "B":
                    grade_b += 1
                elif list_of_students[i][7] == "C":
                    grade_c += 1
                elif list_of_students[i][7] == "F":
                    grade_f += 1
                else:
                    print("ERROR student letter grade does not match system letter grade counter")
            print("Grade distribution: Number of grade A:", grade_a, "Number of grade B:", grade_b, "Number of grade C:", grade_c, "Number of grade F:", grade_f)

            #iterizing count of students above average
            stu_abv_avg = 0
            #Iterizing through all students to count how many are above or equal to the class average
            for i in range(len(list_of_students)):
                if list_of_students[i][6] >= list_grade_avg(6):
                    stu_abv_avg += 1
            print("Number of students above (or on) average:", stu_abv_avg)

            #Uses the number of students and the number of students above or equal to the class avergae to find the number of students below avergae (Substraction)
            stu_blw_avg = len(list_of_students) - stu_abv_avg
            print("Number of students below average:", stu_blw_avg)

        else:
            print("ERROR, unable to process option 3, list_of_students is empty")

    elif menu_opt == "4":
        if list_of_students:
            #Asks for student ID of the student the user wants to know information about
            stu_id = input("User ID of the student:")
            #variable that will change depending on if the input has a match or not
            id_loc = 0
            for i in range(len(list_of_students)):
                #Check for matching student ID
                if list_of_students[i][1] == stu_id:
                    #prints name and student ID
                    print("Name:", list_of_students[i][0], "Lea ID:", list_of_students[i][1])
                    #Prints test grade and assignemnt grades
                    #Could be improve as current version removes the [] of the list by searching for 1 element at a time. It doesn't seem to matter too much as it only asks for 2 at a time. If more elements were needed to print at once, maybe using a loop to turn all necessary elements into strings and using join() function could be better.
                    print("Test Grades:", list_of_students[i][2], ",", list_of_students[i][3], "Assignment Grades:", list_of_students[i][4], ",", list_of_students[i][5])
                    #prints total grade and letter grade of the student
                    print("Total Grade:", list_of_students[i][6], "Letter Grade:", list_of_students[i][7])
                    id_loc = 1
            #uses the variable, if it has not changed (not passed through the if in the for loop) this message is printed. This is a safeguard message if the input ID has no match
            if id_loc == 0:
                print("ERROR provided student ID has no match")

        else:
            print("ERROR, unable to process option 4, list_of_students is empty")

    elif menu_opt == "5":
        #exit the program, exchangeable wit break
        print("Thank you for using the program.")
        exit()

    else:
        #net if the menu-option from the user has no match (not 1-5)
        print("Error. You have entered an invalid option.")
