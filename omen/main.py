import fire

from models.definition import Definition
import workflow.validator as validator
import workflow.parser as parser

# def run(name="World"):
#   return "Hello %s!" % name

def run(config="."):
  path = validator.validate_config_file_path(config)
  definition: dict[str, Definition] = parser.parse_config(path)
  metrics = parser.get_metrics(path, definition)

if __name__ == '__main__':
  fire.Fire()