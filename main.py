import shutil
import requests

from driverfactories import *
from secuencies import *

def main():
    driver_factory = LocalFirefox()
    config={
              "Open" : {
                        "base_url": "https://bs-ct-dev.devolo.net/#/"
                        },
              "Login": {
                        "login": "vitalii.petruniak@sogeti.de",
                        "password": "NatAw1988"
                        }
            }
    
    OpenLoginClose().execute(driver_factory.get(), config)
  
if __name__ == "__main__":
    main()