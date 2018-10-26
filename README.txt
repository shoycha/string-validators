October 26
HackerRank
Ex. String Validators
Task

You are given a string . 
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Initially I wrote for each char in string if it is alphanumeric then set initially declared boolean variable to true. Same thing for other evaluations.
After loop is finished print those boolean variables.

Then I went to discussions section and learned pre-built function any()
The any() method returns True if any element of an iterable is True. If not, any() returns False.

any(iterable)