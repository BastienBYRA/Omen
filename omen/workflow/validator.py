import os

def validate_config_file_path(path: str) -> str:
    """
    Validate the path to the configuration file.
    """
    abs_path: str = os.path.abspath(path)
    if os.path.isfile(abs_path):
        return abs_path

    elif os.path.isdir(abs_path):
        omen_yml_path: str = os.path.join(abs_path, 'omen.yml')
        omen_yaml_path: str = os.path.join(abs_path, 'omen.yaml')
        if os.path.isfile(omen_yml_path):
            return omen_yml_path
        elif os.path.isfile(omen_yaml_path):
            return omen_yaml_path
        else:
            print(f"The directory '{abs_path}' does not contain 'omen.yml' or 'omen.yaml'.")
    else:
        print(f"The path '{abs_path}' does not exist.")
    exit(1)