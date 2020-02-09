print('Start')
print('Is it raining?')
a=str(input())
if a=='Yes' or a=='yes':
    print('Do you have an umbrella or smtg to protect you?')
    b=str(input())
    if b=='Yes' or b=='yes':
        print('You can go out')
    else:
        print('Wait till it stops raining')
else:
    print('You can go outside')
