from tkinter import messagebox as mgbx
from CISCO.router.access_cisco_router.access_cisco_router_ssh import conn


# =============================ACL Standard Config functions Section================================
def acl_standard_permit_other_config(aclStandard_number_value):
    if aclStandard_number_value:
        conn.add_commands([f"access-list {aclStandard_number_value} permit any"])
    else:
        mgbx.showinfo("Error", "ACL group Number is required")


def acl_standard_deny_other_config(aclStandard_number_value):
    if aclStandard_number_value:
        conn.add_commands([f"access-list {aclStandard_number_value} deny any"])
    else:
        mgbx.showinfo("Error", "ACL group Number is required")


def acl_standard_define_config(aclStandard_number_value, aclStandard_action_value, aclStandard_host_value, aclStandard_WCM_value):
    if aclStandard_number_value and aclStandard_action_value and aclStandard_host_value and aclStandard_WCM_value:
        if 0 < int(aclStandard_number_value) < 100:
            if aclStandard_action_value in ("deny", "permit"):
                conn.add_commands([f"access-list {aclStandard_number_value} {aclStandard_action_value} {aclStandard_host_value} {aclStandard_WCM_value}"])
            else:
                mgbx.showinfo("Error", "Please select an option from the given in action field")
        else:
            mgbx.showinfo("Error", "Please select ACL Number from 1 to 99")
    else:
        mgbx.showinfo("Error", "Please all fields are required")


def acl_standard_apply_config(aclStandard_apply_interface_value, aclStandard_apply_accessgroup_value, aclStandard_apply_action_value):
    if aclStandard_apply_interface_value and aclStandard_apply_accessgroup_value and aclStandard_apply_action_value:
        if aclStandard_apply_action_value in ("inbound", "outbound"):
            aclStandard_apply_action_value = "in" if aclStandard_apply_action_value == "inbound" else "out"
            conn.add_commands([f"interface {aclStandard_apply_interface_value}", f"ip access-group {aclStandard_apply_accessgroup_value} {aclStandard_apply_action_value}"])
        else:
            mgbx.showinfo("Error", "Please select an option from the given in action field")
    else:
        mgbx.showinfo("Error", "Please all fields are required")


# =============================ACL Extended Config functions Section================================
