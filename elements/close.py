from elements.element import Element

class Close(Element):
    """ Close the web page of a delos device.
        No parameters.
    """
    def execute(self, driver, config):
        driver.close()
        print "All tests run."
