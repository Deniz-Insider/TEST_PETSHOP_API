import uuid
import requests


class BaseFunctions():

    ENDPOINT = "https://petstore.swagger.io/v2/"

    def generate_payload(self):
        return {
            "id": uuid.uuid4().hex,
            "name": "pet"+uuid.uuid4().hex,
            "photoUrls": [
                "cdn."+uuid.uuid4().hex+".com"
            ],

            "status": "available"
        }

    def create_pet(self):
        return requests.post(self.ENDPOINT + "pet", json=BaseFunctions.generate_payload(self))