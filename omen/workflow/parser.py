import yaml

from models.definition import Definition
from models.definitionField import DefinitionField
from workflow.transformer import transform_to_prometheus_metrics

def parse_config(yaml_file_path: str) -> dict[Definition]:
    """
    Parse the configuration file and return a dictionary of Definition objects
    """
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)

        # Get definition objects
        list_definition: list[dict] = data.get('definition')
        if not list_definition:
            return {}

        definition_dict: dict[str, Definition] = {}
        for definition in list_definition:
            val: Definition = get_definition(definition)
            definition_dict[val.name] = val

        # Get metrics objects
        list_metrics: list[dict] = data.get('metrics')
        if not list_metrics:
            print("No metrics list found in the configuration file")
            exit(1)

        get_metrics(list_metrics, definition_dict)

        exit(0)
        # return definition_dict
    

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


def get_metrics(list_metrics: list[dict], definition_dict: dict[str, Definition]):

    for metric in list_metrics:
        # For each metric defined in "metrics", get the name
        metrics_name: str = next(iter(metric.keys())) # https://stackoverflow.com/questions/18686903/dict-keys0-on-python-3

        if definition_dict.get(metrics_name):
            metrics_description = definition_dict.get(metrics_name).description
            # TODO: Check the fields match with the definition
            transform_to_prometheus_metrics(metrics_name, metric, metrics_description)
        else:
            # dict_metrics_to_prometheus_metrics(metrics_name, metric)
            print("No")