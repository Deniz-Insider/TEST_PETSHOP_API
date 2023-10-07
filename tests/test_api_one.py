import requests
from base_functions.base_functions import BaseFunctions


class TestDemoApi(BaseFunctions):

    ENDPOINT = "https://petstore.swagger.io/v2/"

    def test_can_add_new_pet(self):
        add_pet_request = requests.post(self.ENDPOINT + "pet", json=BaseFunctions.generate_pet_payload(self))
        assert add_pet_request.status_code == 200

        add_pet_response = add_pet_request.json()
        # assert (add_pet_response.headers["Content-Type"] == "application/json; charset=utf-8",
        #         "Response does not match JSON format!")
        print("Status Code: ", add_pet_request.status_code)
        print(add_pet_response)


    def test_can_get_pet(self):
        add_pet_request = requests.post(self.ENDPOINT + "pet", json=BaseFunctions.generate_pet_payload(self))
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
        #create new pet
        add_pet_request = requests.post(self.ENDPOINT + "pet", json=BaseFunctions.generate_pet_payload(self))
        assert add_pet_request.status_code == 200
        add_pet_response = add_pet_request.json()
        pet_id = add_pet_response["id"]
        pet_status = add_pet_response["status"]
        print("Pet Status Before: ", pet_status)

        #update pet status
        new_payload = {
            "status": "sold"
        }
        update_pet_request = requests.post(self.ENDPOINT + "pet/{}".format(pet_id), json=new_payload)
        #update_pet_response = update_pet_request.json()

        #print("Pet Status After: ", update_pet_response["status"])
        get_pet_request = requests.get(self.ENDPOINT + "pet/{}".format(pet_id))
        get_pet_response = get_pet_request.json()
        print("Pet Status After: ", get_pet_response)
