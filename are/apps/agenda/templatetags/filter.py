from django import template
from datetime import datetime
register = template.Library()

@register.filter
def next(some_list, current_index): 
    try:
        return some_list[int(current_index) + 1] # access the next element
    except:
        return '' # return empty string in case of exception

@register.filter
def mytimesince(starttime,endtime):
    # import pdb; pdb.set_trace()
    end_minutes = endtime.hour*60 + endtime.minute
    start_minutes = starttime.hour*60 + starttime.minute
    temp = (end_minutes - start_minutes)/60
    hours = int(temp)
    minutes = int((temp-hours)*60)
    if minutes == 0:
        time_diff = str(hours) + " hr"
    elif hours == 0:
        time_diff = str(minutes) + " min"
    else:
        time_diff = str(hours) + " hr " + str(minutes) + " min"

    return time_diff