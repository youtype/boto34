"""
Wrapper for aioboto3 Textract service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_textract/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_textract.client import TextractClient

from boto34.aioboto3.service_factory import ServiceFactory


class TextractService(ServiceFactory[TextractClient]):
    """
    Textract service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_textract/)
    """
