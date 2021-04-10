time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}

def convert(time):
    try:
        return int(time[:-1]) * time_convert[time[-1]]
    
    except:
        return time