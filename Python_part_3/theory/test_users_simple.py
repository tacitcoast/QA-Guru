
import csv

# -------------------------------------------------------------------
# Прямолинейный вариант теста
# -------------------------------------------------------------------


def test_workers_are_adults():
    """
    Тестируем, что все работники старше 18 лет
    """
    with open("users.csv") as f:
        users = csv.DictReader(f, delimiter=";")
        workers = [user for user in users if user["status"] == "worker"]
    for worker in workers:
        assert int(worker["age"]) >= 18, f"Работник {worker['name']} младше 18"


        # workers = []
        # for user in users:
        #     if user["status"] == "worker":
        #         workers.append(user)
