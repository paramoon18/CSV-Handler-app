import pandas as pd
import glob

# --------------------------------------------------
# Step 1: Load the TEPIX_W_IDX file, due to the consisty of this file with market working day its use as a master_file.
# --------------------------------------------------
# Reads the TEPIX_W_IDX file, which holds the reference for dates (<DTYYYYMMDD>).
master_file = pd.read_csv("TEPIX_W_IDX.txt", index_col=False)
# Extract only the date column from the master file.
master_dates = master_file[["<DTYYYYMMDD>"]]
# Creating a copy for potential future enhancements (currently redundant).
merged_df = master_dates.copy()

# --------------------------------------------------
# Step 2: Identify all relevant data files.
# --------------------------------------------------
# Use glob to collect all text files under the specified directory.
files = glob.glob("Iran Stock market datas\\*.txt")

# --------------------------------------------------
# Step 3: Process and merge each file.
# --------------------------------------------------
for file_path in files:
    try:
        # Read the current file into a DataFrame.
        df = pd.read_csv(file_path, index_col=False)

        # Check if the file is empty or missing critical columns.
        if df.empty or "<DTYYYYMMDD>" not in df.columns or "<Close>" not in df.columns:
            print(f"Skipping file {file_path} due to missing columns or empty data.")
            continue
        
        # The first cell of the file is used as the new column name for the Close values.
        col_name = df.iloc[0, 0]
        # Filter the DataFrame to keep only date and close price columns.
        df_temp = df[["<DTYYYYMMDD>", "<Close>"]].copy()

        # Rename the <Close> column to the name derived from the file for clarity.
        df_temp.rename(columns={"<Close>": col_name}, inplace=True)
        # Merge the temporary DataFrame with the master dates based on the date column.
        master_dates = master_dates.merge(df_temp, on="<DTYYYYMMDD>", how="left")
    
    except Exception as e:
        # If an error occurs, log it and continue with the next file.
        print(f"Error processing file {file_path}: {e}")

# --------------------------------------------------
# Step 4: Save the merged DataFrame to a CSV file.
# --------------------------------------------------
output_path = "final file directory\\merged.csv"
master_dates.to_csv(output_path, index=False)
print(f"Master file with <Close> values saved as: {output_path}")
