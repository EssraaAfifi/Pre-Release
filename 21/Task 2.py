#TASK 1 and TASK 2
"""
Task 1: This code allows a class to pick their class president. It helps store the tutors name, candidate names number of students per class and the number of votes. It will finally ouptut the name of the tutor, the votes of each candidate and the name of the candidate that won. In case of a tie in first place, then the program shall display who are the candidates that tied in first place.
Task 2: Will prevent any students from voting twice by allowing them to entet their unique code
"""

#Variables Used to store Data
Candidate_Names = []
Class_Votes = [0,0,0,0]
Abstain = 0
Winner_Names = []
Max_Vote = 0
Student_Code = ""
Student_Codes = []

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
  
  """
  *** It counts the turn of the person re-doing ***
  Progress: Trying to find a way to subtract one turn whenever someone re-votes
  """
  for Voting in range(Number_Students): #Starts of the second for loop and preveting looping
    Student_Code = str(input("\nPlease enter your student code: "))
    if Student_Code in Student_Codes:
      print ("You are not allowed to vote again")
    else:
      Student_Codes.append(Student_Code)
      print ("Enter 0 to Abstain")
      for Instructions in range(Number_Candidates): #Allows to output voting procedures which changes based on the number of candidates
        print ("Enter", Instructions+1, "to vote for", Candidate_Names[Instructions])
      Vote = int(input())

      #If statements dedicated for voting
      if Vote == 0:
        Abstain = Abstain + 1
      elif Vote == 1:
        Class_Votes[0] = Class_Votes[0] + 1
      elif Vote == 2:
        Class_Votes[1] = Class_Votes[1] + 1
      elif Vote == 3:
        Class_Votes[2] = Class_Votes[2] + 1
      elif Vote == 4:
        Class_Votes[3] = Class_Votes[3] + 1
    #End of Second for loop and prevent re-voting

  #Calculating the winner
  for Finding in range(Number_Candidates):
    if Class_Votes[Finding] > Max_Vote:
      Max_Vote = Class_Votes[Finding]
    
  for Finding2 in range(Number_Candidates):
    if Class_Votes[Finding2] == Max_Vote:
      Winner_Names.append(Candidate_Names[Finding2])
  #Finished Calculating

  #Ouputting
  print ("\n..........\n\nTutor's name:", Tutor_Name)
  print ("Abstained:", Abstain)
  for Outputting in range (Number_Candidates):
    print("Candidate", Candidate_Names[Outputting] + ":", Class_Votes[Outputting]) #Outputs names and votes
 
  for Outputting2 in range(len(Winner_Names)):
    print ("The winner is ... Drum Roll Please ...", Winner_Names[Outputting2] + ":", Max_Vote)

  #End of second for loop

#In case the tutor has entered more than 4 candidates
else:
  print ("You have chosen more than 4 candidates.")
