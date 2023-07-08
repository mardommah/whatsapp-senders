from pydantic import BaseModel


class DataModels(BaseModel):
  order_id: int
  product_name: str
  order_total: int
  payment_method: str
  first_name: str
  last_name: str
  address: str
  city: str
  post_code: str
  email: str
  phone: str
  date_created: str


class DataUsers(BaseModel):
  id_pembelian: str
  data: DataModels