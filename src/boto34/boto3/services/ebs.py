"""
Wrapper for boto3 EBS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ebs/)

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
    # Returns type annotated boto3 EBS client
    ebs_client = session.ebs.client()
    ebs_client: types_boto3_ebs.client.EBSClient
    ```
"""

from __future__ import annotations

from types_boto3_ebs.client import EBSClient

from boto34.boto3.service_factory import ServiceFactory


class EBSService(ServiceFactory[EBSClient]):
    SERVICE_NAME = "ebs"
    _SERVICE_PROP = "ebs"
