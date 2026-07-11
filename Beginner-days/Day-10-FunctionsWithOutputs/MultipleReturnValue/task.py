def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("HeBER", "maTtA"))

def under_age(age):
    if age >= 18:
        return False
    else:
        return True

if under_age(19):
    print("YES IS UNDER AGE")
else:
    print("NO IS UNDER AGE")


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(f"2000 is a leap year? {is_leap_year(2000)}")
print(f"2000 is a leap year? {is_leap_year(2020)}")
print(f"2000 is a leap year? {is_leap_year(2024)}")
print(f"2000 is a leap year? {is_leap_year(2400)}")
