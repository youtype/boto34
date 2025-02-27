"""
Wrapper for boto3 CloudSearchDomain service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudsearchdomain/)

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
    # Returns type annotated boto3 CloudSearchDomain client
    cloudsearchdomain_client = session.cloudsearchdomain.client()
    cloudsearchdomain_client: types_boto3_cloudsearchdomain.client.CloudSearchDomainClient
    ```
"""

from __future__ import annotations

from types_boto3_cloudsearchdomain.client import CloudSearchDomainClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_cloudsearchdomain.client import CloudSearchDomainClient
except ImportError:
    CloudSearchDomainClient = object  # type: ignore[misc,assignment]


class CloudSearchDomainService(
    ServiceFactory[CloudSearchDomainClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudsearchdomain"
    _SERVICE_PROP = "cloudsearchdomain"
