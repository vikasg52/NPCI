from locust import between, task, User
from datetime import datetime


class WebsiteUserTest01(User):
    wait_time = between(1, 2)
    weight = 3
    @task
    def get_call(self):
        print("WebsiteUserTest01 user1")


class MobileUserTest(User):
    wait_time = between(1, 2)
    weight = 1
    @task
    def get_call(self):
        print("MobileUserTest user2")
