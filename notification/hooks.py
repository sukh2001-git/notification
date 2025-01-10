app_name = "notification"
app_title = "Notification"
app_publisher = "sukh@onehash.ai"
app_description = "notification related operations"
app_email = "sukh@onehash.ai"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "notification",
# 		"logo": "/assets/notification/logo.png",
# 		"title": "Notification",
# 		"route": "/notification",
# 		"has_permission": "notification.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/notification/css/notification.css"
app_include_js = "/assets/notification/js/notification.js"

# include js, css files in header of web template
# web_include_css = "/assets/notification/css/notification.css"
# web_include_js = "/assets/notification/js/notification.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "notification/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "notification/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "notification.utils.jinja_methods",
# 	"filters": "notification.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "notification.install.before_install"
# after_install = "notification.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "notification.uninstall.before_uninstall"
# after_uninstall = "notification.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "notification.utils.before_app_install"
# after_app_install = "notification.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "notification.utils.before_app_uninstall"
# after_app_uninstall = "notification.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "notification.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",  
# 		"on_trash": "method"
# 	}
# }

# doc_events = {
#     "Notification": {
#         "on_update": "notification.custom_notification.on_save",
#         "trigger_notifications": "notification.custom_notification.override_trigger_notifications"
#     }
# }

# scheduler_events = {
#     "cron": {
#         "* * * * *": [
#             "notification.custom_notification.process_notification"
#         ]
#     }
# }

scheduler_events = {
    "hourly": [
            "notification.custom_notification.process_notification"
        ],
    "daily": [
            "notification.custom_notification.reset_notification_triggers"
        ]
}

# scheduler_events = {
#     "cron": {
#         "0 * * * *": [  # Run at the start of every hour
#             "notification.custom_notification.trigger_daily_alerts"
#         ]
#     }
# }


# override_doctype_class = {
#     "Notification": "notification.custom_notification.CustomNotification"
# }

# from frappe.email.doctype.notification.notification import trigger_daily_alerts
# from notification.custom_notification import trigger_daily_alerts as custom_trigger_daily_alerts

# # Monkey-patch the method
# trigger_daily_alerts = custom_trigger_daily_alerts

# hooks.py
# override_methods = {
#     "frappe.email.doctype.notification.notification.trigger_daily_alerts": "notification.custom_notification.trigger_daily_alerts"
# }


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"notification.tasks.all"
# 	],
# 	"daily": [
# 		"notification.tasks.daily"
# 	],
# 	"hourly": [
# 		"notification.tasks.hourly"
# 	],
# 	"weekly": [
# 		"notification.tasks.weekly"
# 	],
# 	"monthly": [
# 		"notification.tasks.monthly"
# 	],
#     "daily_long": [
#         "notification.notification.notification.CustomNotification.process_scheduled_notifications"
#     ]
# }

# Testing
# -------

# before_tests = "notification.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "notification.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "notification.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["notification.utils.before_request"]
# after_request = ["notification.utils.after_request"]

# Job Events
# ----------
# before_job = ["notification.utils.before_job"]
# after_job = ["notification.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"notification.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

