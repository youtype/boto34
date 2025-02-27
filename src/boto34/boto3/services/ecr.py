"""
Wrapper for boto3 ECR service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ecr/)

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
    # Returns type annotated boto3 ECR client
    ecr_client = session.ecr.client()
    ecr_client: types_boto3_ecr.client.ECRClient
    ```
"""

from __future__ import annotations

from types_boto3_ecr.client import ECRClient

from boto34.boto3.service_factory import ServiceFactory


class ECRService(ServiceFactory[ECRClient]):
    SERVICE_NAME = "ecr"
    _SERVICE_PROP = "ecr"
