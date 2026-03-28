year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# This is very simple problem, the sintax error is that the statement "elif" is ignoring the year 1994, so when
# we input 1994, it doesn't print anything. To fix this, we can change the statement "elif" to "else", so it will
# print "You are a Gen Z." for any year greater than 1994, including 1994 itself.
# Or we can change the statement "elif" to "elif year >= 1994:", so it will include the year 1994 in the condition.