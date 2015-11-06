# Write a function that takes in a string and returns the number of
# letters that appear more than once in the string.
# The string will contain only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.

# Difficulty: hard.

def num_repeats(string):
	common = dict()
	letters = list()
	for letter in string:
	    letters.append(letter)
	for x in letters:
		common[x] = common.get(x,0) + 1
	count = 0
	for key,val in common.items():
	    if val > 1:
	        count += 1


	return count

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print('num_repeats("abdbc") == 1: ' + str(num_repeats('abdbc') == 1))
# one character is repeated
print('num_repeats("aaa") == 1: ' + str(num_repeats('aaa') == 1))
print('num_repeats("abab") == 2: ' + str(num_repeats('abab') == 2))
print('num_repeats("cadac") == 2: ' + str(num_repeats('cadac') == 2))
print('num_repeats("abcde") == 0: ' + str(num_repeats('abcde') == 0))
