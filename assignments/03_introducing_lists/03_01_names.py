'''
Let's do lists
'''
names = ['Brooklyn', 'Widel', 'Ciera', 'Brian']


for name in names:
    print(name)
print ('End. This is not in the for loop')


# doing chapter 3 and assignment 5
names = ['Brooklyn', 'Widel', 'Ciera', 'Brian']
person_not_coming = names.pop()

print (person_not_coming + ' is not coming to the party.')

# Chapter Assignment 6
person_added_late = "Desai"
names.append(person_added_late)
print (names)
print (person_added_late + ' is coming to the party.')