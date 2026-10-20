# # 문서 작업폴더
# # python -m venv .venv(가상환경) > 서버 컴퓨터에 필요한 라이브러리만 설치하기 위해서
# # 가상환경으로 들어가는 명령어
# # .venv\Scripts\activate
# # 가상환경에서 설치된 라이브러리 확인하는 방법
# # pip list 
# # 가상환경에서 빠져나오는 방법
# # deactivate
# # pip install requests(외부라이브러리 설치)
# pip install beautifulsoup4

    
# import requests
# from bs4 import BeautifulSoup

# keyword = "파이썬"

# url = f"https://job.incruit.com/jobdb_info/jobpost.asp?job&kw={keyword}"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, "html.parser")

# lis = soup.find_all("li", class_="c_col")

# print("검색된 항목 수:", len(lis))

# for li in lis:
#     company = li.find("a", class_="cpname")
    
#     if company is not None:
#         print(company.get_text(strip=True))


# import requests
# from bs4 import BeautifulSoup

# keyword = "파이썬"

# url = "https://job.incruit.com/jobdb_list/searchjob.asp"

# r = requests.get(url, params={"kw": keyword}, timeout=10)

# print("상태 코드:", r.status_code)
# print("실제 주소:", r.url)

# soup = BeautifulSoup(r.text, "html.parser")

# print("페이지 제목:", soup.title)
# print("HTML 길이:", len(r.text))

# lis = soup.find_all("li", class_="c_col")

# print("검색된 항목 수:", len(lis))

# print("li 태그 수:", len(soup.find_all("li")))
# print("c_col 개수:", len(soup.select(".c_col")))


# for li in lis:
#     try:
#         company = li.find("a", class_="cpname").text
#         li.find("div", class_="cell_mid").find("a").text
#         location = li.find("div", class_="cl_md").find_all("span")
#         print(title)
#     except:
#         pass

# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# keyword = "파이썬"

# url = "https://job.incruit.com/jobdb_list/searchjob.asp"

# r = requests.get(url, params={"kw": keyword}, timeout=10)

# print("상태 코드:", r.status_code)

# soup = BeautifulSoup(r.text, "html.parser")

# lis = soup.find_all("li", class_="c_col")

# print("검색된 항목 수:", len(lis))

# for li in lis:
#     company = li.find("a", class_="cpname")
#     title = li.find("a", class_="job_title")

#     if company is not None and title is not None:
#         company_name = company.get_text(strip=True)
#         job_title = title.get_text(strip=True)

#         link = title.get("href")

#         if link:
#             full_url = urljoin(r.url, link)

#             print("회사명:", company_name)
#             print("채용공고:", job_title)
#             print("링크:", full_url)
#             print("------------------")


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

keyword = "파이썬"
url = "https://job.incruit.com/jobdb_list/searchjob.asp"

for page in range(1, 6):
    print(f"\n===== {page}페이지 =====")

    params = {
        "kw": keyword,
        "page": page
    }

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    lis = soup.find_all("li", class_="c_col")

    print("검색된 항목 수:", len(lis))

    for li in lis:
        company = li.find("a", class_="cpname")

        if company is not None:
            company_name = company.get_text(strip=True)
            print("회사명:", company_name)

    time.sleep(1)
