"""
Wrapper for boto3 Synthetics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_synthetics/)

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
    # Returns type annotated boto3 Synthetics client
    synthetics_client = session.synthetics.client()
    synthetics_client: types_boto3_synthetics.client.SyntheticsClient
    ```
"""

from __future__ import annotations

from types_boto3_synthetics.client import SyntheticsClient

from boto34.boto3.service_factory import ServiceFactory


class SyntheticsService(ServiceFactory[SyntheticsClient]):
    SERVICE_NAME = "synthetics"
    _SERVICE_PROP = "synthetics"
