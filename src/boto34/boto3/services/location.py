"""
Wrapper for boto3 LocationService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_location/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_location.client import LocationServiceClient

from boto34.boto3.service_factory import ServiceFactory


class LocationServiceService(ServiceFactory[LocationServiceClient]):
    """
    LocationService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_location/)
    """
