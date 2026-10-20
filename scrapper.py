# 문서 작업폴더
# python -m venv .venv(가상환경) > 서버 컴퓨터에 필요한 라이브러리만 설치하기 위해서
# 가상환경으로 들어가는 명령어
# .venv\Scripts\activate
# 가상환경에서 설치된 라이브러리 확인하는 방법
# pip list 
# 가상환경에서 빠져나오는 방법
# deactivate
# pip install requests(외부라이브러리 설치)

import requests

r = requests.get('https://job.incruit.com/jobdb_info/jobpost.asp?job=2610160000200&src=gsw*www')
print(r.status_code)