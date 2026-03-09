from pywebio.input import input, FLOAT
from pywebio.output import put_text

# simpe BMI calculation
def bmi():
    height = input("enter your height(cm): ", type=FLOAT)
    weight = input("enter your height(kg): ", type=FLOAT)

    BMI = weight / (height / 100) **2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    
    for top, status in top_status:
        if BMI <= top:
            put_text('your BMI: %.Lf. category: %s' % (BMI, status))
            break

if __name__ == '__main__':
    bmi()