# excel_sheet_update.py
import os
import pandas as pd

def update_excel_sheet(recognized_faces, dataset_names):
    # Check if the CSV file exists
    csv_file = 'attendance.csv'
    if not os.path.exists(csv_file):
        # Create a DataFrame with dataset names
        attendance_df = pd.DataFrame(index=dataset_names, columns=['Status'])
        # Write the DataFrame to a CSV file
        attendance_df.to_csv(csv_file, index_label='Name')

    # Read the CSV file into a DataFrame
    attendance_df = pd.read_csv(csv_file, index_col='Name')

    # Update attendance status based on recognized faces
    for name, status in recognized_faces.items():
        if status == 'Not identified':
            attendance_df.loc[name] = 'Absent'
        else:
            attendance_df.loc[name] = 'Present'

    # Write the updated DataFrame to the CSV file
    attendance_df.to_csv(csv_file)
