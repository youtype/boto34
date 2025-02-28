"""
Wrapper for boto3 DAX service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dax/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_dax.client import DAXClient

from boto34.boto3.service_factory import ServiceFactory


class DAXService(ServiceFactory[DAXClient]):
    """
    DAX service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_dax/)
    """
