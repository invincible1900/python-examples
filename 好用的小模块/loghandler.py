# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
import logging
import logging.config
import os
import json

conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(asctime)s] %(filename)s:%(lineno)d %(funcName)s() %(levelname)s: %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },

        "debug_file_handler": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "DEBUG",
                    "formatter": "simple",
                    "filename": "log/debug.log",
                    "maxBytes": 10485760,
                    "backupCount": 20,
                    "encoding": "utf8"
        },

        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "log/info.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },

        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": "log/errors.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        }
    },

    "loggers": {
        "my_module": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": "no"
        }
    },

    "root": {
        "level": "INFO",
        "handlers": ["console", "debug_file_handler", "info_file_handler", "error_file_handler"]
    }
}

def setup_logging(default_path='logging.json', default_level=logging.DEBUG, env_key='LOG_CFG'):
    import os
    print(os.getcwd())
    """
    Setup logging configuration
    """
    if not os.path.exists('log'):
        os.mkdir('log')
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.config.dictConfig(conf)

    return logging.getLogger()


