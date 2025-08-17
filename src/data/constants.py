from datetime import datetime, timezone


class Constants:
    headers = {
        'x-api-key': 'reqres-free-v1'
    }


create_user_data = {
    "name": "morpheus",
    "job": "leader",
    "id": "984",
    "createdAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
}

update_user_data = {
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
}