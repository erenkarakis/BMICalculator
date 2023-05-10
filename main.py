from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(350,350)

def calculate_bmi():
    weight = entry_weight.get()
    height = entry_height.get()
    global label_response

    if weight.isdigit() and height.isdigit():
        bmi = (int(weight) / ((int(height)/100)**2))
        if bmi < 18.5:
            label_response.config(text=f"Your BMI is {bmi}. You are under weight.")
        elif bmi >= 18.5 and bmi < 25:
            label_response.config(text=f"Your BMI is {bmi}. You are normal.")
        elif bmi >= 25 and bmi < 30:
            label_response.config(text=f"Your BMI is {bmi}. You are over weight.")
        elif bmi >= 30 and bmi < 35:
            label_response.config(text=f"Your BMI is {bmi}. You are obesity. (class I)")
        elif bmi >= 35 and bmi < 40:
            label_response.config(text=f"Your BMI is {bmi}. You are obesity. (class II)")
        elif bmi >= 40:
            label_response.config(text=f"Your BMI is {bmi}. You are extreme obesity.")

    elif not weight.isdigit():
        label_response.config(text="Please enter a valid weight")
    elif not height.isdigit():
        label_response.config(text="Please enter a valid height")

label1 = Label(text="Enter your weight (kg)", font=("Comic Sans MS", 8, "bold"))
label1.pack()
entry_weight = Entry(width=10)
entry_weight.config()
entry_weight.pack()

label2 = Label(text="Enter your height (cm)", font=("Comic Sans MS", 8, "bold"))
label2.pack()
entry_height = Entry(width=10, )
entry_height.pack()

label_response = Label(text="", font=("Comic Sans MS", 16, "bold"))

btn_calculate = Button(text="Calculate", command=calculate_bmi)
btn_calculate.pack()
label_response.pack()

window.mainloop()