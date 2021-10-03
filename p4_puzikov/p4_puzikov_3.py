age=float(input('Enter age'))
if age<0:
    print('Error')
elif age<=2:
    age=10.5*age
    print(age) 
else:
    age=21+4*(age-2)
    print('dog age')