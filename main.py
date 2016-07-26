import shutil
import requests
import address


from driverfactories import *
from secuencies import *

def main():
    driver_factory = LocalFirefox()
    config={
              "Open" : {
                        "base_url": "https://bs-ct-dev.devolo.net"
                        },
              "Login": {
                        "login": "vitalii.petruniak@sogeti.de",
                        "password": "NatAw1988"
                        },
            "LocationData" : {
                              "new_name": address.generateName(5, 30),
                              "new_address": address.generateAddress(6, 50),
                              "new_city": address.generateCity(3, 20),
                              "new_postcode": address.generatePostcode(3, 8)
                              }
            }
    
    OpenLoginLocationlistClose().execute(driver_factory.get(), config)
  
if __name__ == "__main__":
    main()