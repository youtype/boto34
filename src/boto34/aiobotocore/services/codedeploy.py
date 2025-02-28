"""
Wrapper for aiobotocore CodeDeploy service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codedeploy/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codedeploy.client import CodeDeployClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeDeployService(ServiceFactory[CodeDeployClient]):
    """
    CodeDeploy service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codedeploy/)
    """
