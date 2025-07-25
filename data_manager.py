import json
from datetime import datetime
from datetime import timedelta
from datetime import date
from pathlib import Path

TIMER_FILE = Path("timer_session.json")

def build_json():
    try:
        with open('data/data.json', 'r') as openfile:
            json_object = json.load(openfile)
            return json_object
    except:
        dic_build = {"study_sessions": {}, "focus_sess": {}}
        with open("data/data.json", "w") as outfile:
            json.dump(dic_build, outfile)
            return dic_build

def list_study_sessions(consult_by_user = False):
    
    json_objects = build_json()

    study_session_objects = json_objects['study_sessions']
    if not study_session_objects and consult_by_user == True:
        print("Nenhuma sessão de estudos adicionada!")
    elif consult_by_user == False and not study_session_objects:
        return None
    elif consult_by_user == True:
        study_count = 1
        for key in study_session_objects:
            if key != 'curr_session':
                print(f'Sessão {study_count}, Nome: {study_session_objects[key]['name']}')
                if study_session_objects[key]["relateds"] != None:
                    print('Matérias associadas:')
                    for related in study_session_objects[key]["relateds"]:
                        print(f'->{related}')
                study_count += 1
    return study_session_objects

def list_focus_sessions():
    focus_sessions_object = build_json()

    return focus_sessions_object['focus_sess']

def get_study_session_by_id(id):
    pos = 1
    study_sessions_object = list_study_sessions()
    if study_sessions_object != None:
        for study_session in study_sessions_object:
            if study_session != 'curr_session':
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

    json_object = build_json()
    
    #Montando outro dicionário
    dic_copy = json_object['study_sessions'].copy()

    #Se for a primeira vez, cria a nova chave de sessão atual
    if 'curr_session' in dic_copy:
        dic_copy['curr_session'] += 1
    else:
        dic_copy['curr_session'] = 1

    new_key = 'study_session' + f'_{dic_copy['curr_session']}'
    dic_copy[new_key] = study_session_dic

    #Utiliza o model (dic_copy) para persistir os dados no arquivo json (json_object)
    if new_key not in json_object['study_sessions']:
        json_object['study_sessions'] = dic_copy

    #Persiste os dados dentro do arquivo json de data
    with open("data/data.json", "w") as outfile:
        json.dump(json_object, outfile)

def update_study_session(study_session):    
    json_object = build_json()

    dic_copy = json_object.copy()
    pos = get_study_session_by_id(study_session['id_study_sess'])[1]
    study_sess_key = 'study_session' + f'_{pos}'
    
    #Converte tipo data para string, para poder ser escrito no json
    study_session['time_spent'] = str(study_session['time_spent'])

    dic_copy[study_sess_key] = study_session

    json_object['study_sessions'][study_sess_key] = dic_copy[study_sess_key]

    with open("data/data.json", "w") as outfile:
        json.dump(json_object, outfile)

def create_focus_session(subject, day, time_spent, notes = ''):

    json_object = build_json()

    focus_sessions_dic = {
        "subject": subject,
        "day": str(day),
        "time_spent": time_spent,
        "notes": notes
    }

    json_object = build_json()

    dic_copy_focus = json_object['focus_sess'].copy()

    if 'curr_focus_sess' in dic_copy_focus:
        dic_copy_focus['curr_focus_sess'] += 1
    else:
        dic_copy_focus['curr_focus_sess'] = 1
    
    new_key = 'focus_sess' + f'_{dic_copy_focus['curr_focus_sess']}'
    dic_copy_focus[new_key] = focus_sessions_dic
    dic_copy_focus[new_key]['id_focus_sess'] = dic_copy_focus['curr_focus_sess']

    json_object['focus_sess'] = dic_copy_focus
    #Persiste os dados dentro do arquivo json de data
    with open("data/data.json", "w") as outfile:
        json.dump(json_object, outfile)

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
    start_time = datetime.strptime(curr_sess['start_date'], "%d/%m/%Y %H:%M:%S")
    curr_day = date.today()
    end_date = timedelta(hours = datetime.now().hour, minutes= datetime.now().minute, seconds= datetime.now().second) - timedelta(hours = start_time.hour, minutes= start_time.minute, seconds= start_time.second)
    curr_sess["time_spent"] = end_date
    update_study_session(curr_sess)
    create_focus_session(curr_sess['name'], curr_day, curr_sess["time_spent"])



