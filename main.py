# 10K productive and effective lines of code 
# where every 1000th line of code is better than the last.


import time

def 10kCode_gauge():
# in real time (update every second if possible)
# scrap files from Leo_Soultions folder
# get lines of code that user: leo writes
# count the lines of code
# return a "total number of lines of code" integer
# Display the "total number of lines of code" integer on a gauge
# make a real time desktop widget that displays the gauge
# make the widget transparent


def print_experience_bar(level, xp, next_level_xp):
    # Calculate the percentage of progress towards the next level
    progress = xp / next_level_xp
    
    # Calculate the number of equal signs to display in the bar
    num_equals = int(progress * 10)  # The bar is 10 characters wide

    # Calculate the number of spaces to display in the bar
    num_spaces = 10 - num_equals

    # Construct the bar string
    bar = '[' + '=' * num_equals + ' ' * num_spaces + ']'

    # Print the bar and the level
    print(f"{bar} Level {level}")

# Test the function
level = 1
xp = 0
next_level_xp = 100
while xp <= next_level_xp:
    print_experience_bar(level, xp, next_level_xp)
    xp += 10  # Increase the xp by 10 each iteration for testing
    time.sleep(1)  # Wait for 1 second to make the progress visible


def 10kCode_db():

# store all lines of code in a database
# store the date and time of each line of code
# store the file name of each line of code
# store the line number of each line of code

def 10kCode_graph():
# graph the 10kCode_db() data
# x-axis: time
# y-axis: lines of code
# make the graph real time
# make the graph transparent
# create a cool dashboard that displays the graph like github's contribution graph. 













