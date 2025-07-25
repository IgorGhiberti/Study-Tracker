import data_manager
import zlib
import display

def generate_crc32_id(text_input):
    return zlib.crc32(text_input.encode())

def list_studys_session(consultByUser = False):
    return data_manager.list_study_sessions(consultByUser)

def add_study_session(name, relateds=[]):
    study_session_id = generate_crc32_id(name)
    if data_manager.get_study_session_by_id(study_session_id)[0] != None:
        raise Exception("Essa sessão de estudos já existe")
    data_manager.create_study_session(study_session_id, name, relateds)

def start_focus_session(name):
    study_session_id = generate_crc32_id(name)
    if data_manager.get_study_session_by_id(study_session_id)[0] == None:
        raise Exception("Essa sessão não existe")
    study_session = data_manager.get_study_session_by_id(study_session_id)[0]
    return data_manager.start_focus_session(study_session)

def end_focus_sessions():
    data_manager.end_focus_sessions()

def show_logs(dataStart = '', dataEnd = '', full_time=False):
    if dataStart != '' and dataEnd != '':
        display.show_focus_logs(dataStart, dataEnd)
    elif full_time == True:
        display.show_focus_logs(full_time=True)
    else:
        display.show_focus_logs()
