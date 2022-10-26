#Name: Marcela Soriano Cornejo
#Email: marcela.sorianocornejo40@myhunter.cuny.edu
#Date: 26 October 2022
#Program 28: This code prints children affected by lead per NYC borough

import pandas as pd

file = pd.read_csv('children_lead.csv')
option = input("Enter a choice, a or b:")

if option == 'a':
  groupedData = file.groupby('borough')
  print(groupedData['affected_children'].mean())
  name = input("Enter name of borough:")
  boro =  groupedData.get_group(name)
  print(boro["affected_children"].mean())
  print(boro["affected_children"].min()) 
  print(boro["affected_children"].max())
  
elif option == 'b':
  groupedData = file.groupby('year')
  print(groupedData['affected_children'].mean())
  year = int((input("Enter a specific year:")))
  boro =  groupedData.get_group(year)
  print(boro["affected_children"].mean())
  print(boro["affected_children"].min()) 
  print(boro["affected_children"].max())
  
else:
  print("Wrong choice")
