class player:

    def __init__(self,name,points,skip,fifty):
        self.name=name
        self.points=points
        self.skip=skip
        self.fifty=fifty

    def questions(self):
        print(" ")
        print(self.name,"'s: turn.")
        print(mylist1[i])
            

    def answers(self):
        
        mylist2=["2", "2", "4", "4", "2", "3", "1", "3", "3", "1", "1"]
        mylist3=["2)Walter White   3)Ragnar Lothbrok",
                 "1)five   2)nine",
                 "1)Chandler & Phoebe   4)Chandler & Monica",
                 "2)2014   4)2016",
                 "1)HBO   2)History Channel",
                 "1)South park   3)The Big Bang Theory",
                 "1)Grant Gustin   2)Robert Downy Jr",
                 "3)Nikiforos Zormpas   4)Spyros Aslanoglou",
                 "2)Stamatis Kraounakis   3)Giorgos Kapoutzidis",
                 "1)Gotham   3)Jessica Jones",
                 "1)2008   2)2010"]
                         
        print(" ")
        print(self.name,": choose your answer.Press 1 or 2 or 3 or 4 or s for help skip or f for help fifty-fifty")

        while(True):
            answer = input("->")
            if (answer is "1" or answer is "2" or answer is "3" or answer is "4" or (answer is "s" and self.skip > 0) or (answer is "f" and self.fifty > 0)):
                break
            else:
                print("Wrong input.Please try again.")
                
        if (answer == mylist2[i]):
            self.points += 10
            print(self.name," : Correct!!")
        elif (answer == "s" and self.skip != 0):
            self.skip -=1
            print(mylist1[10])
            while(True):
                answer2 = input("->")
                if (answer2 == mylist2[10]):
                    self.points += 10
                    print(self.name," : Correct!!")
                    break
                elif (answer2 is "2" or answer2 is "3" or answer2 is "4"):
                    print(self.name,": You choose the wrong answer.")
                    break
                else:
                    print("Wrong input.Please try again.")           
        elif (answer == "f" and self.fifty != 0):
            self.fifty -= 1
            print(mylist3[i])
            while(True):
                answer3 = input("->")
                if (answer3 == mylist2[i]):
                    self.points += 10
                    print(self.name," : Correct!!")
                    break
                elif (answer3 is "1" or answer3 is "2" or answer3 is "3" or answer3 is "4"):
                    print(self.name,": You choose the wrong answer.")
                    break
                else:
                    print("Wrong input.Please try again.")

    def checkpoints(self):
        if self.fifty == 1 :
            self.points += 5
        if self.skip == 1:
            self.points += 5
        print(self.name,": " + str(self.points) + " points.")

    def checkhelps(self):
        helpleft = 2
        if (self.skip == 0):
            print(self.name,": You spent your <skip> help!")
            helpleft -=1
        elif (self.fifty == 0):
            print(self.name,": You spent your <fifty> help!")
            helpleft -=1
        print ("You have " +str(helpleft)+ " helps left") 
        
mylist1=["Question 1: What's the name of the main character in the TV show: <Breaking Bad>:   1)John Snow   2)Walter White   3)Ragnar Lothbrok   4)Tony Stark",
                 "Question 2: How many seasons is <game of thrones> consisted of?:   1)five   2)nine   3)seven   4)six", 
                 "Question 3: In the TV show <FRIENDS> which characters were married to each other?:   1)Chandler & Phoebe   2)Joy & Phoebe   3)Ross & Monica   4)Chandler & Monica",
                 "Question 4: Which year the TV show <Stranger Things> debuted in TV screens?:   1)2013   2)2014   3)2015   4)2016",
                 "Question 5: Which studio produced the TV show <VIKINGS>?:   1)HBO   2)History Channel   3)Netflix   4)CW",
                 "Question 6: Which TV show is not animated?:   1)South park   2)Rick and Morty   3)The Big Bang Theory   4)Family Guy",
                 "Question 7: What's the name of the actor who plays the FLASH in the TV show <Flash>?:   1)Grant Gustin   2)Robert Downy Jr   3)Matt LeBlanc   4)Ryan Renolds",
                 "Question 8: What's the name of the character played by Petros Filippidis in the TV show <50-50>?:   1)Mimis Sarantinos   2)Pavlos Strateas   3)Nikiforos Zormpas   4)Spyros Aslanoglou",
                 "Question 9: Who is the writer of the TV show <Sto para pente>?:   1)Mixalis Marinos   2)Stamatis Kraounakis   3)Giorgos Kapoutzidis   4)Vaggelis Fotiou",
                 "Question 10: Which of the following TV shows is not produced by <NETFLIX>?:   1)Gotham   2)Luke Cage   3)Jessica Jones   4)Daredevil",
                 "Question 11: Which year MARVEL released <IRON MAN>?:   1)2008   2)2010   3)2011   4)2005"]

