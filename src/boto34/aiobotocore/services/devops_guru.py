"""
Wrapper for aiobotocore DevOpsGuru service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_devops_guru/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore DevOpsGuru client
    async with session.devops_guru.create_client() as devops_guru_client:
        devops_guru_client: types_aiobotocore_devops_guru.client.DevOpsGuruClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_devops_guru.client import DevOpsGuruClient
except ImportError:
    DevOpsGuruClient = object  # type: ignore[misc,assignment]


class DevOpsGuruService(
    ServiceFactory[DevOpsGuruClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "devops-guru"
    _SERVICE_PROP = "devops_guru"
