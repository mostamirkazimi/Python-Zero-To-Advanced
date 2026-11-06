# سیستم ثبت رویدادها
import logging


# تنظیمات لاگ
logging.basicConfig(

    filename="app.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

# ثبت پیام اطلاعاتی
logging.info(
    "برنامه اجرا شد"
)

# ثبت هشدار
logging.warning(
    "هشدار سیستم"
)

# ثبت خطا
logging.error(
    "خطای سیستم"
)