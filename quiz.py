print("Hello! Welcome")
name=input("what is your sweet name?:")
ans=input("Are you ready to play(yes/no)?:")
score=0
if ans.lower()=='yes':
    ans=input('1.What is 4+5 equals to?')
    if ans=='9':
            score+=1
            print('correct!')
            print('you must be genius!', name)
            print('your score is: ', score )
    else:
            print('incorrect!')
            print('try again next time! your score is: ', score )
            print('have a good day!')
    ans = input('1.What is 5+5 equals to?')
    if ans == '10':
        score += 1
        print('correct!')
        print('you must be genius!', name)
        print('your score is: ', score )
    else:
        print('incorrect!')
        print('try again next time! your score is: ', score )
        print('have a good day!')











else:
    print('Bye!, see you soon', name )
mainloop()