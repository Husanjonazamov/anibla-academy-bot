import requests
import json
from utils.env import BASE_URL


def createUser(user):
    url = f"{BASE_URL}/users/"

    response = requests.post(url, json=user)

    if response.status_code == 201:
        print("Foydalanuvchi muvaffaqiyatli yaratildi:", response.json())
    else:
        print("Xato:", response.status_code, response.text)

    return response.json()


def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return False  # yoki xato xabarini qaytarish


def changeName(user_id, name):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.put(url, data={'user_id': user_id, 'name': name})

    if response.status_code == 200:
        return response.json()

    return False


def changePhone(user_id, phone):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.put(url, data={'user_id': user_id, 'phone': phone})

    if response.status_code == 200:
        return response.json()

    return False


def get_lessons(user_id):
    """
    API orqali bazadagi barcha lessonslarni olib keladi.
    """
    url = f"{BASE_URL}/lessons?user_id={user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return False


def get_lesson_by_id(lesson_id):

    url = f"{BASE_URL}/lessons/{lesson_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return False


def post_homeworks(lesson_id, user_id, file_ids):
    url = f"{BASE_URL}/homework/"

    payload = json.dumps({
        "file_ids": file_ids,
        "lesson": lesson_id,
        "user": user_id
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()


def generate_payment(amount: int, user_id: int):
    url = f"{BASE_URL.replace('/api/v1', '')}/"

    payload = json.dumps(
        {
            "amount": amount,
            "is_paid": False,
            "user": user_id
        }
    )

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()
