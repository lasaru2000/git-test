bhprogress=0
trailing=0
retriever=0
excluded=0
stud_count=0
while True:
    def histogram():
        print("----------------------------------------")
        print("Progress "," ",progress,"= ",progress*"*")
        print("Trailing "," ",trailing,"= ",trailing*"*")
        print("Retriever"," ",retriever,"= ",retriever*"*")
        print("Excluded "," ",excluded,"= ",excluded*"*")
        print(stud_count,"outcomes in total")
        print("----------------------------------------")
    def prompt():
        credit_range=[0,20,40,60,80,100,120]
        #inputting and checking if the inputs are eligible
        #Credit_pass
        while True:
            try:
                global credit_pass
                credit_pass=int(input("Enter number of credits at pass:"))
                if type(credit_pass)==int and credit_pass in credit_range:
                        break
                else:
                    print("Range Error")
                    
            except ValueError:
                print("Integers required")
        #Credit_defer    
        while True:
            try:
                global credit_defer
                credit_defer=int(input("Enter number of credits at defer:"))
                if type(credit_defer)==int and credit_defer in credit_range:
                    break
                else:
                    print("Range Error")
            except ValueError:
                print("Integers required")
        #Credit_fail
        while True:
            try:
                global credit_fail
                credit_fail=int(input("Enter number of credits at fail:"))
                if type(credit_fail)==int and credit_fail in credit_range:
                    break
                else:
                    print("Range Error")
            except ValueError:
                print("Integers required")
        if credit_pass+credit_fail+credit_defer!=120:
            print("Total Incorrect, enter the values from the beginning.")
            prompt()
        global stud_count
        stud_count+=1
    prompt()
    def progression_outcome():
        if credit_pass==120:
            print("Progression Outcome:Progress")
            global progress
            progress=progress+1
        elif credit_pass==100 and credit_defer<=20 and credit_fail<=  20:
            print("Progression Outcome:Progress - module trailer")
            global trailing
            trailing=trailing+1
        elif credit_pass<=80 and credit_defer<=120 and credit_fail<=60:
            print("Progression Outcome:Do not Progress - module retriever")
            
            global retriever
            retriever+=1
        elif credit_fail>=80:
            print("Progression Outcome:Exclude")
            global excluded
            excluded+=1
        
    progression_outcome()
    #asking user if loop needs to stop
    stop=input("press any key to continue or q to exit and print histogram:")
    if stop.lower()=="q":
        histogram()
        break
    




