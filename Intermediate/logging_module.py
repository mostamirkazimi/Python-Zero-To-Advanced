import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("برنامه اجرا شد")

logging.warning("یک هشدار")

logging.error("یک خطا")

print("لاگ ثبت شد")