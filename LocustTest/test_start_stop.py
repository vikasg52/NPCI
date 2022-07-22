from locust import User, task, between, events


@events.test_start.add_listener
def script_start(**kwargs):
    print("I am starting the db")


@events.test_stop.add_listener
def script_stop(**kwargs):
    print("I am closing the db")


class MyUser(User):
    wait_time = between(1, 2)

    # host = "http://localhost:7000/employees"

    def on_start(self):
        print("I am login in")

    @task
    def login_test(self):
        print("I am working")

    def on_stop(self):
        print("I am doing logout")
