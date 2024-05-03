import requests
import os
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
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'X-APP-CHANNEL': 'RSB-Booking',
    'CacheKey': '32d9997e-2eb2-4f01-8d5c-35bb4fe19498',
    'channelId': 'ECOM',
    'appId': 'CKO',
    'airlineCode': 'DL',
    'isMobile': 'false',
    'pageName': 'ABC',
    'Origin': 'https://www.delta.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.delta.com/complete-purchase/review-pay?cacheKeySuffix=32d9997e-2eb2-4f01-8d5c-35bb4fe19498&cartId=e138f352-116f-43c4-92a8-c73bf9562fdf',
    'Cookie': 'dlsite=a; AMCV_F0E65E09512D2CC50A490D4D%40AdobeOrg=-894706358%7CMCIDTS%7C19847%7CMCMID%7C12044541794224227362292156089818387546%7CMCAID%7CNONE%7CMCOPTOUT-1714704621s%7CNONE%7CMCAAMLH-1715302221%7C7%7CMCAAMB-1715302221%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C2.3.0; pref=en-us; check=true; mbox=session#06b7f956962c47f1a2a07a880aa2d5b6#1714777900|PC#06b7f956962c47f1a2a07a880aa2d5b6.34_0#1778020840; RT="z=1&dm=delta.com&si=43729a79-7b17-4418-8723-e86afe6f004c&ss=1714775961143&sl=1&tt=5357&obo=0&sh=1714775967551%3D1%3A0%3A5357&bcn=%2F%2F17de4c0f.akstat.io%2F&ld=1714775967551&nu=&cl=1714775975750&r=https%3A%2F%2Fwww.delta.com%2F&ul=1714775978915&hd=1714775979224"; s_ecid=MCMID%7C12044541794224227362292156089818387546; AMCVS_F0E65E09512D2CC50A490D4D%40AdobeOrg=1; uuid=81068120-ccc5-42ae-aa5a-dbb2ebe4dfa9; exp_type=%5B%5BB%5D%5D; s_nr=1714776076027-Repeat; tnt_pagename=Booking%20Verify%20and%20Purchase; c_m=Googlewww.google.com; s_chl=%5B%5B%27Natural%2520Search%27%2C%271714697421967%27%5D%2C%5B%27Paid%2520Non-Search%27%2C%271714698344504%27%5D%2C%5B%27Natural%2520Search%27%2C%271714699571765%27%5D%5D; s_cpmscm=%5B%5B%27NS%257CKeyword%2520Unavailable%27%2C%271714697421967%27%5D%2C%5B%27Keyword%2520Unavailable%27%2C%271714698344505%27%5D%2C%5B%27NS%257CKeyword%2520Unavailable%27%2C%271714699571765%27%5D%5D; s_cc=true; TLTSID=1F41E74A08E710085FCBF3D6229BAE2A; TLTUID=1F41E74A08E710085FCBF3D6229BAE2A; prefUI=en-us; ft_id=5967C2C5B906A2; criteoid=; _fbp=fb.1.1714697424316.575061398; QuantumMetricUserID=532a2cbef8a874a507e98ee310862a74; visitorID=48ab0c56-3e38-476b-87cf-3a7d153fcc2b; tkpi_phid=7e9271bb-e510-469c-ba27-128b69b6953b; tkpiphid=7e9271bb-e510-469c-ba27-128b69b6953b; tkpi_fvid=51c2bb29-ceb9-4d2f-bb63-e70400533b32; akaalb_www_alb=~op=www_delta_metering_channelsAPI_dig_east:www_delta_channels_dig_east|www_delta_50_channelsAPI_east:www_delta_channels_east|www_delta_prda:prda|www_delta_aws_s3_ew:www_delta_aws_s3_east|www_delta_metering_channelsAPI_east:www_delta_channels_east|~rv=99~m=www_delta_channels_dig_east:0|prda:0|www_delta_aws_s3_east:0|www_delta_channels_east:0|~os=48d273ae4858bbc3223560588306b0ba~id=adb38c45ded513e3e196eeeafc492023; _abck=718DE461C2207FC065AE6C07B7C4E878~0~YAAQZWDcF2AYdjSPAQAAjzadQAtWK977gexdcjxO6AUWqBOsyWdGgNwQQJAsg3mFGfiP8goX2sXnSKc8HSS2Nlxst0hFBJwAvWnqKi3DQdI+jLCsWIESk3fAOWrBLZaCRDC7eil16Pi6Qh8xuv5dNtwhi0vWtkS4ivBt2329mKd0eL48wBoK3yEBW35mQi5R8doQK42DwFUV3fpSgyxej9E4pcYP+nyMQPAQp6x3rHkeSE93am3fUAV314CMoOKiL1m2y3T4eHuBqceO9u4G2Zv/jcC2LS69hZwFiKbbpcyXZf74wumWmnxwJhWA346kfVPZl+JBFn8E0S3iWzTGIU5SZtPsImzeOiGJZUJNp8L3JJjvNp5CL4m08K1k9l5qO/8wsXgX7dByeQ8w8jjoUfJeT/jHKl9+lsYYViaG06N6cN5G8x4w4JscjsYbZuJEO0MOTYmab8Bs~-1~-1~1714779562; xssid=f69364e0-f0e1-4e3f-816f-76e3556368ca; dtCookie=v_4_srv_11_sn_A8F5CD55A39B5D85845F04522EB34F73_app-3A9912e316bf6ad580_1_ol_0_perc_100000_mul_1; BIGipServerPUBLISH-A-TRACKGROUP2-443_pool=553929226.64288.0000; k_user_id=_k_CjwKCAjw88yxBhBWEiwA7cm6pWlGCbtNk0PEhZde2DIEOGWtI6ljoAlWsP_IZtgtfsQ8t2AeKE_n4RoCjRoQAvD_BwE_k_; JSESSIONID=0000VEh2BkO4_p-n0d2d5LVdbSp:-1; IBMID=VEh2BkO4_p-n0d2d5LVdbSp:2; DL_PER=true; AAMC_delta_0=REGION%7C7; aam_uuid=18421204454268764071650795387433119101; s_sq=%5B%5BB%5D%5D; LPVID=NhZjdmYjMxMWQ5ZGNmNDgx; LPSID-29060121=BGWUOlZISyWj9YhaY4gatg; BIGipServerPUBLISH-A-TRACKGROUP1-443_pool=503597578.64288.0000; mobile=N; home_page=rhp; hpr_user=y; rxVisitor=171475291915819U0T5RSHPDR7B27AMPNHLF7RA1GGU0P; dtPC=11$575980103_278h-vOIJUUBGFITSRLOOWCNGRHALCKHFCUTAA-0e0; rxvt=1714777796143|1714775961985; dtLatC=3; dtSa=false%7Cxhr%7C11%7Cx%7Cx%7C1714775996143%7C575980103_278%7Chttps%3A%2F%2Fwww.delta.com%2Fflightsearch%2Fsearch-results%3FcacheKeySuffix%3D32d9997e-2eb2-4f01-8d5c-35bb4fe19498%7C%7C%7C%7C; s_nr=1714775963372-Repeat; _dpm_id.6941=9942ab9a-3bab-4c6b-b5d9-a979402c4b5c.1714752922.2.1714775964.1714752922.159adacd-dec1-45d8-96cf-2a466a120675; kndctr_F0E65E09512D2CC50A490D4D_AdobeOrg_identity=CiYxMjA0NDU0MTc5NDIyNDIyNzM2MjI5MjE1NjA4OTgxODM4NzU0NlIQCOrG9PnzMRgBKgNWQTYwA_AB6sb0-fMx; trip_type=; AMCV_F0E65E09512D2CC50A490D4D%40AdobeOrg=-894706358%7CMCIDTS%7C19847%7CMCMID%7C12044541794224227362292156089818387546%7CMCAID%7CNONE%7CMCOPTOUT-1714783203s%7CNONE%7CMCAAMLH-1715302221%7C7%7CMCAAMB-1715380803%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C2.3.0; xssidsec=0e310c8f-8ff9-4841-98e8-61b742e4c17a; _cc=AeVBMwWa8VdTUP26PdQV65BV; _cid_cc=AeVBMwWa8VdTUP26PdQV65BV; dtPCB=true; AKA_A2=A; ak_bmsc=1CB8FF3A01DC85B8D27BA3BFF6BA799C~000000000000000000000000000000~YAAQZWDcFx8YdjSPAQAA1cKcQBc9juB0nLQsK90rXnzekNCgHn7FN77f9OcbO00Lm9HT9597FgI8hXPKvreGuySSQStm1VZjMeinPwYg5pp2LPSY9E6p7/sj2pGjm0Dyljax/DDZD8/0qO5EuEVZOb5eskvYkkFntvqjgH07modyIynpQbNVvOxqommI/gUKTTBLJv6EFMaDM1V5y6V2vk83fspO9AbNBT05OyXuPAZu1ZXJJGj4qdp89W7gF4S8s4f1dDnhdxVQOEYJOPQYpJQo/i4tEthpduJZUSwFgX4RD6Yj6gkhp+IvH5NCwNvLLYR6hRP9Q8j5fppQ8AVA+Qmz4i+LBZdkpE+p44YCvf6DY+3zga9LpT+OI0qMAq9npH9ecb9Ck/QKezTy05hPl5R2EZRRJqr+gCXCS10u21tPv5sMG3X949RgQ5ecRxTBqrrlsTbnb969gZ5ZwVKHVu9bzd0ARqZE5bi4lDdjY1JFxLXlWP4CDGvVRqYY22d6xvNlr0s=; bm_sz=E6615F350F4241A7AF27186703D20145~YAAQZWDcF2UYdjSPAQAALTqdQBfYKdC9oRpLF/h18OHFLX4RBgwiMURIAxLDL8cAaW1VGLhCdmV4YHECCkjSmaTZs0JSLMTtRELvBciG1MAWVRziK422nnp12Kbw9+NyHhOL/DEteldqTjTRN0RLqUTXNf1jkX2/en66FskhWCfvkcwVJbi7Y7iHvYZ/wwJYogSXpUQku0J1xOmpN/IyIuyBGmsgDkTZ4ZKmGTMdY70DlzZMuBv6pbVW2TqoMHkcl5xo4APHvRb2j3dzuGAf8QonhCSxKVufGDZ5w08gyqCel45q0xaxZOmzv1mqyusbFCQit/nck4sskF5Z8URDB+Et99qmMkWUJZfvsfxGPlxZ6LNb4TuQuqsirrQqx3P3EG6PqoaSFvusVmD414S5+0T+K6nOlgChBwoX5yKPDYiUVkt5d8cD~4536369~3359545; bm_sv=551C9D78A3FA0D58D7913F8B1DA22735~YAAQZWDcF9MZdjSPAQAAQ5ieQBfsSWQNRDR2MZpR4pVRTXvIYivAFHBH9+2nBl8P6de4mnJOfefvRGgLdisqSFLQVZoDUoEDvJHMEjpxVwAcfpUg/Cxjs174EIFwZ/Yg+Lal64H+ftMyuOYuGXhIVYVqF86K3gmdNWWfUfP7m92K0X2QbEBKaa1WMDnnLwTb4cn1a7wTtMxGzLJ+m9vh1ep7b8/DHbYAVVDpaxf94hZj17lgviIDCHgr1BsF6Y/D~1; bm_mi=F4A56572A74F50BA1AEB6B33B2F5E568~YAAQZWDcFxMYdjSPAQAAA7acQBfRRnQtHPZU1x6Mw9fMySydxLAMBtMPZR11R4SUsqfZ6WDw3C1i51jcGvcz7uYB/mt+NdPWjSjgj0bKZa/cNy1+kCyRRXSz83iiryVacKovVBJsVlEvaVxmP1FLGb4FmUmO7XgxsNG0ADOAFNpKMOozmbxTSUwJ+cpGdjIKV7M0W/3kcvPt7PR0iPO8nveIEPTUv4ZUrBaADWd8s6Q+6HriURbr/e5iDSSE4eJOTw/16Il2SgaxP87ZbLcIq/1y6ZZJwUKaFCUlM8RmQbJnFUquFhVhJ3cdZjw6POKYtxoTbQCE0ZibeZULU1aTvlMl5LGDMVjdGO+nEUe55K8=~1; _dpm_ses.6941=*; kndctr_F0E65E09512D2CC50A490D4D_AdobeOrg_cluster=va6; mboxEdgeCluster=34; QuantumMetricSessionID=fc1ade6eb43acaf1d5d8c98963cb9a84; SFAFFlowRouterCookie=/flightsearch/search-results; s_visit=1; s_dl=1; cko_aws_rev=onprem; 53325=; tas=%7B%22createdDate%22%3A1714775968021%2C%22ID%22%3A%22sgnr17sj3ve.1714775968021%22%2C%22status%22%3A%22existing%22%2C%22lastVisitedDate%22%3A1714776040482%7D; TLTSID=45616906099F10099292D810EFD918F0; TLTUID=45616906099F10099292D810EFD918F0; _abck=5F800419A78FAF4DA154DC43176078DC~-1~YAAQLI8UAlnN2jSPAQAAEyClQAsVtaHNqWoE00t87pdtwKe4XUV0UmKDLpvn7u46arnPZfc3RILe6DollKI6SkNO56e6XAWPAVHK6yszueKXNb0LBBCVvmYuv8lImiSG9MnCFLpYy1WS3aaoShFTn3MrPMM8nM64kKFHNR8GIGCmfWRAsz4GksbYNHkLd++s8wEofn2h6AcQJv82ekKjW14NvJvgLUmZIYLLg8d5IZtowFLCegVDj8jpyjriZ22dGNV4LAhMkNFO2PmKD3P8xex6m0/TuRj99qU3Ty/v+nPeE6Hodlmu43cLikS0GfiLajAeWIEU8hlQlU1HXk+naJEDoDvoMvsojxjNqkA=~-1~-1~-1; ak_bmsc=EABCADB80376F9763F2C43776BCDA78D~000000000000000000000000000000~YAAQLI8UAqrN2jSPAQAA5n+lQBcHM0BV+17dIv4Hpdtz4daRQ0IpMgvNKWarYzWqXQWCa+S6HXzLhkUiXO4lT4rV/AoNHCd9jLKVzRUqXLi+2tD0bH5bFt77Q0AQZ9iDfCtWd3zo8MdA2TVZeifpV6TaRg0TiAC9WxxiCII9MWIZDV61eqwqS+uIWPIzHOUPJ6jvfOaqgZVj1+jhRnna9N2Fii09Fd1r9yHV7tMqRlc4TawOus4AF7BAZT1/tvxhAfaol8wTOoJ7cW8in4a7vqkBajcE7IDLuys22xsODn8fdxaakh8Fvl+lqtPlkZwztXKFdIpMCisxrq23wJo02thlLdYlUgC4mqcv7ru5pBaiOpEp8+2I2rXQ/A==; bm_sv=5009D0DEDCB069D389DFDE2CD34D8DA5~YAAQLI8UAl3n2jSPAQAAZESyQBd93NgqiJXxINnQr0zYZyeaHrHlhobFg/c8znt2IAVkP9jBF2QALvYJePXaYa5zALek625Ch3gf3wGhYDJkIsEoT5lEuT6efn3Dl/WppP1O9XBftkRL5VB3awBtWudcJJE8vMQOO4XK1PU0l2xw3mbbKNKO3wvGubywlGajULmmLJRahJVPStRi2daDdXOr4D0GB5SZ+ATqXVvOxNskhOHMRd1/XDvC2vjm5Oc=~1; bm_sz=EB9CAE1FD5B56FB21AD8607255DBC0B6~YAAQLI8UAlrN2jSPAQAAEyClQBceJo508K722TRSn043o1DUPYLd8QMQ2BrmP0CJXzIDvOhwSITEvynyv8cFRll2NKJ394hUyBbFyg+ZsLKnTZOfj1UClxKj1KuqvwjyhIGvwSwcD/tH63QhJd8d1nPg0UwaxQ5uc+0jNjBQcPaEuw1Qn2LkEaAFbpJUji1u6UtUbATPeS7SOtkfGCjX0AVixV/pL+0q9oXGqAQtUSI2FKFKlaQ9SJILCsmSzGTqi9ZQIMkue/kk5zjx530HjtayhYaBTOgGrO+ApRexpqDdpQx5ETkIRToKCkavnpuPeauPh+KrgV1iPtjyZ0dJUXwJzEybWK4ASrEN/n4xAsC14sr24toH7L/l~3160377~3225413; dlsite=a; xssid=303c8405-1548-4bbe-82c4-c0b6bda85c1f; IBMID=cNHMsZbq4QfaxdsDhKg1jR-:2; JSESSIONID=0000cNHMsZbq4QfaxdsDhKg1jR-:-1; akaalb_www_alb=~op=www_delta_prda:prda|~rv=88~m=prda:0|~os=48d273ae4858bbc3223560588306b0ba~id=36770bc46b6aaa34de383e3d4a994218',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



