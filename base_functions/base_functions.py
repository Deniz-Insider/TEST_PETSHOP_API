import requests
import uuid

ENDPOINT = "https://petstore.swagger.io/v2/"
class BaseFunctions():

    def generate_pet_payload(self):
        pet_name = "pet_{}".format(uuid.uuid4().hex)
        photo_url = "photo_{}.com".format(uuid.uuid4().hex)
        return {
            "name": pet_name,
            "photoUrls": [
                photo_url
            ],

            "status": "available"
        }

    def create_new_pet(self):
        return requests.put(ENDPOINT + "pet", json=self.generate_pet_payload())

    def update_pet(self):
        create_pet = self.create_new_pet()
        create_pet_response = create_pet.json()
        pet_id = create_pet_response["id"]

        get_created_pet = requests.put(ENDPOINT + "pet/" + pet_id)
        get_pet_response = get_created_pet.json()




        # task_response = self.create_new_pet()
        # task_id = task_response.json()["task"]["task_id"]
        # user_id = task_response.json()["task"]["user_id"]
        #
        # new_payload = {"content": "updated content",
        #                "is_done": True}
