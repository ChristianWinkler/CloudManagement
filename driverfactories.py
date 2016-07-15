from selenium import webdriver

class LocalFirefox:
    def get(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        return webdriver.Firefox(firefox_profile=profile)
    
class LocalChrome:
    def get(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        return webdriver.Chrome(chrome_options=options)

class SeleniumHub:
    def get(self):
        return webdriver.Remote(command_executor='http://selenium-hub.dvt.intern:80/wd/hub',
                              desired_capabilities={
                                "browserName": "firefox",
                                "version": "STABLE",
                                "platform": "WIN10",
                                "javascriptEnabled": "True"
                                }
                              ) 