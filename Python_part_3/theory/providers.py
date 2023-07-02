import csv

from models.users import User, Status


class UserProvider:

    def get_users(self) -> list[User]:
        raise NotImplementedError("Реализуйте эту функцию в конкретном провайдере")


class CsvUserProvider(UserProvider):

    def get_users(self) -> list[User]:
        with open("users.csv") as f:
            users = list(csv.DictReader(f, delimiter=";"))
        return [
            User(name=user["name"],
                 age=int(user["age"]),
                 status=Status(user["status"]),
                 items=user["items"].split(","))
            for user in users
        ]


class DatabaseUserProvider(UserProvider):
    pass


class ApiUserProvider(UserProvider):
    pass

