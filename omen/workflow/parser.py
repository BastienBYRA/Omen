import yaml

from models.definition import Definition
from models.definitionField import DefinitionField

def parse_config(yaml_file_path: str) -> dict[Definition]:
    """
    Parse the configuration file and return a dictionary of Definition objects
    """
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)

        list_definition: list[dict] = data.get('definition')
        if not list_definition:
            return {}

        definition_dict: dict[str, Definition] = {}
        for definition in list_definition:
            val: Definition = get_definition(definition)
            definition_dict[val.name] = val

        return definition_dict
    

def get_definition(definition_dict: dict):
    """
    Parse the definition dictionary and return a Definition object
    """

    # Definition object
    name: str = definition_dict.get('name')
    description: str = definition_dict.get('description')
    fields: list[dict] = definition_dict.get('fields')
    fields_required_by_default: bool = definition_dict.get('fields_required_by_default')

    definition_field_dict: dict[str, DefinitionField] = {}

    # Get DefinitionField objects
    for definition_field in fields:
        definition_field_name: str = definition_field.get('name')
        definition_field_description: str = definition_field.get('description')
        definition_field_type: str = definition_field.get('type')
        definition_field_required: bool = definition_field.get('required')

        if not definition_field_name:
            print("Name not found in definition field")
            exit(1)

        definition_field: DefinitionField = DefinitionField(definition_field_name, definition_field_description, definition_field_type, definition_field_required)
        definition_field_dict[definition_field_name] = definition_field

    definition: Definition = Definition(name, description, definition_field_dict, fields_required_by_default)

    return definition