import importlib


class Router:
    def __init__(self):
        self.parameters = {}

    def set_parameters(self, default_parameters, action):
        # Reset parameters since running in a loop
        self.parameters = {}

        # Add default parameters
        self.parameters.update(default_parameters)

        # Import parameter_bags module
        parameter_bags_module = importlib.import_module(
            '...parameter_bags',
            package='search_tool.search_engine.parameter_bags'
        )

        # Get parameter bag and make it callable
        parameters_bag_class_callable = getattr(parameter_bags_module, 'ParameterBag')

        # Check if the controller method has a corresponding method in the parameter bag
        if not hasattr(parameters_bag_class_callable(), action):
            return

        # Get parameter bag method and make it callable
        parameters_bag_method_callable = getattr(parameters_bag_class_callable(), action)

        self.parameters.update(parameters_bag_method_callable())

    def route(self, action, search_engine):
        # Import controller module
        controllers_module = importlib.import_module('...controller', package='search_tool.search_engine.controller')

        # Load Controller class
        controller_class = getattr(controllers_module, 'Controller')

        # Handle actions that do not exist
        if not hasattr(controller_class, action):
            controller_method = getattr(controller_class(), 'not_found')
            self.set_parameters({'action': action}, action)
            return controller_method(**self.parameters)

        if action == 'help':
            controller_method = getattr(controller_class(), action)
            self.set_parameters({}, action)
            return controller_method(**self.parameters)

        # Handle implemented actions
        controller_method = getattr(controller_class(), action)
        self.set_parameters({'search_engine': search_engine}, action)

        return controller_method(**self.parameters)
