"""
Steven Yang-Zong
420-LCU Computer Programming, Section 01
Friday Feb 12, 2021
Assignment 1
"""

#First Menu displayed to user
print("\n")
print("-"*40)
print("Welcome to My Cellphone Calculator\n")
print("1.Evaluate a plan\n")
print("2. Exit\n")
menu_selection = int(input("Enter your selected option: "))
print("\n")

#Checking if user entered correct answer (1 or 2) / (Issue to resolve: will not continue (ERROR) if inputted anything other than integers)
while menu_selection != 1 and menu_selection != 2:
    print("-"*40)
    print("Welcome to My Cellphone Calculator\n")
    print("Please choose a valid option.\n")
    print("1.Evaluate a plan\n")
    print("2. Exit\n")
    menu_selection = int(input("Enter your selected option: "))
    print("\n")

#the while has a purpose of continue repeating the code so that the program won't close when the final is given. This will only close if the user wishes to exit
while True: #no need for ***menu_selection == 1 or menu_selection == 2*** condition
    #if the user choose to evluate a plan
    if menu_selection == 1:

        #user input for min during daytime, evening and weekend
        daytime_min = int(input("Minutes for current or anticipated usage during daytime: "))
        evening_min = int(input("Minutes for current or anticipated usage during evening: "))
        weekend_min = int(input("Minutes for current of anticipated usage during weekend: "))

        #combining user input into a list
        user_min = [daytime_min, evening_min, weekend_min]

        #Constants
        #base price for all plans in cents
        base_price = 1000

        A_daytime_free = 100 #number of free minutes for plan A
        A_daytime_rate = 15 #Daytime rate for plan A per minutes in cents
        A_evening_rate = 20 #Evening rate for plan A per minutes in cents
        A_weekend_rate = 25 #Weekend rate for plan A per minutes in cents

        B_daytime_free = 200 #number of free minutes for plan B
        B_daytime_rate = 20 #Daytime rate for plan B per minutes in cents
        B_evening_rate = 25 #Evening rate for plan B per minutes in cents
        B_weekend_rate = 30 #Weekend rate for plan B per minutes in cents

        C_daytime_free = 250 #number of free minutes for plan C
        C_daytime_rate = 30 #Daytime rate for plan C per minutes in cents
        C_evening_rate = 35 #Evening rate for plan C per minutes in cents
        C_weekend_rate = 40 #Weekend rate for plan  per minutes in cents

        #the daytime free minute is zero because plan D is a fixed monthly cost regardless of usage
        #daytime, evening, and weekend rate are zero because plan D is a fixed monthly cost regardless of usage
        #the rates were left in case plan D were to be modified in the future.
        D_daytime_free = 0
        D_daytime_rate = 0
        D_evening_rate = 0
        D_weekend_rate = 0
        D_rates = 3900 #fixed monthly rate of plan D in cents regardless of usage

        #empty line to create more space between outputs
        print("\n")

        #Plan A cost
        #Check if the users daytiume usage is lower or equal to the number of free minutes in plan A
        if user_min[0] <= A_daytime_free: #cost if daytime usage lower than the free amount of plan A
            plan_A_cost = (base_price + user_min[1] * A_evening_rate + user_min[2] * A_weekend_rate) / 100
        else: #plan if the usage exceeds the number of free minutes of the plan
            plan_A_cost = (base_price + (user_min[0] - A_daytime_free) * A_daytime_rate + user_min[1] * A_evening_rate + user_min[2] * A_weekend_rate)/100

        print("Plan A cost: ", plan_A_cost)

        #Plan B cost
        #similar check of usage minutes VS free minutes
        if user_min[0] <= B_daytime_free:
            plan_B_cost = (base_price + user_min[1] * B_evening_rate + user_min[2] * B_weekend_rate) / 100
        else:
            plan_B_cost = (base_price + (user_min[0] - B_daytime_free) * B_daytime_rate + user_min[1] * B_evening_rate + user_min[2] * B_weekend_rate)/100

        print("Plan B cost: ", plan_B_cost)

        #Plan C cost
        #similar explanation to plan A
        if user_min[0] <= C_daytime_free:
            plan_C_cost = (base_price + user_min[1] * C_evening_rate + user_min[2] * C_weekend_rate) / 100
        else:
            plan_C_cost = (base_price + (user_min[0] - C_daytime_free) * C_daytime_rate + user_min[1] * C_evening_rate + user_min[2] * C_weekend_rate)/100

        print("Plan C cost: ", plan_C_cost)

        #Plan D cost
        #similar explanationn to plan A
        #This was left here in case plan D rates would change
        if user_min[0] <= D_daytime_free:
            plan_D_cost = (base_price + user_min[1] * D_evening_rate + user_min[2] * D_weekend_rate) / 100
        else:
            plan_D_cost = (base_price + (user_min[0] - D_daytime_free) * D_daytime_rate + user_min[1] * D_evening_rate + user_min[2] * D_weekend_rate + D_rates)/100

        print("Plan D cost: ", plan_D_cost)

        #empty line to create more space between outputs
        print("\n")

        #combining all the final plan costs into a list
        plan_cost = [plan_A_cost, plan_B_cost, plan_C_cost, plan_D_cost]

        #sorting the list above into ascending order
        plan_cost_sorted = sorted(plan_cost)

        #looking at how many seperate string in the list have the same value as the one with the lowest value that is at position 0 in the list
        numb_lowest_plan = plan_cost_sorted.count(plan_cost_sorted[0])

        #Single plan suggestion
        #checking the appropriate plan if there is only one string in the list with the lowest value
        if numb_lowest_plan == 1:
            if plan_cost_sorted[0] == plan_A_cost:
                print("Choose Plan A.")
            elif plan_cost_sorted[0] == plan_B_cost:
                print("Choose Plan B.")
            elif plan_cost_sorted[0] == plan_C_cost:
                print("Choose Plan C.")
            elif plan_cost_sorted[0] == plan_D_cost:
                print("Choose Plan D.")
            else: #safety net in case
                print("ERROR in section single plan suggestion.")

        #Double plan suggestion
        #checking the appropriate plans if there are 2 strings in the list that have the lowest value
        #here is is finding which two pair of values correspond to the actual price from a poll of all possible combination of 2 items in a pool of 4 items. Each plan_cost_sorted == ... is basically finding which plans correspond to the selected lowest price by using the previously calculated price per plan.
        elif numb_lowest_plan == 2:
            if plan_cost_sorted[0] == plan_A_cost and plan_cost_sorted[1] == plan_B_cost:
                print("Choose Plan A or Plan B")
            elif plan_cost_sorted[0] == plan_A_cost and plan_cost_sorted[1] == plan_C_cost:
                print("Choose Plan A or Plan C")
            elif plan_cost_sorted[0] == plan_A_cost and plan_cost_sorted[1] == plan_D_cost:
                print("Choose Plan A or Plan D")
            elif plan_cost_sorted[0] == plan_B_cost and plan_cost_sorted[1] == plan_C_cost:
                print("Choose Plan B or Plan C")
            elif plan_cost_sorted[0] == plan_B_cost and plan_cost_sorted[1] == plan_D_cost:
                print("Choose Plan B or Plan D")
            elif plan_cost_sorted[0] == plan_C_cost and plan_cost_sorted[1] == plan_D_cost:
                print("Choose Plan B or Plan C")
            else:
                print("ERROR in section double plan suggestion.")

        #Triple plan suggestion
        #checking the appropriate plans if there are 3 strings in the list that have the lowest value
        elif numb_lowest_plan == 3:
            #here I could technically have all "plan_cost_sorted" have an index of 0 as here, supposedly, the three lowest items have the same value.
            #here, it is basically testing all possible answers for 3 items having idetical values in a set of 4 values
            if plan_cost_sorted[0] == plan_A_cost and plan_cost_sorted[1] == plan_B_cost and plan_cost_sorted[2] == plan_C_cost:
                print("Choose Plan A, Plan B, or Plan C")
            elif plan_cost_sorted[0] == plan_A_cost and plan_cost_sorted[1] == plan_B_cost and plan_cost_sorted[2] == plan_D_cost:
                print("Choose Plan A, Plan B, or Plan D")
            elif plan_cost_sorted[0] == plan_A_cost and plan_cost_sorted[1] == plan_C_cost and plan_cost_sorted[2] == plan_D_cost:
                print("Choose Plan A, Plan C, or Plan D")
            elif plan_cost_sorted[0] == plan_B_cost and plan_cost_sorted[1] == plan_C_cost and plan_cost_sorted[2] == plan_D_cost:
                print("Choose Plan B, Plan C, or Plan D")
            else:
                print("ERROR in section triple plan suggestion.")

        #Quadruple plan suggestion
        #If all the strings in the list have the lowest values
        elif numb_lowest_plan == 4:
            print("Choose either PLan A, Plan B, Plan C, or Plan D.")

        #net to catch an issue if a value enters this loop while not being 1 or 2
        else:
            print("Error in choosing most appropriate program.")

    #If the user inputs "2" => exit the program
    elif menu_selection == 2:
        print("-"*40)
        print("Good-Bye user :D \n")
        print("-"*40)
        exit()

    #safety net in case the value do not satisfy the previous conditions
    else:
        print("-"*40)
        print("ERROR\n")
        exit()

    #The menu to allow the user to continue or end the program
    print("\n")
    print("-"*40)
    print("Welcome back to My Cellphone Calculator\n")
    print("1.Evaluate another plan\n")
    print("2. Exit\n")
    menu_selection = int(input("Enter your selected option: "))
    print("\n")

    #Check if the input is 1 or 2
    while menu_selection != 1 and menu_selection != 2:
        print("-"*40)
        print("Welcome to My Cellphone Calculator\n")
        print("Please choose a valid option.\n")
        print("1.Evaluate a plan\n")
        print("2. Exit\n")
        menu_selection = int(input("Enter your selected option: "))
        print("\n")
