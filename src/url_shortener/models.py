from datetime import UTC, datetime
from uuid import UUID, uuid7

from sqlmodel import Field, Relationship, SQLModel


class Url(SQLModel, table=True):
    __tablename__ = "urls"

    short_url: str = Field(primary_key=True)
    long_url: str = Field(index=True)

    creation_time: datetime = Field(
        index=True, default_factory=lambda: datetime.now(UTC)
    )
    expiration_time: datetime | None = Field(default=None)

    user_id: UUID = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="urls")


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid7, primary_key=True)

    urls: list[Url] = Relationship(back_populates="user")
