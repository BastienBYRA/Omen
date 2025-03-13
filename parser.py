import yaml

def parse_config(yaml_file_path: str):
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data.get('definition', {}).get('essential')