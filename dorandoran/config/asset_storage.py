from storages.backends.s3boto3 import S3Boto3Storage


class ImageStorage(S3Boto3Storage):
    location = "image"
    file_overwrite = False
