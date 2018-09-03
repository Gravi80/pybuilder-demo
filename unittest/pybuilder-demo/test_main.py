from mock import patch

from pybuilder_demo.main import start


class TestMain:

    @patch("pybuilder_demo.main.DemoClass")
    @patch("pybuilder_demo.main.path")
    def test_should_start_project(self, os_path_mock, DemoClassMock):
        arg1, arg2, conf = 'arg1', 'arg2', 'conf_dir'
        expanded_path = "conf_expanded_path"
        absolute_path = "conf_absolute_path"
        start_return = "start string"
        os_path_mock.expanduser.return_value = expanded_path
        os_path_mock.abspath.return_value = absolute_path
        DemoClassMock.start_method.return_value = start_return

        start(arg1, arg2, conf)

        os_path_mock.expanduser.assert_called_once_with(conf)
        os_path_mock.abspath.assert_called_once_with(expanded_path)
        DemoClassMock.start_method.assert_called_once()
