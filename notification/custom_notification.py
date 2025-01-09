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
            fields=["name", "delay_time", "time_hh_mm"]
        )
        
        current_time = frappe.utils.now()
        formatted_current_time = frappe.utils.format_time(current_time, 'HH:mm')
        
        for notification in notifications:
            doc = frappe.get_doc("Notification", notification.name)

        if doc.delay_time:
            # Format the delay_time
            time_hh_mm = frappe.utils.format_time(doc.delay_time, 'HH:mm')
            frappe.log_error(f"Formatted time_hh_mm: {time_hh_mm}", "Notification Debug")

            if doc.time_hh_mm != time_hh_mm:
                frappe.log_error("i am hereee")
                frappe.db.set_value('Notification', doc.name, 'time_hh_mm', time_hh_mm)
                frappe.db.commit()

            if time_hh_mm == formatted_current_time:
                frappe.log_error("time matched")
                frappe.log_error("trigger_daily_alerts is called", trigger_daily_alerts())
            else:
                frappe.log_error(
                    f"Time mismatch - configured: {time_hh_mm}, current: {formatted_current_time}",
                    "Notification Error"
                )
        else:
            frappe.log_error("Delay time not configured or delay_enabled is False", "Notification Warning")

    except Exception as e:
        frappe.log_error(f"Process Notification Error: {str(e)}", "Process Notification Error")
        
        
        
        
        
        
        
        
        
        


# def trigger_daily_alerts():
#     """Trigger notifications at specific times"""
#     if frappe.flags.in_import or frappe.flags.in_patch:
#         return

#     current_time = frappe.utils.format_time(frappe.utils.now(), 'HH:mm')
    
#     notifications = frappe.get_all(
#         "Notification",
#         filters={
#             "enabled": 1,
#             "delay_enabled": 1,
#             "time_hh_mm": current_time
#         },
#         fields=["name"]
#     )
    
#     for notif in notifications:
#         doc = frappe.get_doc("Notification", notif.name)
#         trigger_notifications(doc, "custom_daily")

# def on_save(doc, method):
#     """Update `time_hh_mm` field when `delay_time` is saved"""
#     if doc.delay_time and doc.delay_enabled:
#         time_hh_mm = frappe.utils.format_time(doc.delay_time, 'HH:mm')
#         frappe.db.set_value('Notification', doc.name, 'time_hh_mm', time_hh_mm)
#         frappe.db.commit()






# import frappe
# from frappe.email.doctype.notification.notification import trigger_notifications
# from frappe.core.doctype.communication.email import make

# def override_trigger_notifications(doc=None, method=None, recipients=None):
#     if method == "custom_daily":
#         return trigger_notifications(doc, method, recipients)
#     if method == "daily":
#         return
#     return trigger_notifications(doc, method, recipients)

# def trigger_daily_alerts():
#     if frappe.flags.in_import or frappe.flags.in_patch:
#         return

#     current_time = frappe.utils.format_time(frappe.utils.now(), 'HH:mm')
    
#     notifications = frappe.get_all(
#         "Notification",
#         filters={
#             "enabled": 1,
#             "delay_enabled": 1,
#             "time_hh_mm": current_time
#         },
#         fields=["name", "channel", "subject", "message"]
#     )
    
#     for notif in notifications:
#         doc = frappe.get_doc("Notification", notif.name)
#         trigger_notifications(doc, "custom_daily")
        
#         if notif.channel == "Email":
#             make(
#                 subject=notif.subject,
#                 content=notif.message,
#                 recipients=notif.recipients,
#                 send_email=True,
#                 now=True
#             )

# def on_save(doc, method):
#     if doc.delay_time and doc.delay_enabled:
#         time_hh_mm = frappe.utils.format_time(doc.delay_time, 'HH:mm')
#         frappe.db.set_value('Notification', doc.name, 'time_hh_mm', time_hh_mm)
#         frappe.db.commit()




######################################################################
######################################################################

# import frappe
# import json
# # from frappe.email.doctype.notification.notification import evaluate_alert
# from frappe.core.doctype.communication.email import _make as make_communication
# from email.utils import formataddr
# # from frappe.desk.doctype.notification_log.notification_log import enqueue_create_notification
# # from frappe.core.doctype.sms_settings.sms_settings import send_sms
# # from frappe.integrations.doctype.slack_webhook_url.slack_webhook_url import send_slack_message

# def trigger_daily_alerts():
#     """Custom implementation of trigger_daily_alerts"""
#     print("Custom Trigger Daily Alerts")
#     trigger_notifications(None, "daily")
    
