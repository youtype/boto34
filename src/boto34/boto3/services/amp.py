"""
Wrapper for boto3 PrometheusService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_amp/)

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
    # Returns type annotated boto3 PrometheusService client
    amp_client = session.amp.client()
    amp_client: types_boto3_amp.client.PrometheusServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_amp.client import PrometheusServiceClient

from boto34.boto3.service_factory import ServiceFactory


class PrometheusServiceService(ServiceFactory[PrometheusServiceClient]):
    SERVICE_NAME = "amp"
    _SERVICE_PROP = "amp"
