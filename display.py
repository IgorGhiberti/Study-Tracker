import data_manager
from datetime import datetime

def formate_date(date):
    list_date = date.split('-')
    date = " ".join(list_date)
    return datetime.strptime(date, "%Y %m %d").date()

def filtered_dictionary_date(dictionary, dateStart, dateEnd):
    filtered_dict = {}
    dateEnd = formate_date(dateEnd)
    dateStart = formate_date(dateStart)
    curr_date = formate_date(dictionary['day'])        
    if curr_date <= dateEnd and curr_date >= dateStart:
        filtered_dict.update(dictionary)   
    return filtered_dict

def show_focus_logs(dateStart = '', dateEnd = ''):
    json_object = data_manager.list_focus_sessions()

    for key in json_object:
        if key != 'curr_focus_sess':
            if dateStart != '' and dateEnd != '':
                filtered_dic = filtered_dictionary_date(json_object[key], dateStart, dateEnd)
                if filtered_dic != {}:
                    print(f'{filtered_dic['day']} | Tópico: {filtered_dic['subject']} | Tempo de estudo: {filtered_dic['time_spent']}')
            else:
                print(f'{json_object[key]['day']} | Tópico: {json_object[key]['subject']} | Tempo de estudo: {json_object[key]['time_spent']}') 

show_focus_logs('2025-07-17', '2025-07-21')