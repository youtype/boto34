"""
Wrapper for boto3 WAFRegional service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_waf_regional/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_waf_regional.client import WAFRegionalClient

from boto34.boto3.service_factory import ServiceFactory


class WAFRegionalService(ServiceFactory[WAFRegionalClient]):
    """
    WAFRegional service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_waf_regional/)
    """
