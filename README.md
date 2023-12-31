# Emotions_DL

Develop methods to identify the intensity of emotions in text and submit a technical paper detailing the approaches used.
download the dataset from https://competitions.codalab.org/competitions/16380.
and convert the text file into csv file using the below code.


# Emotion_ML
Develop methods to identify the intensity of emotions in text and submit a technical paper detailing the approaches used.

Download the dataset from :https://competitions.codalab.org/competitions/16380
and convert the Text file into csv file.

import csv

# Specify the input and output file paths
input_file_path = '/content/fear2.txt'
output_csv_path = r'C:\Users\CHETHU\Downloads\fear2.csv'

# Open the text file for reading
with open(input_file_path, 'r') as txt_file:
    # Read the content of the text file
    txt_content = txt_file.readlines()

# Open the CSV file for writing
with open(output_csv_path, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Iterate through each line of the text file and write it to the CSV file
    for line in txt_content:
        # Assuming the values are separated by tabs (you can change the delimiter if needed)
        values = line.strip().split('\t')

        # Write the values to the CSV file
        csv_writer.writerow(values)

print(f'Text file "{input_file_path}" has been successfully converted to CSV file "{output_csv_path}".')
