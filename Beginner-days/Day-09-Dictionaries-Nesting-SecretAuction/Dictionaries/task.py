#Testing
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
print(programming_dictionary)

print(programming_dictionary["Bug"])

programming_dictionary = {}

programming_dictionary["bug"] = "An error in a program that prevents the program from running as expected."

print(programming_dictionary)

programming_dictionary["bug"] = "Hello"
print(programming_dictionary["bug"])

programming_dictionary["function"] = "bye"

for key in programming_dictionary:
    print(key)

for key in programming_dictionary:
    print(programming_dictionary[key])
