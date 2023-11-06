# Initialize variables to keep track of total points and the contest winner.
import os

total_points = 0
winner_name = ""
winner_points = 0


os.chdir('..') #<----- this took so long to figure out
with open("Langdat/prog505a.txt", "r") as file:
    for line in file:
        #get the first 13 characters of the line, which is the name
        name = line[0:12]

       #the last character is the number of books read
        books_read = line[-2]
        # Convert the number of books read to an integer.
        books_read = int(books_read)

        # Calculate the points for each reader based on the given rules.
        if books_read <= 3:
            points = 10 * books_read
        elif books_read <= 6:
            points = (10 * 3) + (15 * (books_read - 3))
        else:
            points = (10 * 3) + (15 * 3) + (20 * (books_read - 6))

        # Update the total points.
        total_points += points

        # Check if this reader has the highest points so far.
        if points > winner_points:
            winner_name = name
            winner_points = points

        # Print the reader's information.
        print(f"{name}{books_read}{points}")

# Calculate the average points per reader.
average_points = total_points / 5

# Print the average points and the contest winner.
print(f"Average points per reader = {int(average_points)}")
print(f"The winner of the contest is {winner_name}")
