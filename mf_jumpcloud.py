import pandas as pd




# sets options for pandas formatting
def set_options():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)



# Loads users based on user csv and column list
def load_users():
    user_cols = ["id",
                 "state",
                 "displayname",
                 "manager",
                 "department",
                 "jobTitle",
                 "email",
                 "employeeType"]
    print("Loading data...")
    users = pd.read_csv("oct_jc_users.csv", usecols=user_cols)
    return users

# Loads devices based on device csv and column list
def load_devices(columns):
    print("Loading data...")
    devices = pd.read_csv("oct_jc_devices.csv", usecols=columns)
    return devices


# Get all user ids
def get_all_user_ids():
    return users[users['id']]

# Get All Contractors
def get_contractors():
    contractors_list = users[users["employeeType"] == "Contractor"].loc[:, "id"]
    return contractors_list

# Get All FTE Employees
def get_fte_employees():
    fte_employees = users[users["employeeType"] == "FTE"]
    return fte_employees


# Display users with no manager
def get_users_with_no_manager():
    users_with_no_manager = users[users["manager"].isnull()]
    return users_with_no_manager


def get_suspended_users():
    suspended_users = users[users["state"] == "SUSPENDED"]
    return suspended_users


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
        "company",
    ]
    df = df[cols]
    return df.loc[df["id"] == user_id]


def get_device_by_id(device_id):
    devices = load_devices(["id", "hostname", "userMetrics"])
    return devices.loc[devices["id"] == device_id]


def get_device_by_hostname(hostname):
    pass


def get_device_user_metrics(hostname):
    return get_device_by_hostname(hostname)["userMetrics"]


set_options()
users = load_users()
devices = load_devices(["id", "hostname", "userMetrics"])

# Displays all managers and their direct reports that are suspended
def get_suspended_users_with_managers():
    suspended_users = get_suspended_users()
    for suspended_user in suspended_users["id"]:
        suspended_user = get_user_by_id(suspended_user)
        suspended_user_manager_id = suspended_user["manager"].values[0]
        print(suspended_user_manager_id)
        if suspended_user_manager_id is not None:
            suspended_user_manager = get_user_by_id(suspended_user_manager_id)
            print(f'Suspended User: {suspended_user["displayname"].values[0]} Employee Type: - Manager: {suspended_user_manager["displayname"].values[0]}')
        else:
            print(f'Suspended User: {suspended_user["displayname"].values[0]} - Manager: None')


def get_suspended_users_without_managers():
    suspended_users = get_suspended_users()
    for suspended_user in suspended_users["id"]:
        suspended_user = get_user_by_id(suspended_user)
        if suspended_user["manager"].isnull().values[0]:
            print(f'Suspended User: {suspended_user["displayname"].values[0]} - Manager: None')