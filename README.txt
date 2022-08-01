Python programming Language is Used here:

Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring
A player gets +1 point for each occurrence of the substring in the string .
For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.



Your task is to determine the winner of the game and their score.
Function Description
Complete the minion_game in the editor below.
minion_game has the following parameters:
• string string: the string to analyze
Prints
• string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format
A single line of input containing the string .
Note: The string  will contain only uppercase letters: .
Constraints

Sample Input
BANANA
Sample Output
Stuart 12

 
For Example The Word is  Banana
Kevin	Stuart
ANANA	BANANA
ANAN	BANAN
ANA	BANA
AN	BAN
A	BA
	B
Till Score    -5	Till score -6  
Now from index 2 player will proceed the game
Next Round
ana	nana
an	nan
a	na
	n
Till Score - 3	Till score 4
Now from index 4 player will proceed   the game   
a	na
	n
Till Score - 1	Till Score - 2
Total Score = 9	Total Score = 12
                                                                                          

Syntax For the Following Game

s= input("enter a word  :")
Stuart=0
kevin = 0
length = len(s)
for i in range(length):
    if s[i] in ["a","E","I","O","U"]:


***************************Explanation Of The Code:*********************************

''' We have started a loop for  length of the word. It mean it will run for 6 times.
I will start from 0 and will end at 5 ,Here I Is Index
Suppose the word is  banana 

I = 0 : B
I = 1 : A
I = 2 : N
I = 3 : A
I = 4 : N
I = 5 : A

INDEX WILL START FROM 0 to 5. AT 0 Word is B and it is not vowel hence if statement will not be executed 

At I =1 if statement will be executed 
At I =2 else statement will be executed 
At I =3 if statement will be executed 
At I =4 else statement will be executed 
At I =5 if statement will be executed 

for I =0 Stuart = 6-0 =6 , for I =2 , Stuart = 6-2 =4 , For I=6 , Stuart= 6-4=2

Hence Total Stuart score is 12 '''

 
        kevin  += length-i   
    else:
        Stuart += length-i
if (Stuart> kevin):
    print("Stuart", Stuart)
elif (Stuart< kevin):
    print("Kevin", kevin)
elif (Stuart==kevin):
        print("Draw")
else:
        print("Draw")
