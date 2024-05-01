import pandas as pd

def extract_locations(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    locations = set()  # Use a set to store unique locations
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        location = row['INCIDENT_LOCATION'].strip()  # Assuming the field is called 'INCIDENT_LOCATION'
        if location:  # Check if the location field is not empty
            # Split the location by comma and extract the portion after the comma
            location_parts = location.split(',')
            if len(location_parts) > 1:
                location_after_comma = location_parts[1].strip()
                locations.add(location_after_comma)
    
    return locations

# Example usage
csv_file = '../data/incident_response.csv'  # Replace with the path to your CSV file
unique_locations = extract_locations(csv_file)
print("Unique Locations:")
for location in unique_locations:
    print(location)
