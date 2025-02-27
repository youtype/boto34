"""
Wrapper for boto3 RoboMaker service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_robomaker/)

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
    # Returns type annotated boto3 RoboMaker client
    robomaker_client = session.robomaker.client()
    robomaker_client: types_boto3_robomaker.client.RoboMakerClient
    ```
"""

from __future__ import annotations

from types_boto3_robomaker.client import RoboMakerClient

from boto34.boto3.service_factory import ServiceFactory


class RoboMakerService(ServiceFactory[RoboMakerClient]):
    SERVICE_NAME = "robomaker"
    _SERVICE_PROP = "robomaker"
