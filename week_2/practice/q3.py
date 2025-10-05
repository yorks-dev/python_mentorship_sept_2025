# Conditionals

student_age = 15
student_hostel = "Ganga"
student_marks = 70

# student is eligible for internship if his age is >= 18 but less than 30 and he should be from
#  ganga hostel and his marks should be greater than equal 80 but also less than 90 (A)

if student_age >= 18 and student_age < 30:
    if student_hostel == "Ganga":
        if student_marks >= 80 and student_marks < 90:
            print("Eligible")
        else:
            print("Not eligible : marks criteria not met")
    else:
        print("Not eligible: student_hostel requirement not ok")
else:
    print("Not eligible : age criteria not met")
