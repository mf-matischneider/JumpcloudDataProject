import os

import pandas as pd
import schedule
import mf_jumpcloud as jc


if __name__ == "__main__":
    jc.set_options()
    users = jc.load_users()
    devices = jc.load_devices(columns=["id", "hostname", "os", "userMetrics"])
    contractors = jc.get_contractors()
    fte_employees = jc.get_fte_employees()
    users_with_no_manager = jc.get_users_with_no_manager()
    suspended_users = jc.get_suspended_users()
    print(f'Users with no manager: {len(users_with_no_manager)}')
    print(f"Suspended users: {len(suspended_users)}")
    print(f"Contractors: {len(contractors)}")
    print(f"FTE Employees: {len(fte_employees)}")
    print(f"All users: {len(users)}")
    print(f"All devices: {len(devices)}")
    print(f"Devices with no user metrics: {len(devices[devices['userMetrics'].isnull()])}")


    # schedule.every().day.at("00:00").do(jc.get_all_user_ids)
    # schedule.every().day.at("00:00").do(jc.get_all_device_ids)
    # schedule.every().day.at("00:00").do(jc.get_contractors)
    # schedule.every().day.at("00:00").do(jc.get_fte_employees)
    # schedule.every().day.at("00:00").do(jc.get_users_with_no_manager)
    # schedule.every().day.at("00:00").do(jc.get_suspended_users)
    # schedule.every().day.at("00:00").do(jc.get_all_users)
    # schedule.every().day.at("00:00").do(jc.get_all_devices)
    # schedule.every().day.at("00:00").do(jc.get_device_user_metrics)
    # schedule.every().day.at("00:00").do(jc.get_device_by_hostname)
    # schedule.every().day.at("00:00").do(jc.get_device_by_id)
    # schedule.every().day.at("00:00").do(jc.get_user_by_id)
    # schedule.every().day.at("00:00").do(jc.get_all_user_ids)
    # schedule.every().day.at("00:00").do(jc.get_all_device_ids)
    # schedule.every().day.at("00:00").do(jc.get_contractors)
    # schedule.every().day.at("00:00").do(jc.get_fte_employees)
    # schedule.every().










