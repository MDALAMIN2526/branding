# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = '0.0.1'

if frappe.conf and frappe.conf.get("app_logo_url"):
    __logo__ = frappe.conf.get("app_logo_url") or '/assets/branding/images/branding_logo.png'
else:
    __logo__ = '/assets/branding/images/branding_logo.png'