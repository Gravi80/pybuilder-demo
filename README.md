$ pip install pybuilder
$ pyb <task>
$ pyb install_build_dependencies
$ pyb run -P arg1="param1" -P arg2="param1" -P conf="./default_conf"

TEST
$ pyb run_unit_tests


install_build_dependencies - Installs all build dependencies specified in the build descriptor
install_dependencies - Installs all (both runtime and build) dependencies specified in the build descriptor
install_runtime_dependencies - Installs all runtime dependencies specified in the build descriptor
