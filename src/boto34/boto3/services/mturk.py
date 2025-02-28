"""
Wrapper for boto3 MTurk service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mturk/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_mturk.client import MTurkClient

from boto34.boto3.service_factory import ServiceFactory


class MTurkService(ServiceFactory[MTurkClient]):
    """
    MTurk service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_mturk/)
    """
