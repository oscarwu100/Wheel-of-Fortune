################################################################################
# Author: BO-YANG WU
# Date: 04/23/2020
# This program is a variation of the game Wheel of Fortune game for a single player.
################################################################################
import random as ran


f= open('phrases.txt')
f1= f.read()
f.close()

data= f1.split('\n')


consonant= 'BCDFGHJKLMNPQRSTVWXYZ'# consonant
vowel= 'AEIOU'# vowel

rounds= 1
phrases_num= ran.randrange(0, len(data))
phrases= data[phrases_num]# ramdomly choosse the answer
data.pop(phrases_num)# move this anser out off the list
phrases_s= phrases.split()
phrases_slist= list(phrases.upper())
words_long= [len(phrases_s[i]) for i in range(len(phrases_s))]# count each word long
space= (53- len(phrases)- 4)/ 2# count the space
if space% 1 != 0:# if it is not integer
    space1= int(space)# space infront
    space2= int(space)+1# space behind
else:
    space1= int(space)
    space2= int(space)
words_space= ''
alphabat= consonant+ vowel
for l in phrases_slist:
    if l in alphabat:
        words_space+= '_'
    else:
        words_space+= l
words_space_list= list(words_space)

consonant_list= list(consonant)

vowel_list= list(vowel)
money= 0

spin_space= [500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650,
             700, 700, 700, 800, 900, 2500, 0, 0]

number= 0
consonant_used= []
vowel_used= []
totalmoney= 0
while number!= 4:
    money_show= ' '* (10- len(str(money)))+ '$'+ str(money)+ '::'
    consonant= ''.join(map(str, consonant_list))
    vowel= ''.join(map(str, vowel_list))
    print(':::::::::::::::::::::::::::::::::::::::::: ROUND', rounds, 'of 4 ::')
    print('::', ' '* space1, words_space,' '* space2, ' ::')
    print(':'* 58)
    print('::', ' ',consonant , '  ::  ',vowel , '  ::', money_show)
    print(':'* 58)
    
    number= 0
    while number== 0:#ask question
        print('What would you like to do?\n  1 - Spin the wheel\n  2 - Buy a vowel\n  3 - Solve the puzzle\n  4 - Quit the game')
        number= input('Enter the number of your choice: ')
        if (number== '1') or (number== '2') or (number== '3') or (number== '4'):
            number= int(number)
        else:
            print(number, 'is an invalid choice.')
            number= 0
    if number== 1:
        r= ran.randrange(0, 21)
        if len(consonant_used)== 21:
            print('There are no more consonants to choose.')
        elif spin_space[r] != 0:
            print('The wheel landed on '+ str(spin_space[r])+ '.')
    
            while 1:
                wheel_pick= input('Pick a consonant: ')
                if wheel_pick.upper() in consonant_used:
                    print('The letter', wheel_pick.upper(), 'has already been used.')
                elif wheel_pick.upper() in vowel_list:
                    print('Vowels must be purchased.')
                elif wheel_pick.upper() in consonant_list:
                    consonant_used.append(wheel_pick.upper())
                    for i in range(21):
                        if wheel_pick.upper()== consonant_list[i]:
                            consonant_list[i]= ' '
                    if wheel_pick.upper() in phrases_slist:
                        count= 0
                        wheel_pick_num= []
                        for i in range(len(phrases_slist)):
                            if wheel_pick.upper()== phrases_slist[i]:
                                count+= 1
                                wheel_pick_num.append(i)
                        print('There is '+ str(count)+ ' '+ str(wheel_pick.upper())+ ' , which earns you $'+ str(format(spin_space[r]* count, ',d'))+ '.')
                        money+= spin_space[r]* count
                        for j in wheel_pick_num:
                            words_space_list[j]= wheel_pick.upper()
                        words_space= ''.join(map(str, words_space_list))
                        break
                    else:
                        print('I\'m sorry, there are no '+ str(wheel_pick.upper())+ '\'s.')
                        break
                elif len(wheel_pick)> 1:
                    print('Please enter exactly one character.')
                else:
                    print('The character', wheel_pick, 'is not a letter.')
                    
        else:
            print('The wheel landed on BANKRUPT.')
            print('You lost $'+ str(format(money, ',d'))+ '!')
            money= 0
    elif number== 4:
        if rounds== 1:
            money= 0
        print('You earned $'+ format(money, ',d')+ ' this round.')
        print('Thanks for playing!')
        totalmoney+= money
        print('You earned a total of $'+ format(totalmoney, ',d'))
        break
        
    elif number== 2:
        if money< 250:
            print('You need at least $250 to buy a vowel.')
        elif len(vowel_used)== 5:
            print('There are no more vowels to buy.')
        else:
            while 1:
                    wheel_pick= input('Pick a vowel: ')
                    if wheel_pick.upper() in vowel_used:
                        print('The letter', wheel_pick.upper(), 'has already been used.')
                    elif wheel_pick.upper() in consonant_list:
                        print('Consonants cannot be purchased.')
                    elif wheel_pick.upper() in vowel_list:
                        vowel_used.append(wheel_pick.upper())
                        for i in range(5):
                            if wheel_pick.upper()== vowel_list[i]:
                                vowel_list[i]= ' '
                        if wheel_pick.upper() in phrases_slist:
                            count= 0
                            wheel_pick_num= []
                            for i in range(len(phrases_slist)):
                                if wheel_pick.upper()== phrases_slist[i]:
                                    count+= 1
                                    wheel_pick_num.append(i)
                            print('There is '+ str(count)+ ' '+ str(wheel_pick.upper())+ '\'s.')
                            money-= 250
                            for j in wheel_pick_num:
                                words_space_list[j]= wheel_pick.upper()
                            words_space= ''.join(map(str, words_space_list))
                            break
                        else:
                            print('I\'m sorry, there are no '+ str(wheel_pick.upper())+ '\'s.')
                            break
                    elif len(wheel_pick)> 1:
                        print('Please enter exactly one character.')
                    else:
                        print('The character', wheel_pick, 'is not a letter.')
    
    
    elif number== 3:
        print('Enter your solution.')
        print('  Clues: ', words_space)
        guess= input('  Guess:  ')
        if guess.upper()== phrases.upper():
            print('Ladies and gentlemen, we have a winner!')
            print('You earned $'+ format(money, ',d')+ ' this round.')
            totalmoney+= money
        else:
            print('I\'m sorry. The correct solution was:')
            print(phrases.upper())
            print('You earned $0 this round.')
            money= 0
            totalmoney+= money
        if rounds== 4:# round 4, the game should end
            number= 4
            print('Thanks for playing!')
            totalmoney+= money
            print('You earned a total of $'+ format(totalmoney, ',d'))
        # clear everything to original
        rounds+= 1
        money= 0
        consonant= 'BCDFGHJKLMNPQRSTVWXYZ'
        consonant_list= list(consonant)
        vowel= 'AEIOU'
        vowel_list= list(vowel)
        phrases_num= ran.randrange(0, len(data))
        phrases= data[phrases_num]
        data.pop(phrases_num)
        phrases_s= phrases.split()
        phrases_slist= list(phrases.upper())
        words_long= [len(phrases_s[i]) for i in range(len(phrases_s))]
        space= (53- len(phrases)- 4)/ 2
        if space% 1 != 0:
            space1= int(space)
            space2= int(space)+1
        else:
            space1= int(space)
            space2= int(space)
        words_space= ''
        for l in phrases_slist:
            if l in alphabat:
                words_space+= '_'
            else:
                words_space+= l
        words_space_list= list(words_space)
        consonant_used= []
        vowel_used= []
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
