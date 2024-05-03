import requests
<<<<<<< HEAD
import os
=======
>>>>>>> 532c48cd928215779395298e7205ed8aaafc3749
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/verifyDeltaStatus", methods=["POST"])
def verifyDeltaStatus():
    url = "https://www.delta.com/checkout/validateskymilesmember"
    payload = {
        "firstName": request.json["firstName"],
        "lastName": request.json["lastName"],
        "skymilesNumber": request.json["skymilesNumber"],
        "ffProgrammeCode": "DL",
        "suffix": "",
        "travelDate": "2024-06-21"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=utf-8',
        'X-APP-CHANNEL': 'RSB-Booking',
        'CacheKey': 'f7b6877a-dbdd-4f48-93fa-6aefe0c4eba8',
        'channelId': 'ECOM',
        'appId': 'CKO',
        'airlineCode': 'DL',
        'isMobile': 'false',
        'pageName': 'ABC',
        'Origin': 'https://www.delta.com',
        'Referer': 'https://www.delta.com/complete-purchase/review-pay?cacheKeySuffix=f7b6877a-dbdd-4f48-93fa-6aefe0c4eba8&cartId=4ca76c7a-e8ec-4646-b617-34ea2d1553c3',
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    response_data = response.json()
    filtered_response = filter_response_data(response_data)
    return (filtered_response)

def filter_response_data(response_data):
    filtered_data = {}
    try:
        filtered_data["firstName"] = response_data["passengerInfo"]["basicInfo"]["name"].get("firstName", "")
    except KeyError:
        filtered_data["firstName"] = ""
    
    try:
        filtered_data["lastName"] = response_data["passengerInfo"]["basicInfo"]["name"].get("lastName", "")
    except KeyError:
        filtered_data["lastName"] = ""
    
    try:
        filtered_data["middleName"] = response_data["passengerInfo"]["basicInfo"]["name"].get("middleName", "")
    except KeyError:
        filtered_data["middleName"] = ""
    
    try:
        filtered_data["accountBalance"] = response_data["passengerInfo"]["loyaltyAccount"].get("accountBalance", "")
    except KeyError:
        filtered_data["accountBalance"] = ""
    
    try:
        filtered_data["loyaltyAirlineCode"] = response_data["passengerInfo"]["loyaltyAccount"].get("loyaltyAirlineCode", "")
    except KeyError:
        filtered_data["loyaltyAirlineCode"] = ""
    
    try:
        filtered_data["loyaltyNumber"] = response_data["passengerInfo"]["loyaltyAccount"].get("loyaltyNumber", "")
    except KeyError:
        filtered_data["loyaltyNumber"] = ""
    
    try:
        filtered_data["loyaltyTierLevel"] = response_data["passengerInfo"]["loyaltyAccount"].get("loyaltyTierLevel", "")
    except KeyError:
        filtered_data["loyaltyTierLevel"] = ""
    
    try:
        filtered_data["mismatchedName"] = response_data.get("mismatchFldNames", "")
    except KeyError:
        filtered_data["mismatchedName"] = ""

    try:
        filtered_data["skymilesNumberExists"] = response_data.get("profileExist", "")
    except KeyError:
        filtered_data["skymilesNumberExists"] = ""

    try:
        filtered_data["profileMatch"] = response_data.get("profileMatch", "")
    except KeyError:
        filtered_data["profileMatch"] = ""

    
    return filtered_data
<<<<<<< HEAD

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
=======
if __name__ == "__main__":
    app.run(port=5000)
>>>>>>> 532c48cd928215779395298e7205ed8aaafc3749



