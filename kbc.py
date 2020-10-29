from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if question["answer"]==answer:
    	return True
    else:
    	return False	

   

def lifeLine(ques,i):
	print('\tQuestion {}:{}'.format(i+1,ques["name"] ))
	answer=ques["answer"]
	valuelist=list(ques.values())
	print("\t\t\tOption {}".format(answer)+": "+valuelist[answer])
	del valuelist[answer] 
	print("\t\t\tOption {}: {}".format(answer+1 if answer<4 else 1,valuelist[1]))      



def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print('Welcome To The Game\n')
    flag=1
    for i in range(0,15):
    	print('\tQuestion {}:{}'.format(i+1,QUESTIONS[i]["name"] ))
    	print(f'\t\tOptions:')
    	print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
    	print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
    	print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
    	print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
    	
    	# check for the input validations
    	if flag==1 and i!=14:
    		LifelineCheck=input('\n Do you want to use lifeline?(yes/no)')
    		if LifelineCheck.lower()=='yes':
    			lifeLine(QUESTIONS[i],i)
    			flag=flag-1

    		
    			
    	ans = input('Your choice ( 1-4 ) : ')

    	if isAnswerCorrect(QUESTIONS[i], int(ans) ):
        	# print the total money won.
        	# See if the user has crossed a level, print that if yes
        	print('\nCorrect !')
        	if i==4:
        		print('\nCongratulations,you crossed level 1')
        	elif i==9:
        		print('\nCongratulations,you crossed level 2')
        			
        	global reward
        	reward=QUESTIONS[i]["money"]
        	print('\n You Won {}'.format(reward))
        	print('\nDo you want to quit?')
        	quitcheck=input()
        	if quitcheck.lower()=='quit':
        		print('\nYou have quit the game')
        		print('\n You Won {}'.format(reward))
        		quit()



    	else:
        	# end the game now.
        	# also print the correct answer
        	print('\nIncorrect !')
        	print('\nThe correct answer is option {}'.format(QUESTIONS[i]["answer"]))
        	print('\nThe Game Ended!')
        	if i>=9:
        		print('\nYou Won {}'.format(reward))
        	elif i>=4:
        		print('\n You Won 10000')
        	else:
        		print('\n You Won 0')
        	quit()	

    	# print the total money won in the end.


kbc()
