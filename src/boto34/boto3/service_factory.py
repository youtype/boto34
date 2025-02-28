"""
Factory for creating boto3 clients and resources.

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from botocore.client import BaseClient
from botocore.config import Config

from boto34.exceptions import Boto34Error

try:
    from boto3.resources.base import ServiceResource
except ImportError as e:
    raise Boto34Error("boto3 is not installed. Install `boto34[boto3]`") from e

if TYPE_CHECKING:
    from boto34.boto3.session import Session

_Client = TypeVar("_Client", bound=BaseClient)
_ServiceResource = TypeVar("_ServiceResource", bound=ServiceResource)


class ServiceFactory(Generic[_Client]):
    """
    Service session wrapper for boto3.

    Attributes:
        service_name: botocore service name
        session: Underlying boto3.Session
    """

    def __init__(self, service_name: str, session: Session) -> None:
        self.service_name = service_name
        self.session = session

    def client(
        self,
        service_name: str | None = None,
        region_name: str | None = None,
        api_version: str | None = None,
        use_ssl: bool | None = None,
        verify: bool | str | None = None,
        endpoint_url: str | None = None,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        aws_session_token: str | None = None,
        config: Config | None = None,
    ) -> _Client:
        """
        Proxy method to boto3.session.Session.client.

        Arguments are the same, but service_name is ignored.
        """
        result: _Client = self.session.client(
            service_name=self.service_name,
            region_name=region_name,
            api_version=api_version,
            use_ssl=use_ssl,
            verify=verify,
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            config=config,
        )
        return result

    def get_available_regions(
        self,
        service_name: str | None = None,
        partition_name: str = "aws",
        allow_non_regional: bool = False,
    ) -> list[str]:
        """
        Proxy method to boto3.session.Session.get_available_regions.

        Arguments are the same, but service_name is ignored.
        """
        return self.session.get_available_regions(
            service_name=self.service_name,
            partition_name=partition_name,
            allow_non_regional=allow_non_regional,
        )


class ServiceResourceFactory(
    ServiceFactory[_Client],
    Generic[_Client, _ServiceResource],
):
    def resource(
        self,
        service_name: str | None = None,
        region_name: str | None = None,
        api_version: str | None = None,
        use_ssl: bool | None = None,
        verify: bool | str | None = None,
        endpoint_url: str | None = None,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        aws_session_token: str | None = None,
        config: Config | None = None,
    ) -> _ServiceResource:
        """
        Proxy method to boto3.session.Session.resource.

        Arguments are the same, but service_name is ignored.
        """
        result: _ServiceResource = self.session.resource(
            service_name=self.service_name,
            region_name=region_name,
            api_version=api_version,
            use_ssl=use_ssl,
            verify=verify,
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            config=config,
        )
        return result
