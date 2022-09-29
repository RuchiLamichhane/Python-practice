from unittest.util import three_way_cmp


stg=('Simplilearn')
print(stg)

stg=("Simplilearn's Course")
print(stg)

stg='Tim said,"I am busy today".'
print(stg)

stg= 'Tim said,"I\'m busy today".'
print(stg)

stg=''' hey there
welcome to simplilearn '''
print(stg)


stg="StudyHard"
print(len(stg))
print(stg[4])


stg1="Simplilearn"
for i in stg1:
  print(i)

'''stg2="Simplilearn"
for i in stg1:
  print(i,end="")'''


#Slicing

stg="Simplilearn"
print(stg[0:5])
print(stg[:5])
print(stg[5:])
print(stg[2:5])
'''end index is excluded but starting index is included'''

stg="Welcome to Simplilearn"

print(stg.upper())
print(stg.lower())

print(stg.find('l'))
print(stg.index('l'))

print(stg.split(" "))

x=stg.split(" ")
print (x)

print(stg.replace('Simplilearn', 'python tutorial'))

print(stg.rpartition(" to "))


'''string concatenation'''

stgl1="good"
stgl2="morning"
'''stgl= stgl1 + stgl2
print(stgl)'''
print(stgl1 + stgl2)

stg1='Hey'
stg2='there'
stg3='all'
stg="{} {},{}!".format(stg1,stg2,stg3)
print(stg)
