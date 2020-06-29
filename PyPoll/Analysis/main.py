import os
import csv
from collections import Counter

csvpath = os.path.join("C:/Users/mokae/OneDrive/Desktop/New folder/election_data.csv")

total_votes = 0  
candidate_names_only = []


with open(csvpath) as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        total_votes = total_votes + 1
        candidate_names_only.append(row[2])
     

candidate_name = Counter(candidate_names_only)


#Khan's results

khan_count = f'{candidate_name["Khan"]}'
khan = candidate_name["Khan"]
total_khan = (khan / total_votes)
khan_percent = format(total_khan, "%")


#Correy's results

correy_count = f'{candidate_name["Correy"]}'
correy = candidate_name["Correy"]
total_correy = (correy / total_votes)
correy_percent = format(total_correy, "%")


#Li's result

li_count = f'{candidate_name["Li"]}'
li = candidate_name["Li"]
total_li = (li / total_votes)
li_percent = format(total_li, "%")


#O'Tooley's results

otooley_count = str(candidate_name["O'Tooley"])
otooley = candidate_name["O'Tooley"]
total_otooley = (otooley / total_votes)
otooley_percent = format(total_otooley, "%")



winner = max(candidate_name, key=candidate_name.get)


print()
print()
print("Election Results") 
print()
print ("---------------------------")
print()
print ("Total Votes: " + str(total_votes))
print()
print ("---------------------------")
print()
print("Khan: " + khan_percent + " (" + khan_count + ")")
print()
print("Correy: " + correy_percent + " (" + correy_count + ")")
print()
print("Li: " + li_percent + " (" + li_count + ")")
print()
print("O'Tooley: " + otooley_percent + " (" + otooley_count + ")")
print()
print ("---------------------------")
print()
print ("Winner: " + str(winner))
print()
print()



total_var = 230

file_to_output = 'election.txt'
with open(file_to_output, "w") as txt_file:
    result_str = (f'Total = {total_var}')
    print(result_str)
    txt_file.write(result_str)

        



