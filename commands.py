import data_manager
import zlib

def generate_crc32_id(text_input):
    return zlib.crc32(text_input.encode())

def list_studys_session():
    return data_manager.list_study_sessions()

def add_study_session(name, relateds=[]):
    study_session_id = generate_crc32_id(name)
    if data_manager.get_study_session_by_id(study_session_id) != None:
        raise Exception("Essa sessão de estudos já existe")
    data_manager.create_study_session(study_session_id, name, relateds)
