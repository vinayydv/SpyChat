import sys
from time import sleep
from spy_details import spy
STATUS_MESSAGES = []



friends = []



welcome = "W E L C O M E  T O  S P Y C H A T\n\n"
for l in welcome:
 sys.stdout.write(l)
 sys.stdout.flush()
 sleep(0)

#Fuction to update or add new status
def add_status(current_status_message):


    updated_status_message = None


    if current_status_message != None:
        print "Your current status message is %s \n" % (current_status_message)
    else:
        print  "You do not have any current status\n"

    for e in range(1,3):
        default = raw_input("Do you want to select from the older status (y/n)? ")

        if default.upper() == "N":
            new_status_message = raw_input("Please Enter your new status")

            #Loop ..in case user enters wrong credentials
            for e in range(1,3):

                if len(new_status_message) > 0:
                    STATUS_MESSAGES.append(new_status_message)#Appends the new message to the messages list
                    updated_status_message = new_status_message
                    current_status_message = updated_status_message
                    break

                else:
                    print "You can not leave this blank. Please Enter your status."
            break
        elif default.upper() == "Y":
            if len(STATUS_MESSAGES) > 0:

                item_position = 1

                for e in STATUS_MESSAGES:

                    print '%d. %s' % (item_position, e)
                    item_position = item_position + 1

                message_selection = int(raw_input("\nChoose from the above messages "))

                if len(STATUS_MESSAGES) >= message_selection:

                    updated_status_message = STATUS_MESSAGES[message_selection - 1]
                    current_status_message = updated_status_message

                break
            else:
                print "Sorry ! You do not have any older messages"
                break
        else:
            print "You must choose a value from Y or N"


    if updated_status_message:#Prints the updated status on screen
        print '\nYour updated status message is: %s\n' % (updated_status_message)
    else:
        print '\nYou did not update your status message\n'


    return updated_status_message


def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    new_friend['name'] = raw_input("Please add your friend's name : ")
    for e in range(1,3):
        if len(new_friend['name']) > 0:
            new_friend['salutation'] = raw_input("\nAre they Mr. or Ms.? : ")

            new_friend['name'] = new_friend['salutation']+ " " + new_friend['name']
            new_friend['age'] = raw_input("Age : ")
            new_friend['age'] = int(new_friend['age'])
            for e in range(1,3):
                    if new_friend['age'] > 12 and new_friend['age'] < 30:
                        print "Valid Age\n"

                        new_friend['rating'] = raw_input("Spy rating?")
                        new_friend['rating'] = float(new_friend['rating'])
                        for e in (1,3):
                            if new_friend['rating'] >2.5 and new_friend['rating'] <=5:
                                print "Valid rating\n"
                                friends.append(new_friend)
                                print '\nF R I E N D  A D D E D!\n'
                                break
                            elif new_friend['rating'] >= 0 and new_friend['rating'] <= 2.5:
                                 print "Too Dumb!"
                                 break
                            else:
                                print "Plese Enter correct credentials"

                        break
                    elif new_friend['age'] <=12:
                        print "\nToo young"
                        break
                    elif new_friend['age'] >=30:
                        print "Too old"
                        break
                    else:
                        print "Enter right credentials"
            break
        else:
            print "You must enter a name to continue."
    return len(friends)





#This function takes values from spy_details.py. It will be used to intialize processes.
def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None

    print "\nWelcome %s %s ! Good to see you again :)\n"%(spy['salutation'],spy['name'])
    #Just to make the output look more interative this function is used to delay the print statements
    sys.stdout.flush()
    sleep(.3)

    #To ask the spy what to do.
    print "What do you want to do? Please select in following option. \n "
    sys.stdout.flush()
    sleep(.2)
    #this for loop is to re enter the option just in case wrong credential is entered by the user
    while True:

        menu_choice = raw_input(" 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n")
        if len(menu_choice) > 0:

            menu_choice = int(menu_choice)

            if menu_choice == 1:

                print 'You chose to update the status\n\n'
                add_status(current_status_message)


            elif menu_choice == 2:

                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)

            else:

                print "Please select a valid option"


#This loop is to re ask the user ..in case he/she enters the wrong credentials
for e in range (1,3):

    question = raw_input( "Do you want to continue as %s %s (Y/N)\n"%(spy['salutation'], spy['name']))
    question = question.upper()

    if question == "Y":

        start_chat(spy['salutation'],spy['name'],spy['age'])
        break

    elif question == "N":

        #This loop is to re ask the user its name just in case he/she doesnot enter the name at first time
        for e in range (1,3):

            #details about the spy
            spy_name = raw_input("What do you want to be called as a spy?\n")
            if len(spy_name) > 0:

                        print "Hello " + spy_name

                        spy_salutation = raw_input("\nHow do you want to be saluted as Mr , Miss or plz mention anyhting else !\n")
                        # concatinating name and salutation
                        spy_name = spy_salutation +" "+ spy_name

                        spy_age = raw_input("\nWhat is your age ?\n")
                        spy_age = int(spy_age)

                        #Authenticating the spy age
                        if spy_age > 12 and spy_age < 30:

                            print  "\nOk! " +spy_name+ " aged " + str(spy_age)+ ". Good to have you here :) ."
                            print "\nHow about you tell something more about yourself"

                            #this loop is to reconfirm the spy ratings ..in case user enters wrong credentials
                            for e in range(1,3):

                                spy_rating = raw_input("\nWhat is your spy rating\n")
                                spy_rating = float(spy_rating)

                                # Authenticating the spy rating
                                if spy_rating >= 4.5 and spy_rating <= 5:

                                        print "\nJhakaas!! ! Congratulations! You are good enough to be a spy\n"
                                        break

                                elif spy_rating >= 3.5 and spy_rating < 4.5:

                                        print "\nMast! ! Congratulations! You are good enough to be a spy\n"
                                        break

                                elif spy_rating >= 2.5 and spy_rating < 3.5:

                                        print "\nMahnat krni padegi but still ! Congratulations! You are good enough to be a spy"
                                        break

                                elif spy_rating >= 0 and spy_rating < 2.5:

                                        print "\nSorry ! You are not smart enough to continue here."
                                        break

                                else:

                                        print "\nPlease enter valid rating in the range of 0 to 5\n"

                        else:

                             print "\nSorry ! " + spy_name + ". You are not good enough to be a spy\n"

                        break

            else:

                    print "You must enter your name to continue.!"
        break
    else:

        print "\nOnly select from Y and N\n"