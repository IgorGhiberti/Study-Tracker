import data_manager
from datetime import datetime, timedelta
from collections import defaultdict

def formate_date(date):
    list_date = date.split('-')
    date = " ".join(list_date)
    return datetime.strptime(date, "%Y %m %d").date()

def formate_time(time):
    h, m, s = map(int, time.split(":"))
    return timedelta(hours=h, minutes=m, seconds=s)

def filtered_dictionary_name(dictionary, names):
    filtered_dic = []
    for key in dictionary:
        if dictionary[key]['subject'] in names:
            filtered_dic.append(dictionary[key]['subject'])
    return filtered_dic

def show_amount_of_time(dictionary):
    total_per_day = defaultdict(timedelta)
    for key, value in dictionary.items():
        if key != 'curr_focus_sess':
            time_spent = value.get('time_spent', '00:00:00')
            day = value.get('day')
            if time_spent and day:
                total_per_day[day] += formate_time(time_spent)
    return total_per_day

def filtered_dictionary_date(dictionary, dateStart, dateEnd):
    filtered_dict = {}
    dateEnd = formate_date(dateEnd)
    dateStart = formate_date(dateStart)
    curr_date = formate_date(dictionary['day'])        
    if curr_date <= dateEnd and curr_date >= dateStart:
        filtered_dict.update(dictionary)   
    return filtered_dict

def show_focus_logs(dateStart = '', dateEnd = '', full_time = False):
    json_object = data_manager.list_focus_sessions()

    if full_time == True:
        total_per_day = show_amount_of_time(json_object)
        for day, total_time in sorted(total_per_day.items()):
            print(f'{day} | Tempo de estudo: {str(total_time)}')
        return
    
    for key in json_object:
        if key != 'curr_focus_sess':
            if dateStart != '' and dateEnd != '':
                filtered_dic = filtered_dictionary_date(json_object[key], dateStart, dateEnd)
                if filtered_dic != {}:
                    print(f'{filtered_dic['day']} | Tópico: {filtered_dic['subject']} | Tempo de estudo: {filtered_dic['time_spent']}')
            else:
                print(f'{json_object[key]['day']} | Tópico: {json_object[key]['subject']} | Tempo de estudo: {json_object[key]['time_spent']}')