word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page

# We can use print to understand what is wrong with the code by printing the value of word_per_page. We can see that it is 0, which is not correct. The issue is that we are using the comparison operator (==) instead of the assignment operator (=) when trying to assign the value to word_per_page. To fix this, we need to change the line to use the assignment operator.
print(word_per_page)  # This will show that word_per_page is 0, which is incorrect.
print(pages)  # This will show the number of pages input by the user, which is correct.

print(total_words)

# So we need to change the line to:
# word_per_page = int(input("Number of words per page: ")) 
