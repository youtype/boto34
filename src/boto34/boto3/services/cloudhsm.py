"""
Wrapper for boto3 CloudHSM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudhsm/)

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
    # Returns type annotated boto3 CloudHSM client
    cloudhsm_client = session.cloudhsm.client()
    cloudhsm_client: types_boto3_cloudhsm.client.CloudHSMClient
    ```
"""

from __future__ import annotations

from types_boto3_cloudhsm.client import CloudHSMClient

from boto34.boto3.service_factory import ServiceFactory


class CloudHSMService(ServiceFactory[CloudHSMClient]):
    SERVICE_NAME = "cloudhsm"
    _SERVICE_PROP = "cloudhsm"
