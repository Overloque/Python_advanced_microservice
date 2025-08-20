import json

import uvicorn

from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from fastapi_pagination import add_pagination, Page, paginate

from src.data.constants import create_user_data
from src.models.AppStatus import AppStatus
from src.models.User import User

app = FastAPI()
add_pagination(app)
users: list[User] = []


@app.get("/status", status_code=HTTPStatus.OK)
def status():
    return AppStatus(users=bool(users))


@app.get("/", status_code=HTTPStatus.OK)
def get_users() -> Page[User]:
    return paginate(users)


@app.post("/api/login", status_code=HTTPStatus.OK)
def login():
    return {
        "token": "QpwL5tke4Pnpja7X4"
    }


@app.post("/api/users", status_code=HTTPStatus.CREATED)
def create_user():
    return create_user_data


@app.put("/api/users/{user_id}", status_code=HTTPStatus.OK)
def update_user(user_id: int):
    users[user_id - 1]["first_name"] = "updated_first_name"
    return users[user_id - 1]


@app.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int):
    if user_id > len(users) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return users[user_id - 1]


@app.on_event("startup")
def load_users():
    global users
    with open("users.json", "r") as f:
        raw_users = json.load(f)
    users = [User(**user) for user in raw_users]

