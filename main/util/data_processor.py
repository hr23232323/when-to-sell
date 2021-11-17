import pandas as pd
import os
from constants import (
    QQQ_DATA_FILE,
    QQQ_PROCESSED_DATA_FILE,
    QQQ
)

DATA_DIR = os.getcwd() + "/data/"

class Processor:
    def __init__(self):
        pass

    def process_data(self, file_name):
        # Get filepath and load raw data
        file_path = generate_filepath(file_name)
        raw_data = pd.read_csv(file_path)

        # Keep only imp fields
        processed_data = raw_data
        processed_data.drop(labels=["High", "Low", "Adj Close", "Volume"], axis=1, inplace=True)

        # Add weekly return column
        processed_data["Weekly Returns"] = round(((processed_data["Close"] - processed_data["Open"])/processed_data["Open"])*100, 3)
        return processed_data


def generate_filepath(file_name):
    return DATA_DIR  + file_name

def main():
    processor = Processor()
    qqq_processed_data = processor.process_data(QQQ_DATA_FILE)
    qqq_processed_data.to_csv(generate_filepath(QQQ_PROCESSED_DATA_FILE), index=False)


if __name__ == "__main__":
    main()
