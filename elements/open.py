from elements.element import Element

class Open(Element):
    """ Open the web page of a delos device.

        Parameters:
        - string base_url "url of delos device"
        e.g. http://192.168.47.11
    """
    def execute(self, driver, config):
        driver.get("{base_url}".format(**config["Open"]))
        driver.set_page_load_timeout(20)