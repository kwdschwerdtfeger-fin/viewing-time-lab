def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.

    We need to skip that 0 row (aka the 1st row)
    """
    clean_data = []
    # scalable data design
    # hard-coded vaues (yellow flag), this won't scale well!
    # Hard coding is a beige to yellow to red flag
    # What are the diff scenarios where this breaks???
    for row in data:
        if row != "minutes\n":
            clean_data.append(float(row.strip()))    
    return clean_data