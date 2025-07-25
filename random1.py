import random
secretno=random.randint(1,50)
# print(secretno) 
count=1
while True:
    guess=int(input('guess the no(1-50)...>>>'))
    if guess==secretno:
        print('yahh u guess right no')
        break
    else:
        if guess<secretno:
            print(" ur no. is lesser than secreate no.")
        elif guess>secretno:
            print(" ur no. is greater than secreate no.")
        print('try again ... u enter wrong no')
    count+=1
print(f'you take {count} chance')
