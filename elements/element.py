class Element:
    """Base class for elements."""
    def execute(self, driver, config):
        raise NotImplementedError