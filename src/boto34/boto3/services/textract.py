"""
Wrapper for boto3 Textract service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_textract/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_textract.client import TextractClient

from boto34.boto3.service_factory import ServiceFactory


class TextractService(ServiceFactory[TextractClient]):
    """
    Textract service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_textract/)
    """
