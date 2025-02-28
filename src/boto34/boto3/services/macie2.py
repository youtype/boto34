"""
Wrapper for boto3 Macie2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_macie2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_macie2.client import Macie2Client

from boto34.boto3.service_factory import ServiceFactory


class Macie2Service(ServiceFactory[Macie2Client]):
    """
    Macie2 service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_macie2/)
    """
