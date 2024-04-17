# need to find widest axis

def calculate_reservoir_capacity(construction_plan):
    area = 0
    x = 0
    y = 0

    for direction in construction_plan:
        direction, distance = direction.split()
        distance = int(distance)

        if direction == "R":
            x += distance
            max_x = max(0, x)
        if direction == 'L':
            x -= distance
            max_x = min(0, x)
        if direction == "U":
            y += distance
            max_y = max(0, y)
        if direction == "D":
            y -= distance
            max_y -= min(0, y)

        area += distance

        return area

construction_plan = ["R 6", "D 5", "L 2", "U 3"]