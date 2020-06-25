import logging


def _set_up_logger():
    # Log to console with a simple formatter; used by CLI
    formatter = logging.Formatter("%(message)s")
    handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    module_logger = logging.getLogger("local")
    module_logger.addHandler(handler)
    module_logger.setLevel(level=logging.DEBUG)

    return module_logger
