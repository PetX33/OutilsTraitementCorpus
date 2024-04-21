from collections import defaultdict
from sklearn.model_selection import train_test_split
import os
import pandas as pd

def create_balanced_csv(folder, folder_csv):
    data_by_language = defaultdict(list)

    for file in os.listdir(folder):
        # print(file)
        lang = file.split("_")[-1].split(".")[0]
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            text = f.read()
        if text:
            data_by_language[lang].append(text)
    
    filtered_data_by_language = {lang: lines for lang, lines in data_by_language.items() if len(lines) > 2}
    min_lines = min(len(lines) for lines in filtered_data_by_language.values())
    balanced_data = []

    for lang, lines in filtered_data_by_language.items():
        if lines:
            balanced_data.extend((lang, line) for line in lines[:min_lines])

    df_balanced = pd.DataFrame(balanced_data, columns=["Label", "Text"])
    os.makedirs(folder_csv, exist_ok=True)
    df_balanced.to_csv(os.path.join(folder_csv, "data_balanced.csv"), index=False, encoding="utf-8")


def create_train_test_csv(csv_balanced, folder_csv):
    df_train, df_test = train_test_split(csv_balanced, test_size=0.2, random_state=42)
    df_train.to_csv(os.path.join(folder_csv, "data_train.csv"), index=False, encoding="utf-8")
    df_test.to_csv(os.path.join(folder_csv, "data_test.csv"), index=False, encoding="utf-8")


def main():
    folder_csv = "./data/csv/"
    folder_txt_files = "./data/clean/"
    create_balanced_csv(folder_txt_files, folder_csv)
    df_balanced = pd.read_csv(os.path.join(folder_csv, "data_balanced.csv"), encoding="utf-8")
    create_train_test_csv(df_balanced, folder_csv)


if __name__ == "__main__":
    main()