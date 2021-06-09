# containing all the configurable

from datetime import datetime
import uuid


# Fetch JSON data from this endpoint
JSON_ENDPOINT = "https://jsonplaceholder.typicode.com/photos"


#  Filename generation based on below requirement:
#  filename format: "photos_YYYY-MM-DD_uuid4"
#  example: "photos_2021-05-04_16fd2706-8baf-433b-82eb-8c7fada847da.tsv.gz"

FILE_NAME="photo_"+datetime.today().strftime('%Y-%m-%d')+"_"+str(uuid.uuid4())+".tsv"

# AWS configuration
aws_settinigs = {
    "ACCESS_KEY_ID": "AKIAY6P2JYSB27K4EN2Y",
    "SECRET_ACCESS_KEY": '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',
    "BUCKET_NAME": "amit-s3-bucket2"
}

file_name= "photo_2021-06-01_6e73932a-7bfc-4dae-9daa-6e6ad240c490.tsv.gz"

logging = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s %(name)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "formatter": "standard",
            "class": "logging.StreamHandler"
        },
        'file': {
            'backupCount': 10,
            'level': 'INFO',
            'maxBytes': 1048576,
            'encoding': 'utf-8',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "_".join(["api_to_aws", ".log"])
        },

    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True
        },

        "requests": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": True
        }
    }
}
