from locust import FastHttpUser, task, between


class MyUser(FastHttpUser):
    wait_time = between(1, 2)
    host = "https://demo.guru99.com"

    @task
    def launch_url(self):
        resp = self.client.get("/test/newtours", name="launchsite")
        print(resp.text)
        print(resp.status_code)
        print(resp.headers)

    @task
    def login_test(self):
        resp1 = self.client.post("/test/newtours/login.php", name="login",
                                data={"action": "process", "userName": "vikas", "password": "master123",
                                      "login.x": "41",
                                      "login.y": "12"
                                      })
        print(resp1.text)
        print(resp1.status_code)
        print(resp1.headers)
