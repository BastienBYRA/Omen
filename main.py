import fire

from checker import check_config_file
from parser import parse_config

def run(name="World"):
  return "Hello %s!" % name

def check_yaml(config="."):
  # check_config_file doesn't return anything as of now
  path = check_config_file(config)
  parse_config(path)
  return "Hello!"

if __name__ == '__main__':
  fire.Fire()