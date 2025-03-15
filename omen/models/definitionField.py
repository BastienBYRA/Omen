from dataclasses import dataclass

@dataclass
class DefinitionField:
    name: str
    description: str
    type: str = "string"
    required: bool = False