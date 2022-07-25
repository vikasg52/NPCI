from locust import User, task, between


class MyUser(User):
    wait_time = between(1, 2)
    host = "http://localhost:7000/employees"

    @task
    def login_test(self):
        print("I am login in")

    url = host
    print("The API is being hit at:", url)
    response = self
    response = self.client.post(
        url,
        name="LOGIN: Post API Call Status:",
        data=sodimac_utils.get_unique_login_data()
    )
