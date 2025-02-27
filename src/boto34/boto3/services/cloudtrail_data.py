"""
Wrapper for boto3 CloudTrailDataService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudtrail_data/)

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
    # Returns type annotated boto3 CloudTrailDataService client
    cloudtrail_data_client = session.cloudtrail_data.client()
    cloudtrail_data_client: types_boto3_cloudtrail_data.client.CloudTrailDataServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_cloudtrail_data.client import CloudTrailDataServiceClient

from boto34.boto3.service_factory import ServiceFactory


class CloudTrailDataServiceService(ServiceFactory[CloudTrailDataServiceClient]):
    SERVICE_NAME = "cloudtrail-data"
    _SERVICE_PROP = "cloudtrail_data"
