#Assigning a string to a type float
v = float(input('Enter wind speed: '))
#comparison v in different ranges 
if 0<=v<137:                           
    print('Minor')                      
elif 137<=v<177:
    print('Modarate')
elif 177<=v<217:
    print('Conciderable')
elif 177<=v<266:
    print('Severe')
elif 266<=v<322:
    print('Devastating')
elif v>=322:
    print('incredible')
elif v<0:
    print('Error')
