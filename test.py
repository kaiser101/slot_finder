import requests
import json
from pprint import pprint
import datetime


def get_slots(zip):
    # tomorrow = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow_fmt = tomorrow.strftime("%d-%m-%Y")

    request_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(
        zip, tomorrow_fmt)
    response = requests.get(request_url)

    sessions = response.text
    sessions_dict = json.loads(sessions)
    centres = sessions_dict["sessions"]

    # print(centres)
    centres_avail = [
        x for x in centres if x["available_capacity_dose2"] > 0
        and x["vaccine"] == "COVISHIELD" and x["min_age_limit"] == 18
    ]

    for centre in centres_avail:
        print("Name: ", centre["name"])
        print("Address: ", centre["address"])
        print("Date: ", centre["date"])
        print("Available: ", centre["available_capacity_dose2"])
        print("Slots:")
        pprint(centre["slots"])
        print(
            "================================================================================"
        )


def get_slots_by_dist(dist):
    # tomorrow = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow_fmt = tomorrow.strftime("%d-%m-%Y")

    request_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
        dist, tomorrow_fmt)
    response = requests.get(request_url)

    sessions = response.text
    sessions_dict = json.loads(sessions)
    # pprint(sessions_dict)
    centres = sessions_dict["sessions"]

    # print(centres)
    centres_avail = [
        x for x in centres if x["available_capacity_dose2"] > 0
        and x["vaccine"] == "COVISHIELD" and x["min_age_limit"] == 18
    ]
    centres_avail.sort(key=lambda x: x["pincode"], reverse=False)

    for centre in centres_avail:
        print("Name: ", centre["name"])
        print("Address: ", centre["address"])
        print("Pincode: ", centre["pincode"])
        print("Date: ", centre["date"])
        print("Available: ", centre["available_capacity_dose2"])
        print("Slots:")
        pprint(centre["slots"])
        print(
            "================================================================================"
        )


# zip_codes = input()
# print(zip_codes)

# for zip in zip_codes.split(","):
#     get_slots(zip)

# dist = input()
dist = 395
# Mumbai - 395

if __name__ == '__main__':
    get_slots_by_dist(dist)
