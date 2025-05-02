# CSV-Handler-app

# Iranian Stock Market Data Merger

This project contains a Python script that processes and merges various text files containing Iran stock market data. Due to restrictions on publicly available market data in Iran, the script reorganizes raw data into a structured CSV file that is easier to analyze.

## Features
- **Master file reading:** Loads the main reference file (`TEPIX_W_IDX.txt`) containing date information.
- **Dynamic data merging:** Iterates over all data files, extracts the `<DTYYYYMMDD>` and `<Close>` columns, and merges them based on date.
- **Flexible column naming:** Uses a dynamic approach by setting the new column name (for close prices) from the first cell of each file.
- **Robust error handling:** Skips files that don’t have the expected structure and logs any exceptions.

## Requirements
- Python 3.x
- Pandas
- Glob (standard Python library)

## Usage
1. Place the `TEPIX_W_IDX.txt` master file in the same directory as the script.
2. Ensure that the additional data files are located in the directory.
3. Run the script with: `python your_script.py`
4. The merged output will be saved as `final file directory\merged.csv`.
