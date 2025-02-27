"""
Wrapper for boto3 EMRContainers service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_emr_containers/)

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
    # Returns type annotated boto3 EMRContainers client
    emr_containers_client = session.emr_containers.client()
    emr_containers_client: types_boto3_emr_containers.client.EMRContainersClient
    ```
"""

from __future__ import annotations

from types_boto3_emr_containers.client import EMRContainersClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_emr_containers.client import EMRContainersClient
except ImportError:
    EMRContainersClient = object  # type: ignore[misc,assignment]


class EMRContainersService(
    ServiceFactory[EMRContainersClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "emr-containers"
    _SERVICE_PROP = "emr_containers"
