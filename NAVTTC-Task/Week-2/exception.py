def calculate_average_speed(distance_str, time_str):
    try:
        dist = float(distance_str)
        time = float(time_str)
        return dist / time
    except ValueError:
        return "Error: Please enter valid numeric inputs."
    except ZeroDivisionError:
        return "Error: Time cannot be zero."