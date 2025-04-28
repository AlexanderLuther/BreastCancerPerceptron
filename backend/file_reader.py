import pandas as pd
from backend.exception.HellException import HellException

class FileReader:

    def __init__(self, headers):
        self.__headers = headers
        pass

    def read_data(self, file_path):
        try:
            columns = ['id', 'diagnosis'] + self.__headers
            return pd.read_csv(file_path, header=None, names=columns)
        except Exception as e:
            raise HellException from e