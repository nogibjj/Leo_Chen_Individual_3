from locust import HttpUser, task, between
from locust import LoadTestShape


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # think time 1-2s
    connection_timeout = 2  # connection timeout 2s
    network_timeout = 3    # network timeout 3s

    @task
    def health_check(self):
        with self.client.get(
            "/analysis/health",
            catch_response=True,
            timeout=5.0,
            verify=False  # if https, can disable certificate verification to improve performance
        ) as response:
            if response.status_code != 200:
                response.failure(
                    f"Failed with status code: {response.status_code}")
            else:
                response.success()

    def on_start(self):
        # initialize operations when user starts
        pass


class StagesShape(LoadTestShape):
    stages = [
        # stage 1: reach 2500 users in 30s
        {"duration": 30, "users": 2500, "spawn_rate": 85},
        # stage 2: reach 5000 users in 60s
        {"duration": 60, "users": 5000, "spawn_rate": 85},
        # stage 3: reach 7500 users in 90s
        {"duration": 90, "users": 7500, "spawn_rate": 85},
        # stage 4: reach 10000 users in 120s
        {"duration": 120, "users": 10000, "spawn_rate": 85},
        # stage 5: maintain 10000 users for 60s
        {"duration": 180, "users": 10000, "spawn_rate": 85}
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                return stage["users"], stage["spawn_rate"]
        return None
