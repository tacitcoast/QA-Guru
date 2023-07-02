import enum

from dataclasses import dataclass


AGE_LIMIT = 18


class Status(enum.Enum):
    student = 'student'
    worker = 'worker'


@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list

    def is_adult(self) -> bool:
        return self.age >= AGE_LIMIT

    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items

    # def __repr__(self):
    #     return f"{self.status} {self.name} with age {self.age}"

    # def __eq__(self, other):
    #     return self.name == other.name and \
    #         self.age == other.age and \
    #         self.status == other.status and \
    #         self.items == other.items


class Worker(User):

    status = Status.worker

    def __init__(self, name, age, items):
        super().__init__(name=name, age=age, items=items, status=Status.worker)

    def do_work(self):
        pass


if __name__ == '__main__':
    oleg = User(name="Oleg", age=18, status=Status.student, items=[])
    oleg.items.append("pen")

    olga = User(name="Olga", age=21, status=Status.worker, items=[])
    olga.items.append("book")

    olga_from_csv = User(name="Olga", age=21, status=Status.worker, items=[])
    olga_from_db = User(name="Olga", age=21, status=Status.worker, items=[])

    assert olga_from_csv == olga_from_db

    sergey = Worker(name="Sergey", age=25, items=[])

    sergey.is_adult()
    sergey.do_work()
    print()
