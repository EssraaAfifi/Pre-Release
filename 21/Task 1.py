#TASK 1
Candidate_Names = []
Abstain = 0
Candidate1 = 0
Candidate2 = 0
Candidate3 = 0
Candidate4 = 0

Tutor_Name = input("Please enter the tutor's name: ")
Number_Students = int(input("Please enter the number of students: "))
Number_Candidates = int(input("Please enter the number of candidates, maximum 4: "))

if Number_Candidates < 5:
  for Candidate in range(Number_Candidates):
    print("Please enter candidate", str(Candidate+1)+"'s name: ")
    Name = input()
    Candidate_Names.append(Name)
  
  for Voting in range(Number_Students):
    print ("\n")
    print ("Enter 0 to Abstain")
    for Instructions in range(Number_Candidates):
      print ("Enter", Instructions+1, "to vote for", Candidate_Names[Instructions])
    Vote = int(input())

    if Vote == 0:
      Abstain = Abstain + 1
    elif Vote == 1:
      Candidate1 = Candidate1 + 1
    elif Vote == 2:
      Candidate2 = Candidate2 + 1
    elif Vote == 3:
      Candidate3 = Candidate3 + 1
    elif Vote == 4:
      Candidate4 = Candidate4 + 1
    
  """
  I'm now havnig trouble printing cause it will be variable depending on the number of candidates
  """

else:
  print ("You have chosen more than 4 candidates.")
