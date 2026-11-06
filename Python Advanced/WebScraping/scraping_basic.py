# دریافت محتوای یک وب سایت

import requests


# ارسال درخواست
response = requests.get(
    "https://example.com"
)

# نمایش کد HTML
print(
    response.text
)
