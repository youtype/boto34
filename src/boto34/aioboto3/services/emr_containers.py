"""
Wrapper for aioboto3 EMRContainers service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_emr_containers/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 EMRContainers client
    emr_containers_client = session.emr_containers.client()
    emr_containers_client: types_aiobotocore_emr_containers.client.EMRContainersClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_emr_containers.client import EMRContainersClient

from boto34.aioboto3.service_factory import ServiceFactory


class EMRContainersService(ServiceFactory[EMRContainersClient]):
    SERVICE_NAME = "emr-containers"
    _SERVICE_PROP = "emr_containers"
