def add_time(start, duration, day = None):
    # Defining Variables
    converted_hours = ""
    num_days = ""
    hour_counter = ""
    am_pm_index = ('PM', 'AM')
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    # Splitting the start time and duration time into hours, minutes and AM/PM
    start_hour = start.split(":")
    start_minutes = start_hour[1].split()
    am_pm = start_minutes[1]
    duration_time = duration.split(":")
    hours_to_add = duration_time[0]
    min_to_add = duration_time[1]

    # Adding start and duration hours and minutes separately
    result_hours = int(start_hour[0]) + int(hours_to_add)
    result_minutes = int(start_minutes[0]) + int(min_to_add)
    
    # Converting Minutes after adding duration minutes to starting minutes
    while result_minutes >= 60: 
        result_minutes -= 60
        result_hours += 1
    
    # AM/PM calculations
    cycle = result_hours // 12
    cycle_switch = abs(am_pm_index.index(am_pm) - (cycle % 2)) 

    # Converting days and hours into 12-hour format
    num_days = (cycle + cycle_switch) // 2
    converted_hours = result_hours % 24

    if converted_hours > 12: 
        converted_hours -= 12
    
    new_time = f"{converted_hours}:{result_minutes:02d} {am_pm_index[cycle_switch]}"
   
    # Day calculations
    if day:
        new_time += f", {days[(days.index(day.capitalize()) + num_days) % 7]}"
        
    if num_days == 1:  
        new_time += " (next day)"
    elif num_days != 0:
        new_time += f" ({num_days} days later)"
   
    return new_time
