from pybuilder_demo.demo_class import DemoClass
from os import path


def start(arg1, arg2, conf):
    conf_path = path.abspath(path.expanduser(conf))
    print(f"arg1={arg1}")
    print(f"arg2={arg2}")
    print(f"conf={conf_path}")
    print(DemoClass.start_method())
