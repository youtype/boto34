"""
Wrapper for boto3 ECRPublic service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ecr_public/)

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
    # Returns type annotated boto3 ECRPublic client
    ecr_public_client = session.ecr_public.client()
    ecr_public_client: types_boto3_ecr_public.client.ECRPublicClient
    ```
"""

from __future__ import annotations

from types_boto3_ecr_public.client import ECRPublicClient

from boto34.boto3.service_factory import ServiceFactory


class ECRPublicService(ServiceFactory[ECRPublicClient]):
    SERVICE_NAME = "ecr-public"
    _SERVICE_PROP = "ecr_public"
