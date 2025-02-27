"""
Service session wrapper for aiobotocore.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar, Unpack

from aiobotocore.session import ClientCreatorContext
from botocore.model import ServiceModel

from boto34.boto3.type_defs import ClientKwargs
from boto34.kwargs_cache import KwargsCache

if TYPE_CHECKING:
    from boto34.aiobotocore.session import Session

_Client = TypeVar("_Client")


class ServiceFactory(Generic[_Client]):
    """
    Service session wrapper for aiobotocore.
    """

    SERVICE_NAME: str = ""
    _SERVICE_PROP: str = "service"

    def __init__(self, session: Session) -> None:
        self._session = session
        self._client_cache = KwargsCache[ClientCreatorContext[_Client]]()

    def _create_client(
        self, **kwargs: Unpack[ClientKwargs]
    ) -> ClientCreatorContext[_Client]:
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        cached_client = self._client_cache.get(filtered_kwargs)
        if cached_client:
            return cached_client
        client = self._session.client(
            service_name=self.SERVICE_NAME,
            **filtered_kwargs,
        )
        self._client_cache.set(filtered_kwargs, client)
        return client

    async def get_service_model(  # type: ignore[override]
        self, service_name: str | None = None, api_version: Any | None = None
    ) -> ServiceModel:
        return await self._session.get_service_model(self.SERVICE_NAME, api_version)

    async def get_service_data(
        self, service_name: str | None = None, api_version: Any | None = None
    ) -> dict[str, Any]:
        return await self._session.get_service_data(self.SERVICE_NAME, api_version)

    async def get_available_regions(
        self,
        service_name: str | None = None,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> list[str]:
        return self._session.get_available_regions(
            service_name=self.SERVICE_NAME,
            partition_name=partition_name,
            allow_non_regional=allow_non_regional,
        )

    def clear_cache(self) -> None:
        """
        Clear the client cache.
        """
        self._client_cache.clear()