# def on_save(doc, method):
#     print("on save is triggered")
#     trigger_daily_alerts()

# def trigger_notifications(doc, method=None):
#     """Handle notification triggers based on delay_enabled for all channels"""
#     if frappe.flags.in_import or frappe.flags.in_patch:
#         return

#     if method == "daily":
#         doc_list = frappe.get_all(
#             "Notification",
#             filters={"enabled": 1},
#             fields=["name", "channel"]
#         )
        
#         current_time = frappe.utils.now()
#         formatted_current_time = frappe.utils.format_time(current_time, 'HH:mm')
#         # frappe.log_error("formatted_current_time", formatted_current_time)
        
#         for notification in doc_list:
#             try:
#                 alert = frappe.get_doc("Notification", notification.name)
#                 frappe.log_error("alert is", alert)
#                 frappe.log_error("process is ", process_notification(alert, formatted_current_time))
#             except Exception as e:
#                 frappe.log_error(
#                     f"Error processing notification {notification.name}: {str(e)}",
#                     "Notification Error"
#                 )
                
#         frappe.log_error("notification", notification)



            
            

# def send_notification(alert):
#     """Send notification based on channel type"""
#     try:
#         context = get_context(alert)
        
#         frappe.log_error("context", context)
#         frappe.log_error("alert channel", alert.channel)
        
#         if alert.channel == "Email":
#             frappe.log_error("send email notification", send_email_notification(alert, context))
            
        
#         # elif alert.channel == "Slack":
#         #     send_slack_notification(doc, alert, context)
        
#         # elif alert.channel == "System Notification":
#         #     send_system_notification(doc, alert, context)
        
#         # elif alert.channel == "SMS":
#         #     send_sms_notification(doc, alert, context)
        
#         # elif alert.channel == "WhatsApp":
#         #     send_whatsapp_notification(doc, alert, context)

#         frappe.db.commit()
#         log_success(alert)

#     except Exception as e:
#         log_error(alert, str(e))

# def get_context(alert):
#     """Build context for notification templates"""
#     context = {"alert": alert, "comments": None}
#     frappe.log_error("context", context)
#     # if doc.get("_comments"):
#     #     context["comments"] = json.loads(doc.get("_comments"))
#     return context

# def send_email_notification(alert, context):
#     """Send email notification"""
    
#     subject = frappe.render_template(alert.subject, context) if "{" in alert.subject else alert.subject
#     message = frappe.render_template(alert.message, context)
    
#     # frappe.log_error("subject is", subject)
#     # frappe.log_error("message is", message)
    
#     def parse_recipients(field):
#         if not field:
#             return []
#         if isinstance(field, list):
#             return field
#         return field.split('\n') if '\n' in field else [field]
    
#     # recipients, cc, bcc = alert.get_list_of_recipients(doc, context)
#     recipients = parse_recipients(alert.recipients)
#     # cc = parse_recipients(alert.cc)
#     # bcc = parse_recipients(alert.bcc)
    
#     frappe.log_error("recipients", recipients)
#     # frappe.log("cc", cc)
#     # frappe.log("bcc", bcc)
    

#     if not (recipients):
#         return
        
#     sender = None
#     if alert.sender and alert.sender_email:
#         sender = formataddr((alert.sender, alert.sender_email))
    
#     # attachments = alert.get_attachment(doc)
    
#     # Create communication record
#     if alert.document_type != "Communication":
#         frappe.log_error("Attempting to create communication record", "Notification Debug")
#         communication = make_communication(
#             # doctype=doc.doctype,
#             name=alert.name,
#             content=message,
#             subject=subject,
#             sender=sender,
#             recipients=recipients,
#             communication_medium="Email",
#             send_email=False,
#             # attachments=attachments,
#             # cc=cc,
#             # bcc=bcc,
#             communication_type="Automated Message",
#         )
    
#     frappe.sendmail(
#         recipients=recipients,
#         subject=subject,
#         sender=sender,
#         # cc=cc,
#         # bcc=bcc,
#         message=message,
#         # communication_type="Automated Message",
#         # reference_doctype=doc.doctype,
#         # reference_name=doc.name,
#         # attachments=attachments,
#         # expose_recipients="header",
#         # print_letterhead=((attachments and attachments[0].get("print_letterhead")) or False),
#         # communication=communication.get("name") if communication else None
#     )
    
    

