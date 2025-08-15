import os
import pytest
from dotenv import load_dotenv

from src.helpers.my_app_helper import MyAppHelper

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def my_app_helper(base_url) -> MyAppHelper:
    return MyAppHelper(base_url)
