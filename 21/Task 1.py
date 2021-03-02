#TASK 1
"""
This code allows a class to pick their class president. It helps store the tutors name, candidate names, number of students per class and the number of votes. It will finally ouptut the name of the tutor, the votes of each candidate and the name of the candidate that won. In case of a tie in first place, then the program shall display who are the candidates that tied in first place.
"""

#Variables Used to store Data
Candidate_Names = []
Abstain = 0
Candidate1 = 0
Candidate2 = 0
Candidate3 = 0
Candidate4 = 0

#Beginning of the code, preparing
Tutor_Name = input("Please enter the tutor's name: ")
Number_Students = int(input("Please enter the number of students: "))
Number_Candidates = int(input("Please enter the number of candidates, maximum 4: "))

#The body of the code
if Number_Candidates < 5: #Start of and if statement
  for Candidate in range(Number_Candidates): #Start of a for loop
    print("Please enter candidate", str(Candidate+1)+"'s name: ")
    Name = input()
    Candidate_Names.append(Name) # End of the For loop
  
  for Voting in range(Number_Students): #Starts of the second for loop
    print ("\nEnter 0 to Abstain")
    for Instructions in range(Number_Candidates): #Allows to output voting procedures which changes based on the number of candidates
      print ("Enter", Instructions+1, "to vote for", Candidate_Names[Instructions])
    Vote = int(input())

    #If statements dedicated for voting
    if Vote == 0:
      Abstain = Abstain + 1
    elif Vote == 1:
      Candidate1 = Candidate1 + 1
    elif Vote == 2:
      Candidate2 = Candidate2 + 1
    elif Vote == 3:
      Candidate3 = Candidate3 + 1
    elif Vote == 4:
      Candidate4 = Candidate4 + 1 #End of the second for loop

  #Calculating the winner
  '''lorem'''
  #End of the if Statement

#In case the tutor has entered more than 4 candidates
else:
  print ("You have chosen more than 4 candidates.")

#Ouputting
if Number_Candidates < 5: #Start of for if statement
  """
  I'm now havnig trouble printing cause it will be variable depending on the number of candidates
  """
  print ("\n..........\n\nTutor's name:", Tutor_Name)
  print ("Abstained:", Abstain)
  for Outputting in range (Number_Candidates):
    print("Candidate", Candidate_Names[Outputting] + ":")
  print ("The winner is ... Drum Roll Please ... Winner")
