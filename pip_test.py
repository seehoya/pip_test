"""
requests를 테스트 해본다.

Ubuntu
    /home/<자기유저명>/.pyenv/versions/3.4.3/env/<가상환경이름>/bin/python
"""

import requests

r = requests.get('http://www.google.co.kr')
print(r.text)
