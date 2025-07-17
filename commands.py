import data_manager
import zlib

def generate_crc32_id(text_input):
    return zlib.crc32(text_input.encode())

def build_json_file():
    return data_manager.build_json()

def list_studys_session():
    return data_manager.list_study_sessions()

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
