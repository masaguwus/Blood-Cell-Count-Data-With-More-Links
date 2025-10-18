import csv
import os

char_mapping = {
    '//': '//', 
    '--': '--', 
    '**': '**'
}

path = os.getcwd() + '/Blood_Cell_Datasets_Link.txt'

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def read_line_data(row):
    if row.startswith(char_mapping['//']):
        return None
    parts = row.split(char_mapping['--'])
    if len(parts) < 3:
        return None
    return parts

def turn_txt_to_csv(txt_file_path):
    lines = read_file(txt_file_path)
    csv_file_path = txt_file_path.replace('.txt', '.csv')
    
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Index', 'Title', 'Description', 'Link'])
        
        for line in lines:
            data = read_line_data(line)
            if data:
                first_split_index = data[0].split('.', maxsplit=1)
                index = first_split_index[0].strip()
                title = first_split_index[1].strip()
                description = data[1].strip()
                link = data[2].strip()
                csvwriter.writerow([index, title, description, link])

    return csv_file_path

def main():
    txt_file_path = path
    csv_file_path = turn_txt_to_csv(txt_file_path)
    print(f"Converted {txt_file_path} to {csv_file_path}")

if __name__ == "__main__":
    main()