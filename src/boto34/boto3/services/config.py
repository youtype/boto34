"""
Wrapper for boto3 ConfigService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_config/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ConfigService client
    config_client = session.config.client()
    config_client: types_boto3_config.client.ConfigServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_config.client import ConfigServiceClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_config.client import ConfigServiceClient
except ImportError:
    ConfigServiceClient = object  # type: ignore[misc,assignment]


class ConfigServiceService(
    ServiceFactory[ConfigServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "config"
    _SERVICE_PROP = "config"
