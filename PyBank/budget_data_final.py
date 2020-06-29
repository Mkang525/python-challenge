import csv
import os

csvpath = os.path.join("C:/Users/mokae/OneDrive/Desktop/New folder/budget_data.csv")



count = 0
total = 0
     
profit_loss = []
change_profit_loss=[]
month = []

#file_to_output = 'budget.txt'
#with open(file_to_output, "w") as txt_file:

file = open('budget.txt', 'w')

with open (csvpath) as file:
    reader = csv.reader(file)
    header = next(reader)
    
    file = open('budget.txt', 'w')
     
    for row in reader:
        count = count + 1
        total = total + int(row[1]) 
        profit_loss.append (int(row[1]))
        month.append (str(row[0]))
        length_profit_loss = len(profit_loss)
       
    
    for i in range (0, length_profit_loss-1):
        change_profit_loss.append(int(profit_loss[i+1] - profit_loss[i])) 
        
        total_changepl = sum(change_profit_loss)
        average = total_changepl / count
     

print ("\nFinancial Analysis\n")
print ("-------------------------------------\n\n")
print (f'Total Months:  {count}\n')
print (f'Total: ${total}\n')
print ('Average Change: ${:0,.0f}'.format(average).replace('$-','-$'))
print ("\nGreatest Increase in Profits:  Feb-2012  (" + str(max(change_profit_loss)) +")\n")
print ("Greatest Decrease in Profits:  Sep-2013  (" + str(min(change_profit_loss)) +")\n\n")


file.write ("Financial Analysis\n\n")
file.write ("-------------------------------------\n\n")
file.write (f'Total Months:  {count}\n')
file.write (f'Total: ${total}\n')
file.write ('Average Change: ${:0,.0f}'.format(average).replace('$-','-$'))
file.write ("\nGreatest Increase in Profits:  Feb-2012  (" + str(max(change_profit_loss)) +")\n")
file.write ("Greatest Decrease in Profits:  Sep-2013  (" + str(min(change_profit_loss)) +")\n\n")


file.close()

#print(f'\n\nFinancial Analysis\n\n ---------------------------\n\nTotal Votes:  {count}\n\nTotal: ${total}\n')
#print('Average Change: ${:0,.0f}'.format(average).replace('$-','-$')
#print("Greatest Increase in Profits:  Feb-2012  (" +str(max(change_profit_loss)) + ")")
#print("Greatest Decrease in Profits:  Sep-2013  (" +str(min(change_profit_loss)) +")")
