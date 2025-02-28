"""
Wrapper for aiobotocore NetworkFirewall service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_network_firewall.client import NetworkFirewallClient

from boto34.aiobotocore.service_factory import ServiceFactory


class NetworkFirewallService(ServiceFactory[NetworkFirewallClient]):
    """
    NetworkFirewall service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_network_firewall/)
    """
