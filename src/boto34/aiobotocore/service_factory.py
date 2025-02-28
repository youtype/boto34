"""
Service session wrapper for aiobotocore.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar

from botocore.model import ServiceModel
from typing_extensions import Unpack

from boto34.aiobotocore.type_defs import ClientKwargs
from boto34.exceptions import Boto34Error

try:
    from aiobotocore.client import AioBaseClient
    from aiobotocore.session import ClientCreatorContext
except ImportError as e:
    raise Boto34Error("aiobotocore is not installed. Install `boto34[aiobotocore]`") from e

if TYPE_CHECKING:
    from boto34.aiobotocore.session import Session

_Client = TypeVar("_Client", bound=AioBaseClient)


class ServiceFactory(Generic[_Client]):
    """
    Service session wrapper for aiobotocore.

    Attributes:
        service_name: botocore service name
        session: Underlying aiobotocore.Session
    """

    def __init__(self, service_name: str, session: Session) -> None:
        self.service_name = service_name
        self.session = session

    def create_client(
        self,
        service_name: str | None = None,
        **kwargs: Unpack[ClientKwargs],
    ) -> ClientCreatorContext[_Client]:
        """
        Proxy method to aiobotocore.session.Session.create_client.

        Arguments are the same, but service_name is ignored.
        """
        return self.session.create_client(service_name=self.service_name, **kwargs)

    async def get_service_model(
        self, service_name: str | None = None, api_version: str | None = None
    ) -> ServiceModel:
        """
        Proxy method to aiobotocore.session.Session.get_service_model.

        Arguments are the same, but service_name is ignored.
        """
        return await self.session.get_service_model(self.service_name, api_version)

    async def get_service_data(
        self, service_name: str | None = None, api_version: str | None = None
    ) -> dict[str, Any]:
        """
        Proxy method to aiobotocore.session.Session.get_service_data.

        Arguments are the same, but service_name is ignored.
        """
        return await self.session.get_service_data(self.service_name, api_version)

    async def get_available_regions(
        self,
        service_name: str | None = None,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> list[str]:
        """
        Proxy method to aiobotocore.session.Session.get_available_regions.

        Arguments are the same, but service_name is ignored.
        """
        return await self.session.get_available_regions(
            service_name=self.service_name,
            partition_name=partition_name,
            allow_non_regional=allow_non_regional,
        )
