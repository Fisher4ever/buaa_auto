import requests
import sys
def main(argv):
        url='https://app.buaa.edu.cn/uc/wap/login/check'
        data={
                'username':argv[1],
                'password':argv[2]
        }
        re=requests.post(url=url,data=data)
        print(re.text)
        cookies=re.cookies
        url='https://app.buaa.edu.cn/buaaxsncov/wap/default/save'
        data={
                "sfzs": "1",
                "bzxyy": "",
                "bzxyy_other": "",
                "brsfzc": "1",
                "tw": "",
                "sfcxzz": "",
                "zdjg": "",
                "zdjg_other": "",
                "sfgl": "",
                "gldd": "",
                "gldd_other": "",
                "glyy": "",
                "glyy_other": "",
                "gl_start": "",
                "gl_end": "",
                "sfmqjc": "",
                "sfzc_14": "1",
                "sfqw_14": "0",
                "sfqw_14_remark": "",
                "sfzgfx": "0",
                "sfzgfx_remark": "",
                "sfjc_14": "0",
                "sfjc_14_remark": "",
                "sfjcqz_14": "0",
                "sfjcqz_14_remark": "",
                "sfgtjz_14": "0",
                "sfgtjz_14_remark": "",
                "szsqqz": "0",
                "sfyqk": "",
                "szdd": "1",
                "area": "北京市 海淀区 知春路",
                "city": "北京市 海淀区",
                "province": "北京市 海淀区",
                "address": "北京市海淀区知春路",
                "gwdz": "",
                "is_move": "1",
                "move_reason": "4",
                "move_remark": "",
                "uid": "421580",
                "created": "1629884956",
                "id": "4774628",
                "gwszdd": ""
        }
        re=requests.post(url=url,data=data,cookies=cookies)
        print(re.json())
        sckey=argv[3]
        msg=re.json()['m']
        requests.get("http://sc.ftqq.com/"+ sckey +".send?text=打卡成功啦！&desp=" + msg)
if __name__=='__main__':
        main(sys.argv)
