"""
Wrapper for boto3 WAF service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_waf/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_waf.client import WAFClient

from boto34.boto3.service_factory import ServiceFactory


class WAFService(ServiceFactory[WAFClient]):
    """
    WAF service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_waf/)
    """
