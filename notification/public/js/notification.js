frappe.ui.form.on('Notification', {

    refresh: function (frm) {
        if (cur_frm.doc.delay_enabled === 1) {

            frm.add_custom_button(
                __("Schedule Notification"),
                () => {
                    schedule_send_dialog(frm);
                },
                __("Send")
            );
        }
    },
});


function schedule_send_dialog(frm) {
    let hours = frappe.utils.range(24);
    let time_slots = hours.map((hour) => {
        return `${(hour + "").padStart(2, "0")}:00`;
    });
    let d = new frappe.ui.Dialog({
        title: __("Schedule Notification"),
        fields: [
            {
                label: __("Time"),
                fieldname: "time",
                fieldtype: "Select",
                options: time_slots,
                reqd: true,
            },
        ],
        primary_action_label: __("Schedule"),
        primary_action(values) {
            if (!values.time) {
                frappe.throw(__("Please select a time"));
                return;
            }

            const delay_time = `${values.time}:00`;

            frm.set_value("delay_time", delay_time);
            d.hide();
            frm.save();

            frappe.msgprint(__('Notification scheduled successfully'));
        },
    });

    d.show();
}