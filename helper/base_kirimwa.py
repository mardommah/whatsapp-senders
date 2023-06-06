import requests
from app.config import config
from fastapi import HTTPException, status

cls_requests = {
  "get": requests.get,
  "post": requests.post,
  "put": requests.put,
  "delete": requests.delete,
  "patch": requests.patch,
}


class KirimWA:
  def __init__(self):
    self.api_key = config.api_key_kirim_wa
    self.url = "https://api.kirimwa.id/v1"
    self.headers = {
      "Content-Type": "application/json",
    }

  async def access_api(
    self,
    method: str,
    url: str,
    params: dict = None,
    payload: dict = None,
    headers: dict = None
  ) -> dict:
    headers = headers or self.headers
    url = self.url + url
    headers["Authorization"] = "Bearer " + self.api_key

    print(payload)

    try:
      request = cls_requests[method](
          url, headers=headers, data=payload, params=params
      )
      response_result = request.json()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    if request.status_code not in (200, 201):
        raise HTTPException(
            status_code=request.status_code,
            detail=response_result.get("errors") or response_result.get("error"),
        )
    return response_result