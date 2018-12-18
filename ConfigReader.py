import yaml
from jinja2 import Template
import git


class ConfigReader:

    def __init__(self):
        pass

    def read_config(self, config_list):
        config = ""
        list_length = len(config_list)
        print(list_length)
        config = config_list[list_length-1]
        for i in range(list_length-1, 0, -1):
            print("Iteration: " + str(i))
            template = Template(config_list[i-1])
            config_dict = yaml.load(config)
            config = template.render(config_dict)
        return config

    def get_config(self):
        git.Git(".").clone("git://gitorious.org/git-python/mainline.git")


config_file_list = ["first_level.yml", "second_level.yml", "third_level.yml", ]
config_list = []
for config_file in config_file_list:
    f = open(config_file, 'r')
    config_list.append(f.read())
    f.close()

config_reader = ConfigReader()
print(config_reader.read_config(config_list))