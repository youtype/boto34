"""
Wrapper for boto3 DevOpsGuru service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_devops_guru/)

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
    # Returns type annotated boto3 DevOpsGuru client
    devops_guru_client = session.devops_guru.client()
    devops_guru_client: types_boto3_devops_guru.client.DevOpsGuruClient
    ```
"""

from __future__ import annotations

from types_boto3_devops_guru.client import DevOpsGuruClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_devops_guru.client import DevOpsGuruClient
except ImportError:
    DevOpsGuruClient = object  # type: ignore[misc,assignment]


class DevOpsGuruService(
    ServiceFactory[DevOpsGuruClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "devops-guru"
    _SERVICE_PROP = "devops_guru"
