# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from . import __logo__ as app_logo


app_name = "branding"
app_title = "branding"
app_publisher = "Bhavesh Maheshwari"
app_description = "ERPNext branding"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "maheshwaribhavesh95863@gmail.com"
app_license = "MIT"
app_logo_url = '/assets/branding/images/branding_logo.png'

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/branding/css/branding_app.css"
app_include_js = "/assets/branding/js/branding.js"

# include js, css files in header of web template
web_include_css = "/assets/branding/css/branding_web.css"
# web_include_js = "/assets/branding/js/branding.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "branding.utils.get_home_page"

website_context = {
	"favicon": app_logo or "/assets/branding/images/branding_logo.png",
	"splash_image": app_logo or "/assets/branding/images/branding_logo.png"
}
after_migrate = ['branding.api.branding_patch']

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "branding.install.before_install"
# after_install = "branding.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "branding.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"branding.tasks.all"
# 	],
# 	"daily": [
# 		"branding.tasks.daily"
# 	],
# 	"hourly": [
# 		"branding.tasks.hourly"
# 	],
# 	"weekly": [
# 		"branding.tasks.weekly"
# 	]
# 	"monthly": [
# 		"branding.tasks.monthly"
# 	]
# }

boot_session = "branding.api.boot_session"
# Testing
# -------

# before_tests = "branding.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "branding.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "branding.task.get_dashboard_data"
# }

override_whitelisted_methods = {
	"frappe.utils.change_log.show_update_popup": "branding.api.ignore_update_popup"
}

