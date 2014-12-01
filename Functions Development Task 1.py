def input_times():
    hours = int(input("Please input how many hours rounded down to the nearest hour: "))
    minutes = int(input("Please input how many minutes rounded down to the nearest minute: "))
    seconds = int(input("Please input how many seconds ronded down to the nearest second: "))
    return hours, minutes, seconds

def convert_to_seconds(hours, minutes, seconds):
    seconds_from_hours = (hours * 60) * 60
    seconds_from_minutes = minutes * 60
    total_seconds = (seconds_from_hours + seconds_from_minutes + seconds)
    return total_seconds

def output_seconds(total_seconds):
    print("Your time is equal to {0} seconds.".format(total_seconds))

hours, minutes, seconds = input_times()
total_seconds = convert_to_seconds(hours, minutes, seconds)
output_seconds(total_seconds)
