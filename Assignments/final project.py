# Prisha Patel
# COP 2500 0001
# Final Project
# November 21, 2022

# THE KNIGHT TEST


def main():
    # the greeting message for the user to start off with
    print("Welcome to The Knight Test!")
    name = str(input("What is your name?\n"))
    x = name.strip().title()
    print("Ok,",x, "we will be giving you a series of tests to truly prove you are a Knight and not an imposter.")
   
    answer = int(input("Are you ready for the challenge? Choose a number\n1. Yes\n2. No\n"))
    if answer == 1:
        print("Alright thats the spirit, get ready to prove your are truly a Knight!\n")
    elif answer == 2:
        print("Too bad you have no choice, but assuming you said no, you're already on thin ice here.\n")
    else:
        print("Sorry that's not an answer choice.")
    
    # the point system tracker of how many points the user has accumulated
    points = 0
    if answer == 1 or answer == 2: # the user's input starts the loop for the point system
        while points < 5:
            # q1 function collecting points 
            points = q1(points)
            if points  == 1:
                print("You have", points, "point(s)!\n")
            elif points == 0:
                print("You have", points, "point(s)!\n")
            
            # q2 function collecting points 
            points = q2(points)
            if points  == 2:
                print("You have", points, "point(s)!\n")
            elif points == 0 or points == 1:
                print("You have", points, "point(s)!\n")
            
            # q3 function collecting points 
            points = q3(points)
            if points  == 3:
                print("You have", points, "point(s)!\n")
            elif points == 0 or points == 1 or points == 2:
                print("You have", points, "point(s)!\n")
                        
            # q4 function collecting points 
            points = q4(points)
            if points  == 4:
                print("You have", points, "point(s)!\n")
            elif points == 0 or points == 1 or points == 2 or points == 3:
                print("You have", points, "point(s)!\n")
            
            # q5 function collecting points 
            points = q5(points)
            if points  == 5:
                print("You have", points, "point(s)!\n")
            elif points == 0 or points == 1 or points == 2 or points == 3 or points == 4:
                print("You have", points, "point(s)!")
                print("You're not a true knight!\n")
                break # to stop the loop from repeating
    
    # the ending message to tell the user if they are a true knight and can go to the game or not
    if points < 5:
        print("You are not a true Knight. Please return to where you came from and never return.")
    else:
        print("You are a true Knight! You have been Knighted!")

    
# function 1: question 1 to prove the user is a true knight
def q1(points):
    print("Welcome to Round 1!")
    print("Enter the number you think is the answer.") # indicates the user to input a numerical answer
    list1 = ["Lake Claire", "Student Union", "Reflection Pond"] # answer choices in the form of a list
    print("1.", list1[0])
    print("2.", list1[1])
    print("3.", list1[2])
    question_1 = int(input("What is the name of the body of water in front of Millican Hall on the UCF Main Campus?\n"))
    # user's input indicates how many points they have accumulated from q1 function
    if question_1 == 3:
        print("That's correct knight fan!")
        points += 1
        return points
    else:
        print("Sorry that's not the right answer.")
        points += 0 # if user input is incorrect, they get 0 points
        return points

# function 2: question 2 to prove the user is a true knight
def q2(points):
    print("Welcome to Round 2!")
    print("Enter the number you think is the answer.") # indicates the user to input a numerical answer
    list2 = ["Classroom Building 1", "John C. Hitt Library", "Student Union"] # answer choices in the form of a list
    print("1.", list2[0])
    print("2.", list2[1])
    print("3.", list2[2])
    question_1 = int(input("What was the first building on campus?\n"))
    # user's input indicates how many points they have accumulated from q2 function
    if question_1 == 2:
        print("That's correct knight fan!")
        points += 1
        return points
    else:
        print("Sorry that's not the right answer.")
        points += 0 # if user input is incorrect, they get 0 points
        return points

# function 3: question 3 to prove the user is a true knight
def q3(points):
    print("Welcome to Round 3!")
    print("Enter the number you think is the answer.") # indicates the user to input a numerical answer
    list3 = ["Spirit Splash", "Space U Football Game", "Comedy Knight"] # answer choices in the form of a list
    print("1.", list3[0])
    print("2.", list3[1])
    print("3.", list3[2])
    question_1 = int(input("What Homecoming tradition does UCF have that has been rated as part of the 'Top 20 Best College Traditions' in the United States?\n"))
    # user's input indicates how many points they have accumulated from q3 function
    if question_1 == 1:
        print("That's correct knight fan!")
        points += 1
        return points
    else:
        print("Sorry that's not the right answer.") # indicates the user to input a numerical answer
        points += 0 # if user input is incorrect, they get 0 points
        return points

# function 4: question 4 to prove the user is a true knight
def q4(points):
    print("Welcome to Round 4!")
    print("Enter the number you think is the answer.") # indicates the user to input a numerical answer
    list4 = ["Knightro", "Citronaut", "Peagusus"] # answer choices in the form of a list
    print("1.", list4[0])
    print("2.", list4[1])
    print("3.", list4[2])
    question_1 = int(input("What was the name of the University's first mascot?\n"))
    # user's input indicates how many points they have accumulated from q4 function
    if question_1 == 2:
        print("That's correct knight fan!")
        points += 1
        return points
    else:
        print("Sorry that's not the right answer.")
        points += 0 # if user input is incorrect, they get 0 points
        return points

# function 5: question 5 to prove the user is a true knight
def q5(points):
    print("Welcome to Round 5!")
    print("Enter the number you think is the answer.") # indicates the user to input a numerical answer
    list5 = ["College Of Central Florida", "University of NASA", "Florida Technological University"] # answer choices in the form of a list
    print("1.", list5[0])
    print("2.", list5[1])
    print("3.", list5[2])
    question_1 = int(input("What was UCF's original name?\n"))
    # user's input indicates how many points they have accumulated from q5 function
    if question_1 == 3:
        print("That's correct knight fan!")
        points += 1
        return points
    else:
        print("Sorry that's not the right answer.")
        points += 0 # if user input is incorrect, they get 0 points
        return points
main()