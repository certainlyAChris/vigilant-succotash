import logging

logger = logging.getLogger(name="logger")

logging.basicConfig(filename="myapp.log", datefmt=r'%m/%d/%Y %H:%M:%S'+' |>',format=' %(levelname)s %(asctime)s %(message)s', level = logging.DEBUG)

logger.critical("hello 7")