import requests

def test_qq2():
    url = 'http://japi.juhe.cn/qqevaluate/qq'
    parm = {
        'key':'23ec5ce89183d7d33e7327728fd4e92c',
        'qq':'1600344803'
    }
    r = requests.post(url=url,data=parm)
    print(r.json())

    error_code = r.json()["error_code"]
    print('取到的error_code：%s'%error_code)
    reason = r.json()["reason"]
    print('取到的reason：%s'%reason)

    # if error_code == 0:
    #     print('测试通过')

    #预期结果
    expect_resul = {'error_code': 0, 'reason': 'success'}

    #断言
    assert error_code == expect_resul['error_code']
    assert reason == expect_resul['reaso_n']

