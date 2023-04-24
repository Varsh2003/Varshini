from my import Mcq
print("welcome to the general knowledge questions!!")
print("you are win or lose!!")

ques=["1. who is the father for our nation?\na) soniya gandhi b) Mahtma gandhi c) Nehru",
      "2. who is the bother of Nation?\na) Rajnath Singh b) Assam c) Mizoram",
      "3. who is family of nation\n a) The northen american status b) The western European status c) The eastern countires",
      "4. our national bird is?\n a) peacock b) parrot c) crow"]

test=[Mcq(ques[0],"b"),Mcq(ques[1],"a"),Mcq(ques[2],"b"),Mcq(ques[3],"a")]
def run_test():
    score=0
    for quest in test:
        print(quest.question)
        answer=input("Enter your answer:")
        if answer == quest.answer:
           score+=1
    print(f"your score is {score} / {len(test)}") 
    if score==len(test):
        print("you are win!!")
    else:
        print("your are lose!!")

run_test()    