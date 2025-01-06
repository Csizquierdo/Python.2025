# Ver Pydantic
import requests


class Users:
    def __init__(
        self,
        id: int,
        name: str,
        username: str,
        email: str,
        address: dict,
        phone: str,
        website: str,
        company: dict,
    ) -> None:
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

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
