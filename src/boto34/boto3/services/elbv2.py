"""
Wrapper for boto3 ElasticLoadBalancingv2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elbv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_elbv2.client import ElasticLoadBalancingv2Client

from boto34.boto3.service_factory import ServiceFactory


class ElasticLoadBalancingv2Service(ServiceFactory[ElasticLoadBalancingv2Client]):
    """
    ElasticLoadBalancingv2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elbv2/)
    """
