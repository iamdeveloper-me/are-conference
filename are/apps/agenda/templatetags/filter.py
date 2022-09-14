from django import template
register = template.Library()

@register.filter
def next(some_list, current_index): 
    try:
        return some_list[int(current_index) + 1] # access the next element
    except:
        return '' # return empty string in case of exception

@register.filter
def mytimesince(starttime,endtime):
    end_minutes = endtime.hour*60 + endtime.minute
    start_minutes = starttime.hour*60 + starttime.minute
    t1 = datetime.strptime(start_time, "%H:%M")
    return (end_minutes - start_minutes) / 60