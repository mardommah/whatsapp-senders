from pydantic import BaseModel
from enum import Enum


class MessageTypeEnum(Enum):
  text = "text"
  image = "image"



class SendMessageModels(BaseModel):
  phone_number: str
  device_id: str
  message_type: MessageTypeEnum
  message: str