from dataclasses import dataclass

from models.definitionField import DefinitionField

@dataclass
class Definition:
    name: str
    description: str
    fields: dict[str, DefinitionField]
    fields_required_by_default: bool = False