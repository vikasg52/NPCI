from locust import User, task, between


class MyUser(User):
    wait_time = between(1, 2)
    host = "http://localhost:7000/employees"

    @task
    def login_test(self):
        print("I am login in")
