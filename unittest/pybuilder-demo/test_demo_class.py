from pybuilder_demo.demo_class import DemoClass


class TestDemoClass:
    def test_start_method(self):
        start_string = DemoClass.start_method()

        assert "Starting pybuilder-demo project.... " == start_string
