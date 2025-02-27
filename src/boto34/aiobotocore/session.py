from collections.abc import Mapping

from aiobotocore.session import AioSession as _Session

from boto34.aiobotocore.services.s3 import S3Service


class Session(_Session):
    @property
    def s3(self) -> S3Service:
        return S3Service(self)


def get_session(env_vars: Mapping[str, str] | None = None) -> Session:
    return Session(env_vars=env_vars)
