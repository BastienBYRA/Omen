import os

def check_config_file(path: str):
    # Convert to absolute path if it's not already
    abs_path: str = os.path.abspath(path)
    
    if os.path.isfile(abs_path):
        print(f"The file '{abs_path}' exists.")

    elif os.path.isdir(abs_path):
        omen_yml_path: str = os.path.join(abs_path, 'omen.yml')
        omen_yaml_path: str = os.path.join(abs_path, 'omen.yaml')
        if os.path.isfile(omen_yml_path) or os.path.isfile(omen_yaml_path):
            print(f"The directory '{abs_path}' contains 'omen.yml' or 'omen.yaml'.")
        else:
            print(f"The directory '{abs_path}' does not contain 'omen.yml' or 'omen.yaml'.")
            
    else:
        print(f"The path '{abs_path}' does not exist.")