"""
Wrapper for aioboto3 LaunchWizard service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_launch_wizard/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_launch_wizard.client import LaunchWizardClient

from boto34.aioboto3.service_factory import ServiceFactory


class LaunchWizardService(ServiceFactory[LaunchWizardClient]):
    """
    LaunchWizard service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_launch_wizard/)
    """
