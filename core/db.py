"""
Core of project.
Models and db.

*!! NO MESSAGE LOGIC !!*

"""
import peewee_async as apeewee
import peewee

from aiogram import types

import config


db = apeewee.PostgresqlDatabase(
    database=config.DB_NAME,
    user=config.DB_USER_NAME,
    host=config.DB_HOST,
    port=config.DB_PORT,
    password=config.DB_PASSWORD
    )

AsyncManager = apeewee.Manager(db)

#  Im_Cocks-Net_321-BzF_g
class User(peewee.Model):
    """User class

    Args:
        peewee (Model): User model
    """

    user_id: peewee.IntegerField = peewee.IntegerField(
        index=True, unique=True, primary_key=True, column_name='user_id'
        )
    """Unique identifier for this user or bot.
    This number may have more than 32 significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52 significant bits,
    so a 64-bit integer or double-precision float type are safe for storing this identifier."""

    is_bot: peewee.BooleanField = peewee.BooleanField()
    """:code:`True`, if this user is a bot"""

    first_name: peewee.TextField = peewee.TextField()
    """User's or bot's first name"""

    last_name: peewee.TextField = peewee.TextField(null=True)
    """*Optional*. User's or bot's last name"""

    username: peewee.TextField = peewee.TextField(null=True)
    """*Optional*. User's or bot's username"""

    is_premium: peewee.BooleanField = peewee.BooleanField()
    """*Optional*. :code:`True`, if this user is a Telegram Premium user"""


    class Meta:
        """
        Meta info
        """
        database = db


class Message(peewee.Model):
    """Message class.
    Stores all data sended to chat

    Args:
        peewee (Model): peewee base model
    """

    message_id: peewee.IntegerField = peewee.IntegerField(
        index=True, unique=True, primary_key=True, column_name='message_id'
        )
    """Unique message identifier inside this chat"""

    date: peewee.DateTimeField = peewee.DateTimeField()
    """Date the message was sent in Unix time"""

    thread_id: peewee.IntegerField = peewee.IntegerField(null=True)
    """*Optional*. Unique identifier of a message thread to which the message belongs;
    for supergroups only"""

    from_user: peewee.ForeignKeyField = peewee.ForeignKeyField(
        model=User, field='user_id', null=True
        )
    """*Optional*. Sender of the message;
    empty for messages sent to channels. For backward compatibility,
    the field contains a fake sender user in non-channel chats,
    if the message was sent on behalf of a chat."""

    forward_date: peewee.DateTimeField = peewee.DateTimeField(null=True)
    """*Optional*. For forwarded messages, date the original message was sent in Unix time"""

    reply_to_message: peewee.ForeignKeyField = peewee.ForeignKeyField(
        model='self', field='message_id', null=True
        )
    """*Optional*. For replies, the original message. 
    Note that the Message object in this field will
    not contain further *reply_to_message* fields even if it itself is a reply."""

    edit_date: peewee.DateTimeField = peewee.DateTimeField(null=True)
    """*Optional*. Date the message was last edited in Unix time"""

    media_group_id: peewee.IntegerField = peewee.IntegerField(null=True)
    """*Optional*. The unique identifier of a media message group this message belongs to"""

    text: peewee.TextField = peewee.TextField()
    """*Optional*. For text messages, the actual UTF-8 text of the message"""

    # pinned_message: Optional[Message] = None
    # """*Optional*. Specified message was pinned. 
    # Note that the Message object in this field will not contain further *reply_to_message* 
    # fields even if it is itself a reply."""

    class Meta:
        """
        Meta info
        """
        database = db
    
    
    async def create_from_message(self, msg: types.Message)


def migrate() -> None:
    """Creates tables in db
    """
    Message.create_table(True)
    User.create_table(True)
