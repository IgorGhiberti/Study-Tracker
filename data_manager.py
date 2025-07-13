import json

def list_study_sessions():
    with open('data/data.json', 'r') as openfile:
        study_session_objects = json.load(openfile)
    
    if not study_session_objects:
        raise Exception('Nenhuma sessão de estudos adicionada')
    
    study_count = 1
    for key in study_session_objects:
        if key != 'curr_session':
            print(f'Sessão {study_count}, Nome: {study_session_objects[key]['name']}')
            study_count += 1
    return study_session_objects

def get_study_session_by_id(id):
    study_sessions_object = list_study_sessions()

    for study_session in study_sessions_object:
        if study_session != 'curr_session':
            for id_study_key in study_sessions_object[study_session]:
                if id == study_sessions_object[study_session]['id_study_sess']:
                    return study_sessions_object[study_session]['id_study_sess']
    return None

def create_study_session(id, name, relateds):

    study_session_dic = {
        'id_study_sess': id,
        'name': name,
        'relateds': relateds 
    }

    json_object = list_study_sessions()
    
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
    