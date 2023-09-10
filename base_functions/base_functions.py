import requests
import uuid

ENDPOINT = "https://petstore.swagger.io/v2/"
class BaseFunctions():

    def generate_payload(self):
        pet_name = "pet_" + uuid.uuid4().hex
        photo_url = "photo_{}.com".format(uuid.uuid4().hex)
        return {
            "name": pet_name,
            "photoUrls": [
                photo_url
            ],

            "status": "available"
        }

    def create_new_pet(self):
        return requests.put(ENDPOINT + "pet", json=self.generate_payload())

    def update_pet(self):
        #generate new payload and create a new pet
        #assert pet status
        #update pet status
        #assert updated status
        return requests.put(ENDPOINT + "pet", json=self.generate_payload())

        # task_response = self.create_new_pet()
        # task_id = task_response.json()["task"]["task_id"]
        # user_id = task_response.json()["task"]["user_id"]
        #
        # new_payload = {"content": "updated content",
        #                "is_done": True}
