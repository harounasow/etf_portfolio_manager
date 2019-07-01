# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "etf_portfolio_manager"
app_title = "Etf Portfolio Manager"
app_publisher = "harounasow"
app_description = "App for managing ETF portfolios"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "harouna.sow@efrei.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/etf_portfolio_manager/css/etf_portfolio_manager.css"
# app_include_js = "/assets/etf_portfolio_manager/js/etf_portfolio_manager.js"

# include js, css files in header of web template
# web_include_css = "/assets/etf_portfolio_manager/css/etf_portfolio_manager.css"
# web_include_js = "/assets/etf_portfolio_manager/js/etf_portfolio_manager.js"

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
# get_website_user_home_page = "etf_portfolio_manager.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "etf_portfolio_manager.install.before_install"
# after_install = "etf_portfolio_manager.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "etf_portfolio_manager.notifications.get_notification_config"

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
# 		"etf_portfolio_manager.tasks.all"
# 	],
# 	"daily": [
# 		"etf_portfolio_manager.tasks.daily"
# 	],
# 	"hourly": [
# 		"etf_portfolio_manager.tasks.hourly"
# 	],
# 	"weekly": [
# 		"etf_portfolio_manager.tasks.weekly"
# 	]
# 	"monthly": [
# 		"etf_portfolio_manager.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "etf_portfolio_manager.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "etf_portfolio_manager.event.get_events"
# }

