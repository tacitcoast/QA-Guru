
import pytest

from models.providers import CsvUserProvider, DatabaseUserProvider, ApiUserProvider, UserProvider
from models.users import User, Status, Worker


# -------------------------------------------------------------------
# Используем объектный подход работы с данными
# -------------------------------------------------------------------

@pytest.fixture(params=[CsvUserProvider, DatabaseUserProvider, ApiUserProvider])
def provider(request) -> UserProvider:
    return request.param()


@pytest.fixture
def users(provider) -> list[User]:
    return provider.get_users()


@pytest.fixture
def workers(users) -> list[Worker]:
    """
    Берем только работников из списка пользователей
    """
    return [Worker(
        name=user.name,
        age=user.age,
        items=user.items
    ) for user in users if user.status == Status.worker]


def test_workers_are_adults_v3(workers):
    for worker in workers:
        assert worker.is_adult(), f"Работник {worker.name} несовершеннолетний"
