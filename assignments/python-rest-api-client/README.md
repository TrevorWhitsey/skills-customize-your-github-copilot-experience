# 📘 Assignment: Python REST API Client

## 🎯 Objective

Use Python's `requests` library to consume a REST API and work with its JSON response. Fetch a user record from JSONPlaceholder and display selected fields.

## 📝 Tasks

### 🛠️ Fetch JSON Data

#### Description
Complete `fetch_user()` in the starter code to request a user record from JSONPlaceholder and convert the response into Python data.

#### Requirements
Completed program should:

- Send a `GET` request to `https://jsonplaceholder.typicode.com/users/{user_id}`.
- Check for an unsuccessful HTTP response and return the response data as JSON.
- Use a request timeout so the program does not wait indefinitely.

### 🛠️ Display the User Details

#### Description
Complete `display_user()` to show useful information from the API response, and run the program to test the result.

#### Requirements
Completed program should:

- Display the user's name, username, and email address.
- Handle request errors by printing a clear message instead of a traceback.
- Install the dependency and run the program with:

  ```bash
  python -m pip install requests
  python starter-code.py
  ```