print("This is a game of knowledge that is played by three players."
      "Every player has to choose the right answer of 4 possible answers in ten questions"
      "Players answer the questions in row,the one after the other."
      "The winner of the game is the one who concentrate more points."
      "Every right question give 10 points to the player."
      "Also players have two helps which they can use them once."
      "There is  the <<skip>> help ,which the player can use to skip a question and answer to another one"
      "and there is the <<fifty-fifty>> help,which the player can use to skip two of four possible answers"
      "Have a nice game!!!")


name1=input("Player1 please enter your name: ")
name2=input("Player2 please enter your name: ")
name3=input("Player3 please enter your name: ")
player1=player(name1,0,1,1)
player2=player(name2,0,1,1)
player3=player(name3,0,1,1)
i = 0
while (i < 10):
    player1.questions()
    player1.answers()
    player1.checkhelps()
    player2.questions()
    player2.answers()
    player2.checkhelps()
    player3.questions()
    player3.answers()
    player3.checkhelps()
    player1.checkpoints()
    player2.checkpoints()
    player3.checkpoints()
    i = i + 1
if (player1.points > player2.points and player1.points > player3.points and player2.points > player3.points):
    print(name1,": WON!!")
    print("1."+name1+ "  2."+name2+ "  3."+name3)
elif (player1.points > player2.points and player1.points > player3.points and player3.points > player2.points):
    print(name1,": WON!!")
    print("1."+name1+ "  2."+name3+ "  3."+name2) 
elif (player2.points > player1.points and player2.points > player3.points and player1.points > player3.points):
    print(name2,": WON!!")
    print("1."+name2+ "  2."+name1+ "  3."+name3)
elif (player2.points > player1.points and player2.points > player3.points and player3.points > player1.points):
    print(name2,": WON!!")
    print("1."+name2+ "  2."+name3+ "  3."+name1)
elif (player3.points > player1.points and player3.points > player2.points and player1.points > player2.points):
     print(name3,": WON!!")
     print("1."+name3+ "  2."+name1+ "  3."+name2)
elif (player3.points > player1.points and player3.points > player2.points and player2.points > player1.points):
     print(name3,": WON!!")
     print("1."+name3+ "  2."+name2+ "  3."+name1)
elif (player1.points == player2.points and player1.points == player3.points):
    print("It's a Draw")
elif (player1.points == player2.points and player1.points > player3.points): 
    print(name1,": WON!!")
    print(name2,": WON!!")
    print("1."+name1+"  1." +name2+ "  2."+name3)
elif (player1.points == player2.points and player3.points > player1.points): 
    print(name3,": WON!!")
    print("1."+name3+"  2." +name1+ "  2."+name2)
elif (player3.points == player2.points and player3.points > player1.points):
    print(name2,": WON!!")
    print(name3,": WON!!")
    print("1."+name3+"  1."+name2+ "  2."+name1)
elif (player3.points == player2.points and player1.points > player3.points):
    print(name1,": WON!!")
    print("1."+name1+"  2."+name3+ "  2."+name2)
elif (player1.points == player3.points and player2.points > player1.points):
    print(name2,": WON!!")
    print("1."+name2+"  2."+name1+ "  2."+name3)
elif (player1.points == player3.points and player1.points > player2.points):
    print(name1,": WON!!")
    print(name3,": WON!!")
    print("1."+name1+"  1."+name3+ "  2."+name2)