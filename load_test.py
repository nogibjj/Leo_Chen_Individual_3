from locust import HttpUser, task, between
from locust import LoadTestShape


class WebsiteUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def health_check(self):
        with self.client.get("/analysis/health", catch_response=True, timeout=5.0) as response:
            if response.status_code != 200:
                response.failure(
                    f"Failed with status code: {response.status_code}")
            else:
                response.success()


class StagesShape(LoadTestShape):
    stages = [
        {"duration": 30, "users": 2500, "spawn_rate": 85},    # 30秒内达到2500用户
        {"duration": 60, "users": 5000, "spawn_rate": 85},    # 60秒内达到5000用户
        {"duration": 90, "users": 7500, "spawn_rate": 85},    # 90秒内达到7500用户
        {"duration": 120, "users": 10000, "spawn_rate": 85}   # 120秒内达到10000用户
    ]

    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return stage["users"], stage["spawn_rate"]
        return None
