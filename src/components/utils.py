import pickle


def save_pickle(file_name,file_path):
    with open(file_path,"wb") as file:
        pickle.dump(file_name,file)

def load_object(file_path):
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

