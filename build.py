from os import listdir, sys, path

from pybuilder.plugins.python.install_dependencies_plugin import install_dependency

project_path = path.dirname(path.abspath(__file__))
sys.path.append(f'{project_path}/main')

from pybuilder.core import use_plugin, init, Author, task, before, depends, RequirementsFile
from pybuilder_demo import __version__

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin('pypi:pybuilder_pytest')
use_plugin('pypi:pybuilder_pytest_coverage')
use_plugin("copy_resources")
use_plugin("python.distutils")

name = "pybuilder-demo"
version = __version__
summary = "An example project for configuring pybuilder"
description = """An example project for configuring pybuilder."""

authors = [Author("Ravi Sharma", "ravi.sharma.cs11@gmail.com")]
url = "https://github.com/imravishar/pybuilder-demo"
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


@before("package")
def package_configs_file(project, logger):
    logger.info("Copying non python source files i.e all config files")
    project.set_property('include_package_data', True)
    project.get_property("copy_resources_glob").append("default_conf/*")
    project.set_property("copy_resources_target", "$dir_dist/pybuilder_demo")
    project.package_data.update({'pybuilder_demo': ["default_conf/*"]})


@task(description="Setup configs files default location")
def package(project, logger):
    logger.info("All configs will be copied to '<virtual_env>/etc' directory "
                "during installation")
    conf_source_directory = 'build/lib/pybuilder_demo/default_conf'
    destination = "etc/configs"
    config_files = map(lambda conf_file: "{0}/{1}".format(conf_source_directory, conf_file),
                       listdir(project.expand_path('$dir_dist/pybuilder_demo/default_conf')))
    project.files_to_install.extend([(destination, config_files)])


@depends("install_runtime_dependencies")
def publish():
    pass


@depends("install_build_dependencies")
@task(description="Run pybuilder-demo")
def run(project):
    from pybuilder_demo.main import start
    arg1 = project.get_property("arg1")
    arg2 = project.get_property("arg2")
    conf = project.get_property("conf")
    start(arg1, arg2, conf)
