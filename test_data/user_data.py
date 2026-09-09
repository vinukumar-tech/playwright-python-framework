import random
import string


# ADMIN USER TEST DATA

ADMIN_USER_DATA = {
    "name": "Vinukumar",
    "city": "Gulu",
    "country": "Uganda",
    "category": "Admin",
    "state": "Central Region",
    "authorisation_profile": "Authorisation ProfileAdmin",
    "security_profile": "SecurityProfileDemo"
}


# AGENT USER TEST DATA

def generate_agent_data():

    # RANDOM VALUES

    agent_code_alias = "".join(random.choices(string.digits, k=8))

    tin = "".join(random.choices(string.digits, k=10))

    float_account_number = "".join(random.choices(string.digits, k=11))

    commission_account_number = "".join(random.choices(string.digits, k=11))

    terminal_id = "".join(random.choices(string.digits, k=8))

    phone_number = "07" + "".join(random.choices(string.digits, k=8))

    email = "vinu" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@tecnotree.com"

    gps_coordinates = f"{random.uniform(-1.5, 1.5):.6f},{random.uniform(32.0, 34.5):.6f}"

    mtn_pos_simcard = "077" + "".join(random.choices(string.digits, k=7))

    airtel_pos_simcard = "075" + "".join(random.choices(string.digits, k=7))

    # AGENT DATA

    return {
        "workspace": "Agent",
        "category": "NormalAgent",
        "agent_code_alias": agent_code_alias,
        "tin": tin,
        "float_account_number": float_account_number,
        "business_name": "",
        "business_owner": "VinuKumarR",
        "nature_of_business": "FUOWS IT SOLUTIONS",
        "phone_number": phone_number,
        "email": email,
        "commission_account_number": commission_account_number,
        "terminal_id": terminal_id,
        "actual_location": "Bangalore",
        "coordinates": gps_coordinates,
        "country": "Uganda",
        "district": "Gulu",
        "parent_region": "Central Region",
        "parent_branch": "Gulu Main Branch",
        "mtn_pos_simcard": mtn_pos_simcard,
        "airtel_pos_simcard": airtel_pos_simcard,
        "authorisation_profile": "AUTH_PRO_DEMO_NEW",
        "security_profile": "Security_Profile_Demo_New"
    }