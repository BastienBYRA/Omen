from dataclasses import dataclass

@dataclass
class AppConfiguration:
    endpoint: str
    sending_interval: int # In seconds