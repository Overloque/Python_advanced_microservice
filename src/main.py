import random
from datetime import datetime, timezone
from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI()
user_id = 2


@app.post("/api/login", status_code=HTTPStatus.OK)
def login():
    return {
        "token": "QpwL5tke4Pnpja7X4"
    }


@app.post("/api/users", status_code=HTTPStatus.CREATED)
def create_user(user_data: dict):
    return {
        "name": user_data.get("name"),
        "job": user_data.get("job"),
        "id": "984",
        "createdAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    }


@app.put(f"/api/users/{user_id}", status_code=HTTPStatus.OK)
def update_user():
    return {
        "name": "morpheus",
        "job": "zion resident",
        "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    }


@app.delete(f"/api/users/{user_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_user():
    return HTTPStatus.NO_CONTENT


@app.get(f"/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user():
    return {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
            "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
        }
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
