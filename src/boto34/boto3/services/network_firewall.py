"""
Wrapper for boto3 NetworkFirewall service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_network_firewall/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_network_firewall.client import NetworkFirewallClient

from boto34.boto3.service_factory import ServiceFactory


class NetworkFirewallService(ServiceFactory[NetworkFirewallClient]):
    """
    NetworkFirewall service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_network_firewall/)
    """
