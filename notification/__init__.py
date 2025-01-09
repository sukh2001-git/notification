__version__ = "0.0.1"


from notification.custom_notification import process_notification

# Override the method
import frappe.email.doctype.notification.notification
frappe.email.doctype.notification.notification.trigger_daily_alerts = process_notification



