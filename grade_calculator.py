import pandas as pd

# Read the CSV file
final_student_grades = pd.DataFrame()
df = pd.read_csv('student_grades.csv')
# Combine "FIRST" and "LAST" columns into a single "FULL NAME" column
df['FULL NAME'] = df['FIRST'] + ' ' + df['LAST']

# Drop the "FIRST" and "LAST" columns if you no longer need them
df = df.drop(['FIRST', 'LAST'], axis=1)

# Reorder the columns with the last column as the first column
df = df[['FULL NAME'] + [col for col in df.columns if col != 'FULL NAME']]

# Create a new column with calculated values
df['CLASS_AVERAGE'] = df[['EXAM_1_GRADE','EXAM_2_GRADE','EXAM_3_GRADE','EXAM_4_GRADE']].mean(axis=1)



# Save the updated DataFrame to a new CSV file
df.to_csv('final_student_grades.csv', index=False)
# print(df)


