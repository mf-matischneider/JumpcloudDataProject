import pandas as pd


# Get jc users by user id
def get_user_by_id(user_id):
    df = pd.read_json("oct_jc_users.json")
    cols = [
        "id",
        "state",
        "displayname",
        "manager",
        "department",
        "jobTitle",
        "email",
        "employeeType",
    ]
    df = df[cols]
    return df[df["id"] == user_id].to_dict("records")[0]


# Get manager by manager id
def get_manager_by_id(user_id):
    df = pd.read_json("oct_jc_users.json")
    cols = [
        "id",
        "displayname",
        "manager",
        "department",
        "jobTitle",
        "email",
        "employeeType",
    ]
    df = df[cols]
    return df[df["id"] == user_id].to_dict("records")[0]["manager"]



def get_all_devices_ids():
    df = pd.read_json("oct_jc_devices.json")
    cols = [
        "id"
    ]
    df = df[cols]
    return df

def get_device_by_id(device_id):
    for device in get_all_devices_ids():
       get_all_devices_ids().loc[device_id]


def get_contractors():
    df = pd.read_json("oct_jc_users.json")
    cols = [
        "id",
        "state",
        "displayname",
        "manager",
        "department",
        "jobTitle",
        "email",
        "employeeType",
    ]
    df = df[cols]
    contractors_list = df[df["employeeType"] == "Contractor"]["id"]
    return contractors_list


def get_suspended_contractors():
    suspended_contractors = pd.DataFrame()
    for contractor in get_contractors():
        contractor_info = get_user_by_id(contractor)
        if contractor_info["state"] == "suspended":
            suspended_contractors.push(contractor_info)
    return suspended_contractors


def get_all_users():
    df = pd.read_json("oct_jc_users.json")
    cols = [
        "id",
        "state",
        "displayname",
        "manager",
        "department",
        "jobTitle",
        "email",
        "employeeType",
    ]
    df = df[cols]
    users_list = df["id"]
    return users_list


def get_suspended_users():
    suspended_users = pd.DataFrame()
    for suspended_user in get_all_users():
        suspended_user_info = get_user_by_id(suspended_user)
        if suspended_user_info["state"] == "suspended":
            suspended_users.push(suspended_user_info)
    return suspended_users



def main():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)




if __name__ == "__main__":
    for device_id in get_all_devices_ids():
        print(get_device_by_id(device_id))



