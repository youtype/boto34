"""
Wrapper for boto3 ElasticLoadBalancingv2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elbv2/)

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
    # Returns type annotated boto3 ElasticLoadBalancingv2 client
    elbv2_client = session.elbv2.client()
    elbv2_client: types_boto3_elbv2.client.ElasticLoadBalancingv2Client
    ```
"""

from __future__ import annotations

from types_boto3_elbv2.client import ElasticLoadBalancingv2Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_elbv2.client import ElasticLoadBalancingv2Client
except ImportError:
    ElasticLoadBalancingv2Client = object  # type: ignore[misc,assignment]


class ElasticLoadBalancingv2Service(
    ServiceFactory[ElasticLoadBalancingv2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elbv2"
    _SERVICE_PROP = "elbv2"
