"""
Wrapper for boto3 LaunchWizard service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_launch_wizard/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_launch_wizard.client import LaunchWizardClient

from boto34.boto3.service_factory import ServiceFactory


class LaunchWizardService(ServiceFactory[LaunchWizardClient]):
    """
    LaunchWizard service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_launch_wizard/)
    """
