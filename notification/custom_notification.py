import frappe
from frappe.email.doctype.notification.notification import trigger_daily_alerts

def process_notification():
    try:
        notifications = frappe.get_all(
            "Notification",
            filters={
                "enabled": 1,
                "delay_enabled": 1
            },
            fields=["name", "delay_time"]
        )
        
        current_time = frappe.utils.now()
        formatted_current_time = frappe.utils.format_time(current_time, 'HH:mm:ss')
        
        for notification in notifications:
            doc = frappe.get_doc("Notification", notification.name)

        if doc.delay_time:
            # Format the delay_time
            # time_hh_mm = frappe.utils.format_time(doc.delay_time, 'HH:mm')
            # frappe.log_error(f"Formatted time_hh_mm: {time_hh_mm}", "Notification Debug")

            # if doc.time_hh_mm != time_hh_mm:
            #     frappe.log_error("i am hereee")
            #     frappe.db.set_value('Notification', doc.name, 'time_hh_mm', time_hh_mm)
            #     frappe.db.commit()

            if doc.delay_time == formatted_current_time:
                frappe.log_error("time matched")
                frappe.log_error("trigger_daily_alerts is called", trigger_daily_alerts())
            else:
                frappe.log_error(
                    f"Time mismatch - configured: {doc.delay_time}, current: {formatted_current_time}",
                    "Notification Error"
                )
        else:
            frappe.log_error("Delay time not configured or delay_enabled is False", "Notification Warning")

    except Exception as e:
        frappe.log_error(f"Process Notification Error: {str(e)}", "Process Notification Error")