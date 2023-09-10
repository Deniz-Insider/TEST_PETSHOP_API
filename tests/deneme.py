import requests
from base_functions.base_functions import BaseFunctions


class MyClass(BaseFunctions):

    ENDPOINT = "https://petstore.swagger.io/v2/"

    def test_can_add_new_pet(self):
        add_pet_payload = BaseFunctions.generate_payload(self)

        add_pet_response = requests.post(self.ENDPOINT + "pet", json=add_pet_payload)
        data = add_pet_response.json()

        assert add_pet_response.status_code == 200
        print("Status Code: ", add_pet_response.status_code)
        print(data)


