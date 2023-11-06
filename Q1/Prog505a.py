import os

def calculate_points(books_read):
    if books_read <= 3:
        return 10 * books_read
    elif books_read <= 6:
        return (10 * 3) + (15 * (books_read - 3))
    else:
        return (10 * 3) + (15 * 3) + (20 * (books_read - 6))

def main():
    total_points = 0
    winner_name = ""
    winner_points = 0

    os.chdir('..')  # <----- this took so long to figure out
    with open("Langdat/prog505a.txt", "r") as file:
        for line in file:
            # Get the first 13 characters of the line, which is the name
            name = line[0:12]

            # The last character is the number of books read
            books_read = int(line[-2])

            # Calculate the points for each reader based on the given rules.
            points = calculate_points(books_read)

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

if __name__ == "__main__":
    main()
