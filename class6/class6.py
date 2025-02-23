from typing import Union

per : Union[int, float] = float(input("Enter your percentage : \t"))
grade : Union[str, None] = None

if per >= 0 and per < 33:
    grade = "Fail"
elif per >= 33 and per < 40:
    grade = "E"
elif per >= 40  and per < 50:
    grade = "D"
elif per >= 50 and per < 60:
    grade = "C"
elif per >= 60 and per < 70:
    grade = "B"
elif per >= 70 and per < 80:
    grade = "A"
else:
    grade = "A+"

print (f"Dear Student Your percentage is (per)  now your calculated grade is : \t {grade}")


PerType = Union[int, float]