"""Utilities"""


from yaml import load


def include(source):
    return load(open(source, "r"))


def process(config):
    for k, v in config.items():
        if k == "$include":
            config[k] = include(v)
    return config
