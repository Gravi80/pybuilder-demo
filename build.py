from os import sys, path

from pybuilder.plugins.python.install_dependencies_plugin import install_dependency

project_path = path.dirname(path.abspath(__file__))
sys.path.append(f'{project_path}/main')

from pybuilder.core import use_plugin, init, Author, task, before, depends, RequirementsFile
from pybuilder_demo import __version__

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin('pypi:pybuilder_pytest')
use_plugin('pypi:pybuilder_pytest_coverage')

name = "pybuilder-demo"
version = __version__
summary = "An example project for configuring pybuilder"
description = """An example project for configuring pybuilder."""

authors = [Author("Ravi Sharma", "ravi.sharma.cs11@gmail.com")]
url = ""
license = "GPL License"
default_task = ["clean"]


@init
def initialize(project):
    project.depends_on_requirements("requirements.txt")
    project.build_depends_on_requirements("dev_requirements.txt")
    project.set_property('dir_source_main_python', 'main')
    project.set_property('dir_source_pytest_python', 'unittest')
    project.set_property('dir_source_main_scripts', 'main/scripts')
    project.set_property("pytest_coverage_break_build_threshold", 90)
    project.set_property("pytest_coverage_html", True)


@before("run_unit_tests", only_once=True)
def configure_pytest(project, logger):
    test_requirement = RequirementsFile("unittest/test_requirements.txt")
    install_dependency(logger, project, [test_requirement])
    project.get_property("pytest_extra_args").append("-xsvv")
    project.get_property("pytest_extra_args").append("--junitxml=target/reports/junit.xml")


@task
@depends("install_build_dependencies")
def run_unit_tests():
    pass


@depends("install_build_dependencies")
@task(description="Run pybuilder-demo")
def run(project):
    from pybuilder_demo.main import start
    arg1 = project.get_property("arg1")
    arg2 = project.get_property("arg2")
    conf = project.get_property("conf")
    start(arg1, arg2, conf)
