import csv

# Input CSV file and output CSV file names
input_csv_filename = "HospitalsListOriginal.csv"
output_csv_filename = "HospitalsList.csv"

# Function to extract and reformat data
def extract_data(row):
    hospital_name = row['SV_NAME']
    latitude = row['LATITUDE']
    longitude = row['LONGITUDE']
    return [hospital_name, latitude, longitude]

# Open the input and output CSV files
with open(input_csv_filename, mode='r') as input_file, open(output_csv_filename, mode='w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    
    # Define the header for the output CSV file
    fieldnames = ['hospitalname', 'latitude', 'longitude']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    
    # Write the header to the output CSV file
    writer.writeheader()
    
    # Iterate through each row in the input CSV file
    for row in reader:
        # Extract the desired data
        extracted_data = extract_data(row)
        
        # Write the extracted data to the output CSV file
        writer.writerow({'hospitalname': extracted_data[0], 'latitude': extracted_data[1], 'longitude': extracted_data[2]})


