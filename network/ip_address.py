#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
File name    : ip_address.py
Author       : miaoyc
Create date  : 2024/2/10
Description  : Get server IP address utilities
"""

import ipaddress
import socket
import subprocess
from typing import List, Union


def get_server_ips() -> List[str]:
    """
    Get all server IP addresses from network interfaces.

    Excludes:
    - Loopback addresses (127.x.x.x, ::1)
    - Link-local addresses (169.254.x.x, fe80::)
    - Docker bridge addresses (172.17.x.x, 172.18.x.x, etc.)

    Returns:
        List[str]: List of valid server IP addresses. Returns empty list if no valid IPs found.

    Examples:
        >>> ips = get_server_ips()
        >>> print(ips)
        ['192.168.1.100', '10.0.0.50']
    """
    ips = []
    seen = set()

    try:
        # Use platform-specific commands to get network interfaces
        ips_raw = _get_ips_from_system()

        for ip in ips_raw:
            if ip not in seen:
                try:
                    ip_obj = ipaddress.ip_address(ip)
                    if not should_exclude_ip(ip_obj):
                        ips.append(ip)
                        seen.add(ip)
                except ValueError:
                    pass

    except Exception:
        pass

    return ips


def _get_ips_from_system() -> List[str]:
    """
    Get IPs from system commands (works on macOS and Linux).

    Returns:
        List[str]: List of IP addresses from system
    """
    ips = []

    try:
        import platform
        system = platform.system()

        if system == "Darwin":  # macOS
            # Use ifconfig to get network interfaces
            result = subprocess.run(["ifconfig"], capture_output=True, text=True, timeout=5)
            for line in result.stdout.split('\n'):
                line = line.strip()
                if line.startswith('inet ') and not line.startswith('inet6'):
                    parts = line.split()
                    if len(parts) >= 2:
                        ip = parts[1]
                        ips.append(ip)

        elif system == "Linux":
            # Use ip command on Linux
            result = subprocess.run(["ip", "addr"], capture_output=True, text=True, timeout=5)
            for line in result.stdout.split('\n'):
                line = line.strip()
                if line.startswith('inet ') and not line.startswith('inet6'):
                    parts = line.split()
                    if len(parts) >= 2:
                        ip = parts[1].split('/')[0]  # Remove subnet mask
                        ips.append(ip)

        else:
            # Fallback for other systems
            return _get_ips_from_socket()

    except (FileNotFoundError, subprocess.TimeoutExpired, Exception):
        # Fallback to socket method
        return _get_ips_from_socket()

    return ips


def _get_ips_from_socket() -> List[str]:
    """
    Fallback method using socket to get IPs.

    Returns:
        List[str]: List of IP addresses from socket
    """
    ips = []
    seen = set()

    try:
        # Get all addresses for the hostname
        hostname = socket.gethostname()

        # Try getaddrinfo first
        try:
            interfaces = socket.getaddrinfo(hostname, None, 0, 0, 0, 0)
            for family, socktype, proto, canonname, sockaddr in interfaces:
                ip = sockaddr[0]
                if ip not in seen:
                    ips.append(ip)
                    seen.add(ip)
        except (socket.error, OSError):
            pass

        # Try gethostbyname_ex as fallback
        if not ips:
            try:
                hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex(hostname)
                for ip in ipaddrlist:
                    if ip not in seen:
                        ips.append(ip)
                        seen.add(ip)
            except (socket.error, OSError):
                pass

    except Exception:
        pass

    return ips


def get_all_ips() -> dict:
    """
    Get all IP addresses with detailed information.

    Returns:
        dict: Contains 'valid_ips' and 'excluded_ips' lists

    Examples:
        >>> result = get_all_ips()
        >>> print(result)
        {
            'valid_ips': ['192.168.1.100', '10.0.0.50'],
            'excluded_ips': ['127.0.0.1', '::1', '172.17.0.1']
        }
    """
    valid_ips = []
    excluded_ips = []
    seen = set()

    try:
        # Use platform-specific commands to get network interfaces
        ips_raw = _get_ips_from_system()

        for ip in ips_raw:
            if ip not in seen:
                try:
                    ip_obj = ipaddress.ip_address(ip)
                    if should_exclude_ip(ip_obj):
                        excluded_ips.append(ip)
                    else:
                        valid_ips.append(ip)
                    seen.add(ip)
                except ValueError:
                    pass

    except Exception:
        pass

    return {
        'valid_ips': valid_ips,
        'excluded_ips': excluded_ips
    }


def should_exclude_ip(ip_obj: Union[ipaddress.IPv4Address, ipaddress.IPv6Address]) -> bool:
    """
    Check if an IP address should be excluded.

    Args:
        ip_obj: ipaddress.IPv4Address or ipaddress.IPv6Address object

    Returns:
        bool: True if IP should be excluded, False otherwise
    """
    # Exclude loopback addresses
    if ip_obj.is_loopback:
        return True

    # Exclude link-local addresses (169.254.x.x for IPv4, fe80::/10 for IPv6)
    if ip_obj.is_link_local:
        return True

    # Exclude multicast addresses
    if ip_obj.is_multicast:
        return True

    # For IPv4 only
    if isinstance(ip_obj, ipaddress.IPv4Address):
        # Exclude Docker bridge addresses (172.17.0.0 - 172.31.255.255)
        if _is_docker_bridge_ip(ip_obj):
            return True

    return False


def _is_docker_bridge_ip(ip_obj: ipaddress.IPv4Address) -> bool:
    """
    Check if IPv4 address is a Docker bridge address.

    Only filters the default Docker bridge (172.17.0.0/16) to avoid
    filtering valid private IPs in the 172.16.0.0/12 range.

    Args:
        ip_obj: ipaddress.IPv4Address object

    Returns:
        bool: True if it's a Docker bridge IP
    """
    # Docker default bridge: 172.17.0.0/16 only
    # We don't filter 172.18.x.x+ because those might be valid private IPs
    docker_bridge = ipaddress.IPv4Network('172.17.0.0/16')
    return ip_obj in docker_bridge


if __name__ == '__main__':
    # Test the module
    print("Valid Server IPs:")
    ips = get_server_ips()
    for ip in ips:
        print(f"  - {ip}")

    print("\nDetailed Information:")
    all_ips = get_all_ips()
    print(f"Valid IPs: {all_ips['valid_ips']}")
    print(f"Excluded IPs: {all_ips['excluded_ips']}")

