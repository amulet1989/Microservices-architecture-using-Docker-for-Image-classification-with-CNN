from locust import HttpUser, between, task


class APIUser(HttpUser):
    wait_time = between(1, 5)

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO

    # Check index endpoint GET
    @task
    def index_endpoint(self):
        response = self.client.get("/")

    # Check predict endpoint POST
    @task
    def predict_endpoint(self):
        headers = {}
        files = [("file", ("dog.jpeg", open("dog.jpeg", "rb"), "image/jpeg"))]
        self.client.post("/predict", files=files, headers=headers)
