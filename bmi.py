#getting height from the users in meters
height = float(input('input your height in meters:'))

#getting weight from the users in kg

weight = float(input('input your weight in kg:'))

#calculating and printing BMI

print('your body mass index is:', round(weight/(height * height),2))