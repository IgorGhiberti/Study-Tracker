import json
from datetime import datetime
from datetime import timedelta
from pathlib import Path

TIMER_FILE = Path("timer_session.json")

def list_study_sessions(consult_by_user = False):
    with open('data/data.json', 'r') as openfile:
        study_session_objects = json.load(openfile)
    
    if not study_session_objects and consult_by_user == True:
        print("Nenhuma sessão de estudos adicionada!")
    elif consult_by_user == False and not study_session_objects:
        return None
    elif consult_by_user == True:
        study_count = 1
        for key in study_session_objects:
            if key != 'curr_session':
                print(f'Sessão {study_count}, Nome: {study_session_objects[key]['name']}')
                study_count += 1
    return study_session_objects

def get_study_session_by_id(id):
    pos = 1
    study_sessions_object = list_study_sessions()
    if study_sessions_object != None:
        for study_session in study_sessions_object:
            if study_session != 'curr_session':
                for id_study_key in study_sessions_object[study_session]:
                    if id == study_sessions_object[study_session]['id_study_sess']:
                        return study_sessions_object[study_session], pos
                    else:
                        pos += 1
    return None, pos

def create_study_session(id, name, relateds, time_spent = ''):

    study_session_dic = {
        'id_study_sess': id,
        'name': name,
        'relateds': relateds,
        'time_spent': time_spent
    }

    json_object = list_study_sessions()

    if json_object == None:
        json_object = {}
    
    #Montando outro dicionário
    dic_copy = json_object.copy()

    #Se for a primeira vez, cria a nova chave de sessão atual
    if 'curr_session' in dic_copy:
        dic_copy['curr_session'] += 1
    else:
        dic_copy['curr_session'] = 1

    new_key = 'study_session' + f'_{dic_copy['curr_session']}'
    dic_copy[new_key] = study_session_dic

    #Persiste os dados dentro do arquivo json de data
    with open("data/data.json", "w") as outfile:
        json.dump(dic_copy, outfile)

def update_study_session(study_session):    
    json_object = list_study_sessions()

    dic_copy = json_object.copy()
    pos = get_study_session_by_id(study_session['id_study_sess'])[1]
    study_sess_key = 'study_session' + f'_{pos}'
    
    study_session['time_spent'] = str(study_session['time_spent'])

    dic_copy[study_sess_key] = study_session

    with open("data/data.json", "w") as outfile:
        json.dump(dic_copy, outfile)

def start_focus_session(study_session):
    time_start = datetime.now()
    study_session['start_date'] = time_start.strftime("%d/%m/%Y %H:%M:%S")
    with open(TIMER_FILE, "w") as f:
        json.dump(study_session, f)
    return study_session
    
def end_focus_sessions():
    with open(TIMER_FILE, "r") as f:
        curr_sess = json.load(f)
        TIMER_FILE.unlink()
    start_date = datetime.strptime(curr_sess['start_date'], "%d/%m/%Y %H:%M:%S")
    end_date = timedelta(hours = datetime.now().hour, minutes= datetime.now().minute, seconds= datetime.now().second) - timedelta(hours = start_date.hour, minutes= start_date.minute, seconds= start_date.second)
    curr_sess["time_spent"] = end_date
    update_study_session(curr_sess)
    #Create a new object that contains the current day, name of the study_session, and maybe some notes


