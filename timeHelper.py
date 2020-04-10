from datetime import datetime
from datetime import timedelta

# Divides the day into a even number of interations defined by the user and returns when is the next iteration
# and the seconds to it
def get_next_daily_iteration(iterations_per_day):
    # Definitions
    seconds_in_day = 86400

    # Minimum once per day
    if iterations_per_day <= 0:
        iterations_per_day = 1
    # Calculate ellapsed seconds between iterations
    secs_between_runs = seconds_in_day / iterations_per_day
    time_increment = timedelta(seconds=secs_between_runs)

    # Get current day/time and current day
    datetime_now = datetime.now()
    datetime_next_iteration = datetime_now.replace(hour=0, minute=0, second=0, microsecond=0)

    # Find what is the next time milestone from the current time
    # Last milestone is next day at 00:00:00
    for i in range(iterations_per_day):
        datetime_next_iteration += time_increment
        if datetime_next_iteration > datetime_now:
            break

    # Get time for a delay
    delay_to_next_iteration = (datetime_next_iteration - datetime.now()).total_seconds()
    return [datetime_next_iteration, delay_to_next_iteration]


def debug_print_daily_iterations(iterations_per_day):
    # Definitions
    seconds_in_day = 86400

    # Minimum once per day
    if iterations_per_day <= 0:
        iterations_per_day = 1
    # Calculate ellapsed seconds between iterations
    secs_between_runs = seconds_in_day / iterations_per_day
    time_increment = timedelta(seconds=secs_between_runs)

    # Get current day/time and current day
    datetime_now = datetime.now()
    datetime_next_iteration = datetime_now.replace(hour=0, minute=0, second=0, microsecond=0)

    # Find what is the next time milestone from the current time
    # Last milestone is next day at 00:00:00
    for i in range(iterations_per_day):
        datetime_next_iteration += time_increment
        print(datetime_next_iteration)
