from pydantic import BaseModel, Field


class Pagination(BaseModel):
    page: int = Field(description="номер страницы", default=None)
    size: int = Field(description="количество объектов", default=None)