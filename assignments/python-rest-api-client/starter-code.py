import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_user(user_id: int) -> dict:
    """Fetch one user record from the API."""
    raise NotImplementedError("Complete the API request")


def display_user(user: dict) -> None:
    """Print the selected fields from a user record."""
    raise NotImplementedError("Display the user's name, username, and email")


def main() -> None:
    user_id = 1

    try:
        user = fetch_user(user_id)
        display_user(user)
    except requests.RequestException as error:
        print(f"Could not fetch user: {error}")


if __name__ == "__main__":
    main()