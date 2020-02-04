#enter details of the person
print("enter your name:")
typedName=input()
print('enter your weight(in kgs):')
wgts=float(input())
print('enter your height(in meters):')
hgt=float(input())

#formula to calculate BMI
bmi= (wgts / (hgt**2))

#bmi results based on bmi
if bmi < 18.5:
    print('Your BMI is',bmi,'. This is considered Under-nutritioned.')
if bmi > 18.5 and bmi < 24.9:
    print('Your BMI is',bmi,'. This is considered Healthy.')
if bmi > 25:
    print('Your BMI is',bmi,'. This is considered Obese.')