import data_manager
import zlib

def generate_crc32_id(text_input):
    return zlib.crc32(text_input.encode())

def add_study_session(name, relateds=[]):
    #list study session by_id
    #if study_session already exists, returna a exception
    #else, generate a new guid for the study session
    study_session_id = generate_crc32_id(name)
    data_manager.create_study_session(study_session_id, name, relateds)
