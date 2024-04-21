import re
import os


def clean_text(text):
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"\D\.\d+", ".", text)
    text = re.sub(r"(?<=\D)\d+[,]?", "", text).strip()
    text = re.sub(r"\n", "", text)
    text = re.sub(r"\s+", " ", text)

    return text

def clean_data(data_clean, data_raw):
    for raw_file in os.listdir(data_raw):
        with open(data_raw+raw_file, 'r', encoding='utf-8') as f:
            text = f.read()
            text = clean_text(text)
            with open(data_clean + raw_file, 'w', encoding='utf-8') as f:
                f.write(text)


data_raw = "./data/raw/"
data_clean = "./data/clean/"

clean_data(data_clean, data_raw)
