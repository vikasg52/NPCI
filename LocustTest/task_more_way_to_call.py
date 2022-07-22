from locust import User, task, between


def login_test(userclass):
    print("I am login test")


def logout_test(userclass):
    print("I am logout test")


class MyUser(User):
    wait_time = between(1, 2)

    # tasks = [login_test, logout_test]
    tasks = {login_test: 2, logout_test: 4}
