from fastapi import APIRouter, Security, Depends
from fastapi.responses import RedirectResponse
from helper.base_kirimwa import KirimWA
from fastapi.security.api_key import APIKey
from fastapi.encoders import jsonable_encoder
import json


from app.config import config
from dependency.checker import check_key, get_api_key
from models.message_model import SendMessageModels


kirim_wa = KirimWA()

router = APIRouter()

@router.get("/qr-code", tags=["Get QR Code"])
async def get_qr_code(
  device_id: str
):
  """
  Setelah Membuat device_id, login melalui qr code berikut, copy link qr code untuk melakukan scan
  """
  get_qr_code = await kirim_wa.access_api("get", "/qr", 
    params={
      "device_id": device_id
    }
  )

  return { 
    "image_url": get_qr_code.get("image_url")
  }


@router.get("/devices/{device_id}", tags=["Check Device"])
async def get_device_details_by_id(
  device_id: str,
):
  check_devices = await kirim_wa.access_api("get", f"/devices/{device_id}")
  return check_devices


@router.delete("/devices/{device_id}", tags=["Check Device"])
async def delete_device_id(
  device_id: str
):
  delete_devices = await kirim_wa.access_api("delete", "/devices{device_id}")
  return delete_devices


@router.post("/message", tags=["Send Message"])
async def send_whatsapp_message(
  data: SendMessageModels
):

  payloads = jsonable_encoder(data)

  send_message = await kirim_wa.access_api("post", "/messages", payload=json.dumps(payloads))

  return send_message
