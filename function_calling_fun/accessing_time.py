import time
def get_time_date():
    secs_since_epoch = time.time()
    localtime = time.localtime(secs_since_epoch)
    formatted_time = time.strftime('%c',localtime)
    return formatted_time