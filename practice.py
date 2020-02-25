##print('enter a word')
##w=input()
##q=0
##for n in w:
##    q=q+1
##    print(n,q)

##d={1:"-",2:"-",3:"-",4:"-",5:"-",6:"-",7:"-",8:"-",9:"-"}
##while True:
##    for n in range(1,10,1):
##        print("\t",n,':',d[n], end='')
##        if n==3 or n==6 or n==9:
##            print()
##    print('Player 1 where you want to put X')
##    choice1=int(input())
##    d[choice1]='x'
##    for n in range(1,10,1):
##        print("\t",n,':',d[n], end='')
##        if n==3 or n==6 or n==9:
##            print()
##    if d[1]==d[2]==d[3]=='x' or d[4]==d[5]==d[6]=='x' or d[7]==d[8]==d[9]=='x' or d[1]==d[4]==d[7]=='x' or d[2]==d[5]==d[8]=='x' or d[3]==d[6]==d[9]=='x' or d[1]==d[5]==d[9]=='x' or d[7]==d[5]==d[3]=='x':
##        print('Player 1 wins')
##        break
##    print('Player 2 pick a number where you want to put O')
##    choice2=int(input())
##    d[choice2]='O'
##    for n in range(1,10,1):
##        print("\t",n,':',d[n], end='')
##        if n==3 or n==6 or n==9:
##            print()
##    if d[1]==d[2]==d[3]=='O' or d[4]==d[5]==d[6]=='O' or d[7]==d[8]==d[9]=='O' or d[1]==d[4]==d[7]=='O' or d[2]==d[5]==d[8]=='O' or d[3]==d[6]==d[9]=='O' or d[1]==d[5]==d[9]=='O' or d[7]==d[5]==d[3]=='O':
##        print('Player 2 wins')
##        break
##    if d[1]==d[2]==d[3]=='x' or d[4]==d[5]==d[6]=='x' or d[7]==d[8]==d[9]=='x' or d[1]==d[4]==d[7]=='x' or d[2]==d[5]==d[8]=='x' or d[3]==d[6]==d[9]=='x'or d[1]==d[5]==d[9]=='x' or d[7]==d[5]==d[3]=='x':
##        print('Player 1 wins')
##    if d[1]==d[2]==d[3]=='O' or d[4]==d[5]==d[6]=='O' or d[7]==d[8]==d[9]=='O' or d[1]==d[4]==d[7]=='O' or d[2]==d[5]==d[8]=='O' or d[3]==d[6]==d[9]=='O'or d[1]==d[5]==d[9]=='O' or d[7]==d[5]==d[3]=='O':
##        print('Player 2 wins')
##    if '-' not in d.values():
##        print('game is a draw')
##        break



        
##import random
##a=[]
##words=['apple','elephant','buffalo','dog','cat']
##word=random.choice(words)
##print(word)
##l=list(word)
##for n in l:
##    a.append('-')
##print(a)
##while '-' in a:
##    print('what is your guess')
##    answer=input()
##    if answer in word:
##        print('Your guess is right')
##        index=l.index(answer)
##        a[index]=answer
##        l[index]='0'
##        print(a)
##    else:
##        print('your guess is wrong')
##

##d={1:'_',2:'_',3:'_',4:'_',5:'_',6:'_',7:'_',8:'_',9:'_'}
##while True:
##    for n in range(1,10,1):
##        print(n,':',d[n] ,end='')
##        if n==3 or n==6 or n==9:
##            print()
##            
##    print('player 1 enter the number where you want to put X')
##    choice1=int(input())
##    d[choice1]='X'
##     
##    for n in range(1,10,1):
##        print(n,':',d[n] ,end='')
##        if n==3 or n==6 or n==9:
##            print()
##        if d[1]==d[2]==d[3]=='X' or d[4]==d[5]==d[6]=='X' or d[7]==d[8]==d[9]=='X' or d[1]==d[4]==d[7]=='X' or d[2]==d[5]==d[8]=='X' or d[3]==d[6]==d[9]=='X'or d[1]==d[5]==d[9]=='X' or d[7]==d[5]==d[3]=='X':
##            print('player 1 wins')
##            break
##            
##    print('Player 2 enter the number where you want to put O')
##    choice2=int(input())
##    d[choice2]='O'
##    for n in range(1,10,1):
##        print(n,':',d[n] ,end='')
##        if n==3 or n==6 or n==9:
##            print()
##        if d[1]==d[2]==d[3]=='O' or d[4]==d[5]==d[6]=='O' or d[7]==d[8]==d[9]=='O' or d[1]==d[4]==d[7]=='O' or d[2]==d[5]==d[8]=='O' or d[3]==d[6]==d[9]=='O' or d[1]==d[5]==d[9]=='O' or d[7]==d[5]==d[3]=='O':
##        
##            print('player 2 wins')
##            break
##        
##    if d[1]==d[2]==d[3]=='X' or d[4]==d[5]==d[6]=='X' or d[7]==d[8]==d[9]=='X' or d[1]==d[4]==d[7]=='X' or d[2]==d[5]==d[8]=='X' or d[3]==d[6]==d[9]=='X' or d[1]==d[5]==d[9]=='X' or d[7]==d[5]==d[3]=='X':
##        print('player 1 wins')
##    if d[1]==d[2]==d[3]=='O' or d[4]==d[5]==d[6]=='O' or d[7]==d[8]==d[9]=='O' or d[1]==d[4]==d[7]=='O' or d[2]==d[5]==d[8]=='O' or d[3]==d[6]==d[9]=='O' or d[1]==d[5]==d[9]=='O' or d[7]==d[5]==d[3]=='O':
##        print('player 2 wins') 
##    if '_' not in d.values():
##        print('game is a draw')
##        break

##password='Apple'
##while True:
##    print('enter password')
##    a = input()
##    if a != password:
##        print("access denied")
##    else:
##        print('access granted')
##        break
##
##
##password='Apple'
##print('enter the password')
##p=input()
##
##while p!=password:
##    print('enter password')
##    p = input()
##    if p != password:
##        print("access denied")
##    else:
##        print('access granted')
##    break
##


things=open("NameList.txt","r")
for g in things:
    print(g)

things.close()


























        
