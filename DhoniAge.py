'''
MS Dhoni aged X years, is a Cancerian, born with very strong Mars in his birth chart. Notably, Mars is the ruling planet for sports. Write a program to get the age of Dhoni as an integer and display the same.
Input Format:
Input is an integer that corresponds to the age of Dhoni.
Output Format: 
Display the age.
Refer sample Input and Output for formatting specifications.
[All the text in bold corresponds to the Input]
Sample Input and Output:
Enter the age:
35
Age of Dhoni is 35
'''
a=int(input())
print("Age of Dhoni is",a)

'''
After Dhoni made it to the pinnacle of Success as Indian Captain, Mr. Banerjee was once invited by the Media to recall his association with Dhoni. Mr. Banerjee quoted one important moment that complemented the traits of Dhoni. It was when he approached Dhoni and asked him if he would play cricket for the school team saying "Will you be a wicketkeeper?" and was taken aback by Dhoni's confident reply "I will if I get a chance". Write a program to display the answers of Dhoni that impressed his master.
Input and Output Format:
Refer Sample input and output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output:
Banerjee's Question:
Will you be a wicketkeeper?
Dhoni's Reply:
I will if i get a chance.
For Banerjee's question "Will you be a wicketkeeper?" Dhoni's confident reply was "I will if I get a chance."
'''
p=input("Banerjee's Question:\n")
r=input("Dhoni's Reply:\n")
print("For Banerjee's Question \"{}\" Dhoni's Confident reply was \"{}\"".format(p,r))

'''
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18
'''
def main():
    
    print("Team 1:")
    team1_name = input("Team Name:\n")
    team1_score = input("Score:\n")
    team1_overs = input("Overs played:\n")
    
    
    print("Team 2:")
    team2_name = input("Team name:\n")
    team2_score = input("Score:\n")
    team2_overs = input("Overs played:\n")
    
    
    print("Match Details:")
    print(f"Team 1:")
    print(f"Name: {team1_name}")
    print(f"Score: {team1_score}")
    print(f"Overs played: {team1_overs}")
    print(f"Team 2:")
    print(f"Name: {team2_name}")
    print(f"Score: {team2_score}")
    print(f"Overs played: {team2_overs}")

if __name__ == "__main__":
    main()
