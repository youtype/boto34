"""
Wrapper for boto3 CloudControlApi service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudcontrol/)

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
    # Returns type annotated boto3 CloudControlApi client
    cloudcontrol_client = session.cloudcontrol.client()
    cloudcontrol_client: types_boto3_cloudcontrol.client.CloudControlApiClient
    ```
"""

from __future__ import annotations

from types_boto3_cloudcontrol.client import CloudControlApiClient

from boto34.boto3.service_factory import ServiceFactory


class CloudControlApiService(ServiceFactory[CloudControlApiClient]):
    SERVICE_NAME = "cloudcontrol"
    _SERVICE_PROP = "cloudcontrol"
