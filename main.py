from typing import Union
import requests

from fastapi import FastAPI
app = FastAPI()

@app.get("/api/v1/get-id-tik-tok")
def read_item(user: Union[str, None] = None):
    if not user:
        return {'status': "failed", "msg": "Không được để trống tham số"}
    else:
        try:
            headers = {
                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                'sec-ch-ua-mobile': '?1',
                'save-data': 'on',
                'upgrade-insecure-s': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'Cookie': 'MONITOR_DEVICE_ID=eb619d15-64d5-4ad2-b420-2c9d9c4ea501; MONITOR_WEB_ID=f0245b08-d2cc-4e98-8afa-3395f0ac5d75; _ttp=2BcPe8Dx5Nf1a3JtYB7H81RH9gc; passport_csrf_token=775523a3905ab979d493222495099d63; passport_csrf_token_default=775523a3905ab979d493222495099d63; uid_tt=2feb93d88e3cf3e48b77de8b6608af5b70026cb203eed485b487494280486aad; uid_tt_ss=2feb93d88e3cf3e48b77de8b6608af5b70026cb203eed485b487494280486aad; sid_tt=b017f720bd245d3e8d455d292a8b78c3; sessionid=b017f720bd245d3e8d455d292a8b78c3; sessionid_ss=b017f720bd245d3e8d455d292a8b78c3; store-idc=useast2a; store-country-code=vn; tt-target-idc=alisg; passport_auth_status=2d61ba03dbd9bd1b7317fa6e7cd4ef41%2C724db7b5e05f5b6502f5a380de9f5550; passport_auth_status_ss=2d61ba03dbd9bd1b7317fa6e7cd4ef41%2C724db7b5e05f5b6502f5a380de9f5550; sid_guard=b017f720bd245d3e8d455d292a8b78c3%7C1659341919%7C5183999%7CFri%2C+30-Sep-2022+08%3A18%3A38+GMT; sid_ucp_v1=1.0.0-KGQwNjEwYjAxOWU2NjBjNTM1NTcwMDk5YWYxNmNmYjJiNTIzYjEzODAKHwiGiJuS_4yd8WIQ35ielwYYswsgDDDckYqXBjgIQBIQAxoGbWFsaXZhIiBiMDE3ZjcyMGJkMjQ1ZDNlOGQ0NTVkMjkyYThiNzhjMw; ssid_ucp_v1=1.0.0-KGQwNjEwYjAxOWU2NjBjNTM1NTcwMDk5YWYxNmNmYjJiNTIzYjEzODAKHwiGiJuS_4yd8WIQ35ielwYYswsgDDDckYqXBjgIQBIQAxoGbWFsaXZhIiBiMDE3ZjcyMGJkMjQ1ZDNlOGQ0NTVkMjkyYThiNzhjMw; cmpl_token=AgQQAPOFF-RMpbLcmsB6dB0_-KHMWb7ZP4AOYMWBHA; __tea_cache_tokens_1988={%22user_unique_id%22:%227115781325290079746%22%2C%22timestamp%22:1659769414886%2C%22_type_%22:%22default%22}; xgplayer_device_id=43478913207; xgplayer_user_id=396069072062; _abck=28552CD461A531C88FD07BF19F365B8C~-1~YAAQDDPqfcCtWWyCAQAAk8sIjQgXFiRM41wKUf6tcMrgMxFB3jJgPbUuMEw1+VrvHfRFWUl1tzd89I1vyl1sdIBmQxImA+Hbi4KkyRMG2yE6KsZmrUUO+1fa3Qx/ztchDy6fId5PjMOXt+b2hKbh25GYZq2HEn6thcDv3Piz/zh1aNgwz3fsbeI+d/oCnM9f9vvikm3QPuYqn5AyHosErxkFKWsHVkTYbaTt1zSs7iKyNlFNu01yOV0YKvKJ+ItFbekMkxoljmd3gtaFLsEzyALpA00d7IxQSJ+HDtfqJakrN6aeiKxSOKiZ9HTQXAI+M2hD0jXs+1KSpj3sK8XPq6cw7sY/2HdoZFIWZ9o0qVdsWduKjYnQTM0ATtSu1RcNhMkeG+GWb5Wh4g==~-1~-1~-1; ak_bmsc=D2760580AC3BDF01692FF2DDB57E52EE~000000000000000000000000000000~YAAQDDPqfcGtWWyCAQAAk8sIjRCD/90q58J+TCN1vZRz+M3bk27diRzVgopNa3k4KRK9ATgg+9RnFyXA3U2BJNCfIrfalaVnNCVz/3yVuE/DeApZoPFrrJCP/vIrVybevDS11VJy2Qou0wyVpAOqp3MI5V1DXitlVC/NStc8SaBaYKLKObqwaU/H1asqJLtr/1qcoC0+CTV0If07vdkbxSc5spDxzFtbosFLg2gGfJlhaknsviE6cdW/WoMfasajXXaxBe2BGwqJrHZqisg9A+3ekpCFHrcbKG/5uQuXocrB1rUZSNFv5tDuJIBqXRYEZ3cH1fxOslSMccFTx3kqzySiVuPs4dp+uQ15NP9Vcn2bh0jIoZu7ScPJ1+ND0gCorrReNBiHYeE2DA==; bm_sz=8658B788872F921D9309343CC92E4BF7~YAAQDDPqfcOtWWyCAQAAk8sIjRDgJPFWJHiky00PjSrdVzsMCUNrklCnoSeXmLPFXCr69fs0yXN21aEGJLReC0ksTbpxF/mKrWdPseld2L9WjTwA7X88A1fcdpqP1egvoDhubv6JfAL0zQwLUFO1s68dKXGeVI1tB0vXxIt8M/Kb2Hp4nq1V4TzoHfoSoZRouBQntwNMVewe/62FqJaAumuw9QtwW3PEoHz+nFUE5QLhH4v3M5KGUkFx8NWRZYG3oDsno3s/ZiNgafLeDh1ivUnDE7WrFztA5gExWRAASJrW3Pw=~4277045~4273459; tt_csrf_token=fBQLGCry-yXjD_c1VZd-gmToE6pS5J9mdbUw; passport_fe_beating_status=true; ttwid=1%7C5cFkv3mG_G4Rtphi_CRtW2LpbxZr8QGrKp5Awz623ec%7C1660229973%7C771c0850d3dbf6c1f1059c331a6acaa175a42a8fb9cc762039e4b37bdbb340d9; odin_tt=f3fcb3ee0f5257e0f98514602d5207801435726480b613d71ba4193a4e0a9740ff8291422cef4f3ceaa8713ea761df0ef70af09ac1bb4902fd0f36d5e746f33f8ac52872ef93eea1c534ed75add0629f; s_v_web_id=verify_l6p628gj_rlRIuNdJ_zsI2_4fJ0_9KAC_CZEsBHaCHnk6; msToken=e7zX7fHUSarodLz_s1V7zfPvDIFFocbURScWCmQxsdySQzLrmamnaEuD17zZoDkjgECfPhLcwHX31yhkdeWDf0rG9dCPlgD0cECyB6vcD5zZKn2NbkcoviThwbYDUSp9IqqCNKA=; msToken=-L5RF1XtRB9WMir-3PAp-92714f0viGCrek8xS4WhNZ9idmV-S6UIqaZcV4YUJNCNrSB5ZQvPC7HSsY-xtf32AtTYOe4uAm128W-yqbupew5ehteha301bEMzGQV3nIn7iAdv1k=; bm_sv=04087BB0C4AC92E43FEA1265DB96F2C9~YAAQVXFHG9OHwmGCAQAArhhrjRBoXZWm7Y/IjDnASGrR/odi0FZpgNT6igzf7vRFrCE8wy5+IW7Y9QOMMQelCF0Kf5oEG7zRJKyr6y5gGIZH2ymZNUDG9KpW8+KyIcLjeVIczslR7d2nttcLLACEZ6ixXkO3N3AR2pcwTBmMOWRmkwHEagaDIbs7baizPkpliwm+qFAXaxXf7R0/XbQ98pbNZ/OLBgCcHwt1BadOsDY0T5rJy68n3P4quXQNoXRW~1; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDQuMC4wLjAgU2FmYXJpLzUzNy4zNg%3D%3D; _uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F104.0.0.0%20Safari%2F537.36;',
                'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            }
            j = requests.get(f'https://www.tiktok.com/@{user}', headers = headers).text
            h = j.split('{"id":"')[1].split('"')[0]
            return {'status': "success", "msg": "Lấy ID Thành Công", 'data': {'id': h}}
        except:
            return {'status': "failed", "msg": "Lấy ID Thất Bại"}   
