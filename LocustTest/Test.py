from locust import FastHttpUser, task, between


class ServiceTest(FastHttpUser):
    wait_time = between(0, 1)
    # host = "https://api.openbrewerydb.org"
    host = "http://localhost:7000"

    @task
    def get_call(self):
        self.client.get("/employees")
