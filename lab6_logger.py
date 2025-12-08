import logging
from functools import wraps

def logged(exception):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
            handler = logging.FileHandler("lab6_log.txt", encoding="utf-8")
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.handlers = []
            logger.addHandler(handler)

            try:
                result = func(self, *args, **kwargs)
                logger.info(f"Successfully executed: {func.__name__}")
                return result
            except exception as e:
                logger.error(f"Exception in {func.__name__}: {e}")
                raise
        return wrapper
    return decorator