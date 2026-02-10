#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
File name    : test_ip_address.py
Author       : miaoyc
Create date  : 2024/2/10
Description  : Pytest tests for IP address utilities
"""

import ipaddress

import pytest

from ip_address import get_server_ips, get_all_ips, should_exclude_ip


class TestServerIps:
    """Test cases for get_server_ips function"""

    def test_returns_list(self):
        """Test that get_server_ips returns a list"""
        result = get_server_ips()
        print(result)
        assert isinstance(result, list)

    def test_no_duplicates(self):
        """Test that returned IPs don't have duplicates"""
        ips = get_server_ips()
        assert len(ips) == len(set(ips))

    def test_valid_ip_format(self):
        """Test that returned IPs are in valid format"""
        ips = get_server_ips()
        for ip in ips:
            ipaddress.ip_address(ip)  # Should not raise ValueError

    def test_consistent_results(self):
        """Test that multiple calls return consistent results"""
        result1 = get_server_ips()
        result2 = get_server_ips()
        assert sorted(result1) == sorted(result2)


class TestAllIps:
    """Test cases for get_all_ips function"""

    def test_returns_dict(self):
        """Test that get_all_ips returns a dictionary"""
        result = get_all_ips()
        print(result)
        assert isinstance(result, dict)

    def test_has_required_keys(self):
        """Test that result contains required keys"""
        result = get_all_ips()
        assert 'valid_ips' in result
        assert 'excluded_ips' in result

    def test_keys_are_lists(self):
        """Test that both keys contain lists"""
        result = get_all_ips()
        assert isinstance(result['valid_ips'], list)
        assert isinstance(result['excluded_ips'], list)


class TestExcludeIp:
    """Test cases for IP filtering logic"""

    def test_exclude_loopback_ipv4(self):
        """Test that IPv4 loopback address is excluded"""
        ip = ipaddress.IPv4Address('127.0.0.1')
        assert should_exclude_ip(ip)

    def test_exclude_loopback_ipv6(self):
        """Test that IPv6 loopback address is excluded"""
        ip = ipaddress.IPv6Address('::1')
        assert should_exclude_ip(ip)

    def test_exclude_link_local(self):
        """Test that link-local addresses are excluded"""
        ip = ipaddress.IPv4Address('169.254.1.1')
        assert should_exclude_ip(ip)

    def test_exclude_docker_bridge(self):
        """Test that Docker default bridge addresses are excluded"""
        # Docker default bridge (172.17.0.0/16)
        ip1 = ipaddress.IPv4Address('172.17.0.1')
        assert should_exclude_ip(ip1)

        ip2 = ipaddress.IPv4Address('172.17.0.2')
        assert should_exclude_ip(ip2)

    @pytest.mark.parametrize("ip_str", [
        '127.0.0.1',      # IPv4 loopback
        '::1',            # IPv6 loopback
        '169.254.1.1',    # Link-local
        '172.17.0.1',     # Docker bridge
    ])
    def test_exclude_various_ips(self, ip_str):
        """Parametrized test for various excluded IPs"""
        ip = ipaddress.ip_address(ip_str)
        assert should_exclude_ip(ip)
