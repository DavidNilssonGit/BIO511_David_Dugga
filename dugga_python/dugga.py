# Question 1.
print("Question 1.")
# a) Save your own name as a str(string) to a variable called 'my_name'

my_name = str("David Nilsson")
print("a) My name is: ", my_name)

# b) Calculate and print the length of your name.

name_length = len(my_name)
print("b) The length of my name is: ", name_length)

# c) Choose a letter that occurs in your name at least once and print the number of times that letter occurs

letter = "d"
letter_count = my_name.lower().count(letter.lower())

print("c) The letter", letter ,"occurs", letter_count, "times in my name.")

# Create an empty space between the questions for better readability
print()

# Question 2.
print("Question 2.")
# Use the following list for this question: [1, 5, "4", "six", 3.14]

my_list = [1, 5, "4", "six", 3.14]

# a) For each item in 'my_list', try to convert it to an int(integer) and add it to a new list called 'new_list' using the append() function
# If it can't be converted to due to an exception, try to instead print a message stating such

# Create a new empty list called 'new_list'
new_list = []

for item in my_list:
    try:
        new_list.append(int(item))
    except ValueError:
        print(f"a) The item '{item}' couldn't be converted to an integer.")

# b) Put the conversion loop in a function called 'clean_list()'
# You should be able to call the function with 'my_list' as an input argument and save the result as 'new_list'

def clean_list(input_list):
    new_list = []
    for item in input_list:
        try:
            new_list.append(int(item))
        except ValueError:
            print(f"b) The item '{item}' couldn't be converted to an integer.")
    return new_list

new_list = clean_list(my_list)
print(f"The cleaned list is: {new_list}")

# c) Take the 'new_list' from part b and calculate the sum of the neighbors in the list
# If the list for example is as follows: [2, 4, 6, 3], the list should return [6, 10, 9]

# Create a new empty list called 'sum_of_neighbors'
sum_of_neighbors = []

# Go through each of the numbers in 'new_list' and add the value of the number[i] to the value of its neighbor[i + 1]
# Use append to add the sum of the neighbors to the empty list 'sum_of_neighbors'
for i in range(len(new_list) - 1):
    sum_of_neighbors.append(new_list[i] + new_list[i + 1])

print(f"c) The sum of neighbors in 'new_list' is: {sum_of_neighbors}")

# Create an empty space between the questions for better readability
print()

# Question 3.
print("Question 3.")

# a) Load the cnv_data.csv file and generate a scatter plot with 'position_mb' on the x-axis and 'log2_ratio' on the y-axis

# Import the required libraries: pandas and matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt

# Load the cnv_data.csv file into a pandas DataFrame called 'df'
df = pd.read_csv("cnv_data.csv")

# Generate a scatter plot with 'position_mb' on the x-axis and 'log2_ratio' on the y-axis
plt.scatter(df
            ['position_mb'],
            df['log2_ratio'],
            label="CNV Data Scatter Plot"
            )

plt.xlabel("Position (Mb)") # Adds the label 'Position (Mb)' to the x-axis
plt.ylabel("Log2 Ratio") # Adds the label 'Log2 Ratio' to the y-axis
plt.title("CNV Data Scatter Plot") # Adds the title 'CNV Data Scatter Plot' to the scatter plot
plt.tight_layout() # Adjust the spacing around the scatter plot

# b) Save the scatter plot as a .png file

plt.savefig("cnv_data_scatter_plot.png")

# Print message stating that the .png file was saved
print("b) Scatter plot was saved as 'cnv_data_scatter_plot.png'")

# c) To further improve the script, make it so that the user can define the name of the input and output files

input_file = input("CSV file name: "
                   ).strip() or "cnv_data.csv" # Requests the user to name input file, uses 'cnv_data.csv' as default
output_file = input("Output PNG file name: "
                     ).strip() or "cnv_data_scatter_plot.png"

plt.savefig(output_file)

# Print message stating that the .png file was saved as 'output_file'
print(f"c) Scatterplot was saved as '{output_file}.png'")

# Create an empty space between the questions for better readability
print()

# Question 4.
print("Question 4.") # Simply did not have enough time to do this question - wrote some text for what I would've done if I had the time

# a) Write a script that can simulate 20 games played
# For each game, record a dict if Alice won, if Bob won, or if it was a draw
# Print the dictionary after the 20 games are played to see how the games went

import random
random.randint (1, 6) # Will generate an int from 1 to 6

# Create a function where a game is simulated using the 'random.randint (1, 6)' for both Alice and Bob
# Perform this task 20 times for the 20 simulated games

# Create the starting values for each outcome

Alice = 0
Bob = 0
Draw = 0

# Then compare the values of the their respective dice throws for each to determine if the game ended in a win for Alice, for Bob, or in a draw
# If Alice won, add a += 1 to her total
# Elif Bob won, add a += 1 to his total
# Else add a += 1 to the total draw count

# Return the final result and print it