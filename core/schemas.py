"""
All pydantic schemas from db and bot only
"""
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    """User pydantic schema

    Args:
        BaseModel (BaseModel): base pydantic model
    """
    user_id: int
    is_bot: bool
    first_name: str
    last_name: str | None
    username: str | None
    is_premium: bool


class Message(BaseModel):
    """Message pydantic model

    Args:
        BaseModel (BaseModel): base pydantic model
    """
    message_id: int
    date: datetime
    thread_id: int | None
    from_user: int
    forward_date: datetime | None
    reply_to_message: int | None
    edit_date: datetime | None
    media_group_id: int | None
    text: str | None
