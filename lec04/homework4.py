
def next_birthday(date, birthdays):
    """
    Finds the next birthday after the given date.
    """
    month = date[0]
    day = date[1]
    
    sorted_keys = sorted(birthdays.keys())
    
    i = 0
   
    while i < len(sorted_keys) and (sorted_keys[i][0] < month or (sorted_keys[i][0] == month and sorted_keys[i][1] <= day)):
        i += 1
        
    if i >= len(sorted_keys):
        i = 0
        
    next_key = sorted_keys[i]
    return next_key, birthdays[next_key]
    
