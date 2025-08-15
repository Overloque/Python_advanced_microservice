from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from src.data import users, create_user_data, update_user_data

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK)
def get_users():
    return users()


@app.post("/api/login", status_code=HTTPStatus.OK)
def login():
    return {
        "token": "QpwL5tke4Pnpja7X4"
    }


@app.post("/api/users", status_code=HTTPStatus.CREATED)
def create_user():
    return create_user_data


@app.put("/api/users/{user_id}", status_code=HTTPStatus.OK)
def update_user():
    return update_user_data


@app.delete("/api/users/{user_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_user():
    return HTTPStatus.NO_CONTENT


@app.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int):
    if user_id > len(users()) or user_id == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return users()[user_id - 1]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
