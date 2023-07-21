#'logical and': returns true if all the expressions connected by 'and' are true

# Example
x = 2

print(x < 10 and x != 3)





# Example 2:
# check voter eligibility

age = 26
is_human = False

is_eligible = age >= 18 and is_human

if is_eligible:
    print("You are eligible")
else:
    print("Sorry you are not eligible")