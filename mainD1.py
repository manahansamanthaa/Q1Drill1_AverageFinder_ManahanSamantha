from pyscript import display


title= "Average Finder"
description= "Input your grades to determine your average!"

display(title, target="webtitle")
display(description, target="desc1")



from pyscript import document, display


def average_finder(e):
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)


Average= (num1 + num2) / 2
message = "Passed" #displays if status is passed


status = "Passed" if Average >= 75 else "Failed"
print(status)
display(f"Average:{Average:2f} - {message}", target="output")


