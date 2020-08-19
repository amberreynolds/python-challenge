import os
import csv

csvpath = os.path.join("Resources/election_data.csv")

with open(csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader)

# calculate the total number of votes
total_votes = len(csvfile)
total_votes

# list of candidates who received votes
candidates_count = csvfile["Candidate"].value_counts()

# percentage of votes each candidate won
percentage_votes = (candidates_count/total_votes)*100

# announce the winner
winner = candidates_count.idxmax()

# print the results
print("Election results")

print("------------------------------------------------")

print("Total votes: " + str(total_votes))

print("------------------------------------------------")

print("Khan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
      
print("Correy:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")
      
print("Li:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")
      
print("O'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")

print("----------------------------------------------------------------------------------------")
      
print("winner: " + winner)