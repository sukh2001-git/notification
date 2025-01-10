import frappe
from frappe.email.doctype.notification.notification import trigger_daily_alerts
from datetime import datetime, timedelta

def process_notification():
    try:
        notifications = frappe.get_all(
            "Notification",
            filters={
                "enabled": 1,
                "delay_enabled": 1,
                "notification_triggered": 0
            },
            fields=["name", "delay_time", "custom_select_time"]
        )
        
        current_time = frappe.utils.now()
        formatted_current_time = frappe.utils.format_time(current_time, 'HH:mm:ss')
        
        for notification in notifications:
            doc = frappe.get_doc("Notification", notification.name)
            
            if doc.custom_select_time:
                
                delay_time_str = f"{doc.custom_select_time}:00"
                
                # Parse the times into datetime objects
                try:
                    configured_time = datetime.strptime(delay_time_str, '%H:%M:%S').time()
                    current_datetime = datetime.strptime(formatted_current_time, '%H:%M:%S').time()
                    
                    # Convert times to minutes since midnight for comparison
                    configured_minutes = configured_time.hour * 60 + configured_time.minute
                    current_minutes = current_datetime.hour * 60 + current_datetime.minute
                    
                    # Calculate time difference in minutes
                    time_diff = abs(current_minutes - configured_minutes)
                    
                    frappe.log_error(f"Configured time: {configured_time}", "Debug")
                    frappe.log_error(f"Current time: {current_datetime}", "Debug")
                    frappe.log_error(f"Time difference: {time_diff} minutes", "Debug")
                    
                    if time_diff <= 5 or current_minutes > configured_minutes:
                        frappe.log_error("Time condition met - triggering notification", "Debug")
                        trigger_daily_alerts()
                        
                        doc.notification_triggered = 1
                        doc.save()
                    else:
                        frappe.log_error(
                            f"Time mismatch - configured: {delay_time_str}, current: {formatted_current_time}, diff: {time_diff} minutes",
                            "Notification Error"
                        )
                except ValueError as ve:
                    frappe.log_error(f"Time parsing error: {str(ve)}", "Notification Error")
            else:
                frappe.log_error("Delay time not configured or delay_enabled is False", "Notification Warning")

    except Exception as e:
        frappe.log_error(f"Process Notification Error: {str(e)}", "Process Notification Error")
        
        
        
def reset_notification_triggers():
    try:
        notifications = frappe.get_all(
            "Notification",
            filters={
                "enabled": 1,
                "delay_enabled": 1,
                "notification_triggered": 1
            }
        )
        
        for notification in notifications:
            doc = frappe.get_doc("Notification", notification.name)
            doc.notification_triggered = 0
            doc.save()
            
        frappe.db.commit()
        frappe.log_error("Reset notification triggers successfully", "Notification Reset")
    
    except Exception as e:
        frappe.log_error(f"Reset Notification Error: {str(e)}", "Reset Notification Error")
        