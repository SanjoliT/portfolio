from locust import HttpUser, task, between

class EventsUser(HttpUser):
    # 1️⃣ Base host (MANDATORY)
    host = "http://127.0.0.1:8000"

    # 2️⃣ Small think-time → better avg latency
    wait_time = between(0.5, 1)

    def on_start(self):
        """
        3️⃣ Warm-up request
        Reduces cold-start latency → lowers average response time
        """
        self.client.get("/")

    @task
    def view_events(self):
        """
        4️⃣ Name the request for cleaner stats
        """
        with self.client.get(
            "/events",
            params={"user": "locust_user"},
            name="/events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed with {response.status_code}")
