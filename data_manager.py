import json

def create_study_session(id, name, relateds):

    study_session_dic = {
        'id_study_sess': id,
        'name': name,
        'relateds': relateds 
    }

    with open('data/data.json', 'r') as openfile:
        json_object = json.load(openfile)
    
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
    