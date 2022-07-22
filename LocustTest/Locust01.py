from locust import FastHttpUser, task, between, constant, constant_pacing
from datetime import datetime


class ServiceTest(FastHttpUser):
    # wait_time = between(1, 2)
    # wait_time = constant(2)
    wait_time = constant_pacing(5)
    host = "https://api.openbrewrydb.org"

    @task
    def get_call(self):
        print(datetime.now())
