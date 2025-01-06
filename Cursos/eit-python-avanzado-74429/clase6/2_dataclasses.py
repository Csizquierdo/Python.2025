from dataclasses import dataclass

import requests


@dataclass
class Users:
    id: int
    name: str
    username: str
    email: str
    address: dict
    phone: str
    website: str
    company: dict

    def __post_init__(self) -> None:
        self.name = self.name.upper()

    def __str__(self) -> str:
        return f"{self.id}: {self.name} ({self.username})"


def get_users() -> list[Users]:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users: list[Users] = []

    if response.status_code == 200:
        users_data: list[dict] = response.json()
        for user in users_data:
            objeto_user = Users(**user)
            users.append(objeto_user)
    return users


if __name__ == "__main__":
    users = get_users()

    for user in users:
        print(user)
