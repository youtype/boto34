from boto3.session import Session as _Session

from boto34.boto3.services.s3 import S3Service


class Session(_Session):
    @property
    def s3(self) -> S3Service:
        return S3Service(self)
