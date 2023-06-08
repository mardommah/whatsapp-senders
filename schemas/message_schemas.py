from pydantic import BaseModel
from enum import Enum
from typing import List


class MessageTypeEnum(Enum):
  text = "text"
  image = "image"



class SendMessageModels(BaseModel):
  phone_number: str
  device_id: str
  message_type: MessageTypeEnum
  message: str


class UserInfoBase(BaseModel):
    username: str


class UserCreate(UserInfoBase):
    full_name: str
    password: str


class UserAuthenticate(UserInfoBase):
    password: str


class UserInfo(UserInfoBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None