# def send_slack_notification(doc, alert, context):
#     """Send Slack notification"""
#     message = frappe.render_template(alert.message, context)
#     send_slack_message(
#         webhook_url=alert.slack_webhook_url,
#         message=message,
#         reference_doctype=doc.doctype,
#         reference_name=doc.name
#     )

# def send_system_notification(doc, alert, context):
#     """Send system notification"""
#     subject = frappe.render_template(alert.subject, context) if "{" in alert.subject else alert.subject
#     message = frappe.render_template(alert.message, context)
    
#     recipients, cc, bcc = alert.get_list_of_recipients(doc, context)
#     users = list(set(recipients + cc + bcc))
    
#     if not users:
#         return
        
#     notification_doc = {
#         "type": "Alert",
#         "document_type": doc.doctype,
#         "document_name": doc.name,
#         "subject": subject,
#         "from_user": doc.modified_by or doc.owner,
#         "email_content": message,
#         "attached_file": alert.get_attachment(doc) and json.dumps(alert.get_attachment(doc)[0])
#     }
#     enqueue_create_notification(users, notification_doc)

# def send_sms_notification(doc, alert, context):
#     """Send SMS notification"""
#     message = frappe.render_template(alert.message, context)
#     receiver_list = alert.get_receiver_list(doc, context)
#     send_sms(receiver_list, message)

# def send_whatsapp_notification(doc, alert, context):
#     """Send WhatsApp notification - Implement based on your WhatsApp integration"""
#     # Example implementation - modify based on your WhatsApp provider
#     message = frappe.render_template(alert.message, context)
#     receiver_list = alert.get_receiver_list(doc, context)
    
#     # Replace with your WhatsApp sending logic
#     for receiver in receiver_list:
#         frappe.log_error(
#             f"WhatsApp message would be sent to {receiver}: {message}",
#             "WhatsApp Notification"
#         )

# def log_success(alert):
#     """Log successful notification"""
#     frappe.log_error(
#         f"{alert.channel} notification sent for document {alert.name} using notification {alert.name}",
#         f"{alert.channel} Success"
#     )

# def log_error(alert, error):
#     """Log notification error"""
#     frappe.log_error(
#         f"Failed to send {alert.channel} notification for document {alert.name}: {error}",
#         f"{alert.channel} Error"
#     )














##################################################################################################################################
##################################################################################################################################


# import frappe
# # from frappe.utils import now_datetime
# # from datetime import datetime
# from frappe.email.doctype.notification.notification import evaluate_alert

# def trigger_daily_alerts():
#     """Custom implementation of trigger_daily_alerts"""
#     print("Custom Trigger Daily Alerts")
#     trigger_notifications(None, "daily")
    
# def on_save(doc, method):
#     print("on save is triggered")
#     trigger_daily_alerts()

# def trigger_notifications(doc, method=None):
#     """Handle notification triggers based on delay_enabled"""
#     if frappe.flags.in_import or frappe.flags.in_patch:
#         # Don't send notifications during imports or patches
#         return

#     if method == "daily":
#         # Get all enabled notifications
#         doc_list = frappe.get_all(
#             "Notification",
#             filters={
#                 "enabled": 1
#             },
#             fields=["name", "channel"]
#         )
        
#         current_time = frappe.utils.now()
#         # Convert current_time to HH:mm format
#         formatted_current_time = frappe.utils.format_time(current_time, 'HH:mm')
#         frappe.log_error("formatted_current_time", formatted_current_time)
        
#         for d in doc_list:
#             try:
#                 alert = frappe.get_doc("Notification", d.name)
#                 frappe.log_error("alert.delay_time", alert.delay_time)
                
#                 if alert.delay_time and alert.delay_enabled:
#                     # Convert delay_time to HH:mm format
#                     time_hh_mm = frappe.utils.format_time(alert.delay_time, 'HH:mm')
                    
#                     if time_hh_mm:
#                         frappe.db.set_value('Notification', alert.name, 'time_hh_mm', time_hh_mm)
#                         frappe.db.commit()
                
#                 if alert.time_hh_mm == formatted_current_time:
#                     frappe.log_error(f"Triggering notification {alert.name} at {formatted_current_time}", "Debug")
#                     for doc in alert.get_documents_for_today():
#                         evaluate_alert(doc, alert, alert.event)
#                         frappe.db.commit()
                        
#             except Exception as e:
#                 frappe.log_error(f"Error processing notification {d.name}: {str(e)}", "Notification Error")
        
#         frappe.log_error("notification is", d)