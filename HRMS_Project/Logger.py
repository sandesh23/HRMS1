import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('D://HRMS.log')
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
logger.addHandler(handler)
handler.setFormatter(formatter)
logger.info("Logger initialized")