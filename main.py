import pandas as pd


def get_user_by_id(user_id):
    df = pd.read_json('oct_jc_users.json')
    cols = ['id','state', 'displayname', 'manager', 'department', 'jobTitle', 'email', 'employeeType']
    df = df[cols]
    return df[df['id'] == user_id].to_dict('records')[0]

def get_manager_by_id(user_id):
    df = pd.read_json('oct_jc_users.json')
    cols = ['id', 'displayname', 'manager', 'department', 'jobTitle', 'email', 'employeeType']
    df = df[cols]
    return df[df['id'] == user_id].to_dict('records')[0]['manager']


def get_contractors():
    df = pd.read_json('oct_jc_users.json')
    cols = ['id', 'state', 'displayname', 'manager', 'department', 'jobTitle', 'email', 'employeeType']
    df = df[cols]
    contractors_list = df[df['employeeType'] == 'Contractor']['id'].tolist()
    return contractors_list

def main():

    for contractor in get_contractors():
        contractor_info = get_user_by_id(contractor)
        print(contractor_info)





if __name__ == '__main__':
    main()

