from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    # 1️⃣ Mandatory base host (prevents StopTest + enables keep-alive)
    host = "http://127.0.0.1:8000"

    # 2️⃣ Lower think-time → smoother averages
    wait_time = between(0.5, 1)

    def on_start(self):
        """
        3️⃣ Warm-up request
        Eliminates cold-start latency from avg response time
        """
        self.client.get("/")

    @task
    def view_my_events(self):
        """
        4️⃣ Group requests (query params ignored in stats)
        """
        self.client.get(
            "/my-events",
            params={"user": "locust_user"},
            name="/my-events"
        )
