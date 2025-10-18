import json
import os

name_to_count = {
    "WBC": "<name>WBC</name>",
    "RBC": "<name>RBC</name>",
    "Platelets": "<name>Platelets</name>"
}

root_dir = os.getcwd() + "/Complete-Blood-Cell-Count-Dataset/"

def is_xml(file_name):
    if file_name.endswith(".xml"):
        return True
    return False

def process_data_total_name_counter(data = ""):
    count_RBC = data.count(name_to_count["RBC"])
    count_WBC = data.count(name_to_count["WBC"])
    count_Platelets = data.count(name_to_count["Platelets"])
    json_data = {
        "RBC": count_RBC,
        "WBC": count_WBC,
        "Platelets": count_Platelets
    }
    return json_data

def execute_counter(dir_path):
        for file in os.listdir(dir_path):
            try:
                if is_xml(file):
                    file_path = os.path.join(dir_path, file)
                    with open(file_path, 'r') as f:
                        data = f.read()
                        print(f"Processing file: {file_path}")
                        result = process_data_total_name_counter(data)
                            
                        # Write the result to a JSON file
                        file = file.split(".xml")[0]
                        with open(f"{dir_path}/{file}_count.json", 'x') as f:
                            f.write(json.dumps(result, indent=4))
                        # Example: count occurrences of a specific tag or name
                        # count = data.count("<name>desired_name</name>")
                        # print(f"Count in {file}: {count}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")

def main():
    folder = input("Enter the folder path: ").capitalize()
    dir = root_dir + folder + "/Annotations"
    execute_counter(dir)

if __name__ == "__main__":
    main()