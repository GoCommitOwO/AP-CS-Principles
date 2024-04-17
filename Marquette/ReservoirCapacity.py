def calculate_reservoir_capacity(construction_plan):
    # Initialize variables
    max_x = 0
    max_y = 0
    grid = set()
    x = 0
    y = 0
    
    # Iterate through each command in the construction plan
    for command in construction_plan:
        direction, distance = command.split()
        distance = int(distance)
        
        # Update position based on the command
        if direction == 'R':
            x += distance
            max_x = max(max_x, x)
        elif direction == 'L':
            x -= distance
            max_x = min(0, x)
        elif direction == 'U':
            y += distance
            max_y = max(max_y, y)
        elif direction == 'D':
            y -= distance
            max_y = min(0, y)
        
        # Mark the squares dug out by the command
        for i in range(x, x + distance + 1):
            for j in range(y, y + distance + 1):
                grid.add((i, j))
    
    # Calculate the total area covered
    area = len(grid)
    
    return area

# Test the function
construction_plan = ["R 6", "D 5", "L 2", "U 3 "]
reservoir_capacity = calculate_reservoir_capacity(construction_plan)
print("Reservoir capacity:", reservoir_capacity, "square meters")
