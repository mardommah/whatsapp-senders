from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session

from dependency.access_token import decode_user_token
from schemas.data_pembeli import DataModels
from models.db_models import DataPembeli, Base
from helper import crud
from database.db import engine

router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.post("/add_data", tags=["Add Data Pembelian"])
async def get_datas(
  user_data: DataModels,
  access_token: str = Header(...,description="Access Token"),
  db: Session = Depends(crud.get_db),
):

  # check acess token
  check_access_token = decode_user_token(db, token=access_token)

  if check_access_token == "ok":
    pass
  else:
    raise HTTPException(status_code=400, detail="invalid token")

  
  # create input data
  data_user = DataPembeli(
    order_id = user_data.order_id,
    product_name = user_data.product_name,
    order_total = user_data.order_total,
    payment_method = user_data.payment_method,
    first_name = user_data.first_name,
    last_name = user_data.last_name,
    address = user_data.address,
    city = user_data.city,
    post_code = user_data.post_code,
    email = user_data.email,
    phone = user_data.phone,
    date_created = user_data.date_created
  )

  db.add(data_user)
  db.commit()
  db.refresh(data_user)

  return data_user
  