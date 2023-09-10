import requests
from base_functions.base_functions import BaseFunctions


class TestDemoApi(BaseFunctions):

    ENDPOINT = "https://petstore.swagger.io/v2/"

    def test_can_add_new_pet(self):
        add_pet_payload = BaseFunctions.generate_payload(self)

        add_pet_response = requests.post(self.ENDPOINT + "pet", json=add_pet_payload)
        data = add_pet_response.json()

        assert add_pet_response.status_code == 200
        print("Status Code: ", add_pet_response.status_code)


    def test_can_get_pet(self):
        add_pet_request = requests.post(self.ENDPOINT + "pet", json=BaseFunctions.generate_payload(self))
        assert add_pet_request.status_code == 200

        add_pet_response = add_pet_request.json()
        pet_id = add_pet_response["id"]
        # pet_name = add_pet_response["name"]
        # pet_photo = add_pet_response["photoUrls"][0]
        # status = add_pet_response["status"]

        get_pet_request = requests.get(self.ENDPOINT + "pet/{}".format(pet_id))
        assert get_pet_request.status_code == 200


        get_pet_response = get_pet_request.json()
        print("Pet Info: ", get_pet_response)

        assert add_pet_response["id"] == get_pet_response["id"]
        #print(("Add_Pet_ID: ", add_pet_response["id"]), ("Get_Pet_ID: ", get_pet_response["id"]))

    def test_can_update_pet(self):
        add_pet_request = BaseFunctions.create_new_pet(self)
        assert add_pet_request.status_code == 200

        add_pet_response = add_pet_request.json()
        print("Create Pet Status: ", add_pet_request.status_code)
