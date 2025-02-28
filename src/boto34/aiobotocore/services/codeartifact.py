"""
Wrapper for aiobotocore CodeArtifact service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codeartifact.client import CodeArtifactClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeArtifactService(ServiceFactory[CodeArtifactClient]):
    """
    CodeArtifact service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/)
    """
