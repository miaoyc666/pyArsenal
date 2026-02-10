#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pytest configuration for network module tests
Ensures proper module path resolution
"""

import sys
import os

# Add network directory to path first to avoid conflicts
# This ensures we import from the network module, not the parent datetime module
network_dir = os.path.dirname(os.path.abspath(__file__))
if network_dir not in sys.path:
    sys.path.insert(0, network_dir)

