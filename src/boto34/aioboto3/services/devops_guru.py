"""
Wrapper for aioboto3 DevOpsGuru service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_devops_guru/)

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
    # Returns type annotated aioboto3 DevOpsGuru client
    devops_guru_client = session.devops_guru.client()
    devops_guru_client: types_aiobotocore_devops_guru.client.DevOpsGuruClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_devops_guru.client import DevOpsGuruClient
except ImportError:
    DevOpsGuruClient = object  # type: ignore[misc,assignment]


class DevOpsGuruService(
    ServiceFactory[DevOpsGuruClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "devops-guru"
    _SERVICE_PROP = "devops_guru"
