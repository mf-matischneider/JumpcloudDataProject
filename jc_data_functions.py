import pandas as pd

user_col_list = ['id', 'state', 'displayname', 'manager', 'department', 'jobTitle', 'email', 'employeeType']

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






def get_contractors(df):
    contractors_list = df[df["employeeType"] == "Contractor"].loc[:,'id']
    return contractors_list


def get_fte_employees(df):
    fte_employees_list = df[df["employeeType"] == "FTE"]
    return fte_employees_list


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
    ]
    df = df[cols]
    return df[df["id"] == user_id].to_dict("records")[0]


def get_device_by_id(device_id):
    return devices.loc[devices['id'] == device_id]

def get_device_by_hostname(hostname):
    return devices.loc[devices['hostname'] == hostname]

set_options()

users = load_users(['id', 'displayname', 'manager', 'employeeType', 'state'])
devices = load_devices(['id', 'hostname', 'os'])
contractors = get_contractors(users)
fte_employees = get_fte_employees(users)
users_with_no_manager = get_users_with_no_manager(users)
print(get_suspended_users(users))

