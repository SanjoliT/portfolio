from locust import HttpUser, task, between

class CheckoutUser(HttpUser):
    host = "http://127.0.0.1:8000"   # 👈 THIS LINE IS MANDATORY
    wait_time = between(1, 2)

    @task
    def test_checkout(self):
        self.client.get("/")
