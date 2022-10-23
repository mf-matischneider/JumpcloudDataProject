import pandas as pd

user_col_list = [
    "id",
    "state",
    "displayname",
    "manager",
    "department",
    "jobTitle",
    "email",
    "employeeType",
]

users = pd.DataFrame()
devices = pd.DataFrame()
contractors = pd.DataFrame()


# sets options for pandas formatting
def set_options():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)


# Loads users based on user csv and column list
def load_users(columns):
    print("Loading data...")
    df = pd.read_csv("oct_jc_users.csv", usecols=columns)
    return df


def load_devices(columns):
    print("Loading data...")
    df = pd.read_csv("oct_jc_devices.csv", usecols=columns)
    return df


# Get all user ids
def get_all_user_ids():
    return load_users(user_col_list)["id"]


def get_contractors(df):
    contractors_list = df[df["employeeType"] == "Contractor"].loc[:, "id"]
    return contractors_list


def get_fte_employees(df):
    fte_employees = df[df["employeeType"] == "FTE"]
    return fte_employees


# Display users with no manager
def get_users_with_no_manager(df):
    users_with_no_manager = df[df["manager"].isnull()]
    return users_with_no_manager


def get_suspended_users(users):
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
    return devices[devices["hostname"] == hostname]


def get_device_user_metrics(hostname):
    return get_device_by_hostname(hostname)["userMetrics"]


set_options()

users = load_users(["id", "displayname", "manager", "employeeType", "state"])
devices = load_devices(["id", "hostname", "os", "userMetrics"])
contractors = get_contractors(users)
fte_employees = get_fte_employees(users)
users_with_no_manager = get_users_with_no_manager(users)


users = load_users(columns=user_col_list)
print(users["state"].value_counts())
print(users["department"].value_counts())







# if user_info['state'].values == 'SUSPENDED' and user_info['employeeType'].values == 'Contractor' and user_info['manager'].values != 'None':
