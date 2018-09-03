Configuring pybuilder for developing command-line application

#### Development setup
1. Create python3 virtual environment
    ```
    $ python3 -m venv venv-name

    $ source venv-name/bin/activate
    ```

2. Install pybuilder
    ```
    $ pip install pybuilder
    ```

3. Run main method
    ```
    $ pyb run -P arg1="param1" -P arg2="param1" -P conf="./default_conf"
    ```

###### Tests
1. Run unittests

    ```
    $ pyb run_unit_tests
    ```

###### Packaging
1. Generate pip package
    ```
    $ pyb publish
    ```
2. package location

    target/dist/pybuilder-demo-<version>/dist/pybuilder-demo-<version>.tar.gz


#### Production setup
1. Create python3 virtual environment
    ```
    $ python3 -m venv prod-venv-name

    $ source prod-venv-name/bin/activate
    ```

2. Install pybuilder-demo package
    ```
    $ pip install <pybuilder-demo-package-path>
    ```

3. Run main method
    ```
    $ pyb-demo --help
    $ pyb-demo --arg1="<param1>" --arg2="<param2>" --conf="<custom_conf_dir>"
    ```
    OR
    ```
    $ pyb-demo
    ```

    **--conf** has default value set to \<prod-venv-name\>/etc/configs