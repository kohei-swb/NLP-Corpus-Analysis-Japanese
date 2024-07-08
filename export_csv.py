import csv

def parse_data(data):
    formatted_data = []
    for item in data.split(', '):
        word, frequency = item.split(': ')
        frequency = frequency.strip('%')
        formatted_data.append({"word": word, "frequency": frequency})
    return formatted_data

# Write data to CSV

def write_data_to_csv(input_file_path, output_csv_file_path):
    with open(input_file_path, "r", encoding='utf-8') as file:
        text = file.read()
        
    lst_data = parse_data(text)
        
    with open(output_csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["word", "frequency"])
        writer.writeheader()
        for row in lst_data:
            writer.writerow(row)

input_file_path = 'Path_of_result_text'
output_csv_file_path = "Path_of_output_csv_file"

write_data_to_csv(input_file_path, output_csv_file_path)

print(f"Results have been written to {output_csv_file_path}")
