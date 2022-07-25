from locust import FastHttpUser, task, between


class MyUser(FastHttpUser):
    wait_time = between(1, 2)
    host = "http://20.204.37.128:8081"

    @task
    def get_user_by_id(self):
        resp = self.client.get("/aadhar/8092ba57-b825-45b3-8c23-7aa6f0428d48", name="getUser")
        print("Response status", resp.status_code)
