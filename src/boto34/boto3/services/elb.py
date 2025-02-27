"""
Wrapper for boto3 ElasticLoadBalancing service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elb/)

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
    # Returns type annotated boto3 ElasticLoadBalancing client
    elb_client = session.elb.client()
    elb_client: types_boto3_elb.client.ElasticLoadBalancingClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_elb.client import ElasticLoadBalancingClient
except ImportError:
    ElasticLoadBalancingClient = object  # type: ignore[misc,assignment]


class ElasticLoadBalancingService(
    ServiceFactory[ElasticLoadBalancingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elb"
    _SERVICE_PROP = "elb"
