# Python dugga part 1:

# Numbers used during this exercise as provided by the "Practice Dugga" instructions

nums = [12, -1, -4, 0, 7, 9, -9, 3]

# a)
# Set a starting "total" value to 0 and then add the numbers greater than 5 to that starting value of 0

total = 0

for number in nums:
    if number > 5:
        total += number

# Print the total sum

print("The total sum of the numbers above 5 is:", total)

# b)

def bucket(n):
    if n <= -5:
        return "LOW"
    elif -5 < n < 5:
        return "MID"
    else:
        return "HIGH"

low = 0
mid = 0
high = 0

for n in nums:
    result = bucket(n)

    if result == "LOW":
        low += 1
    elif result == "MID":
        mid += 1
    else:
        high += 1

print("LOW:", low)
print("MDI:", mid)
print("HIGH:", high)

# c)

# Create an empty list called "odd_high"

odd_high = []

# Go through all of the numbers in nums and check if they are odd and if they belong to the bucket "HIGH"
# If they fulfill the criteria, use append to add them to the list "odd_high"

for n in nums:
    if n % 2 != 0 and bucket(n) == "HIGH":
        odd_high.append(n)

print(odd_high)
