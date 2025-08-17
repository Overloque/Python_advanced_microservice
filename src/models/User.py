from pydantic import BaseModel, EmailStr, HttpUrl, Field


class User(BaseModel):
    id: int = Field(description="айдишник пользователя")
    email: EmailStr = Field(description="почта пользователя")
    first_name: str = Field(description="имя пользователя")
    last_name: str = Field(description="фамилия пользователя")
    avatar: HttpUrl = Field(description="ссылка на аватарку пользователя")
