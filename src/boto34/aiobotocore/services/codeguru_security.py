"""
Wrapper for aiobotocore CodeGuruSecurity service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguru_security/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codeguru_security.client import CodeGuruSecurityClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeGuruSecurityService(ServiceFactory[CodeGuruSecurityClient]):
    """
    CodeGuruSecurity service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguru_security/)
    """
