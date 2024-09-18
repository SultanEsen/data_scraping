import pandas as pd
import logging


class MoldovaFileParser:
    @classmethod
    def read_file(cls, path):
        logging.info(f"Reading file {path}")
        tables = pd.read_excel(path)
        return tables