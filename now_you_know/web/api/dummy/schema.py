from typing import Optional

from pydantic import BaseModel


class DummyModelDTO(BaseModel):
    """
    DTO for dummy models.

    It returned when accessing dummy models from the API.
    """

    id: int
    name: str
    year: Optional[int] = ...

    class Config:
        orm_mode = True


class DummyModelInputDTO(BaseModel):
    """DTO for creating new dummy model."""

    name: str
    year: int
