# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-7 下午9:25

import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return _('错误：没有配置翻译服务。')
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        return _('错误：翻译服务失败。')
    return json.loads(r.content.decode('utf-8-sig'))
