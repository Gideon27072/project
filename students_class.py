class students:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@stutern.com'
    
    def fullname(self):
        return '{} {}' .format(self.first, self.last) 

stud_1 = students('Bukola', 'Dare')
stud_2 = students('Temitope', 'Balogun')

print(stud_1.first)
print(stud_2.last)
print(stud_1.email)
print(stud_2.first)

#printing the fullname
#you have to put () after full name because a method and not a variable
print(stud_2.fullname())
 