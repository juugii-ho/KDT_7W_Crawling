# import os
# import sys
# import urllib.request
# client_id = ""
# client_secret = ""
# encText = urllib.parse.quote("빅데이터")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

# --------------------------------------------------------------------
#
# import urllib.request
# import datetime
# import json
#
# def get_request_url(url):
#     client_id = ""
#     client_secret = ""
#
#     req = urllib.request.Request(url)
#     req.add_header("X-Naver-Client-ID", '')
#     req.add_header("X-Naver-Client-Secret", '')
#
#     try:
#         response = urllib.request.urlopen(req)
#         if response.getcode() ==200:
#             return response.read().decode('utf-8')
#     except Exception as e:
#         print(e)
#         print(f"Error for URL: {url}")
#
# def get_naver_search(node, search_text, start, display):
#     base = "https://openapi.naver.com/v1/search"
#     node = f"/{node}.json"
#     query_string = f"{urllib.parse.quote(search_text)}"
#
#     parameters = ("?query={}&start={}&display={}".format(query_string,start,display))
#
#     url = base + node + parameters
#     response = get_request_url(url)
#
#     if response is None:
#         return None
#     else:
#         return json.loads(response)
#
# def main():
#     node = 'news'
#     search_text='신인 그룹'
#     cnt = 0
#
#     json_response = get_naver_search(node, search_text, 1, 100)
#     if (json_response is not None) and (json_response['display'] !=0):
#         for post in json_response['items']:
#             cnt +=1
#             print(f"[{cnt}]", end=" ")
#             print(post['title'])
#             print(post['description'])
#             print(post['originallink'])
#             print(post['link'])
#             print(post['pubDate'])
#
# if __name__=='__main__':
#     main()


# --------------------------------------------------------------------


import urllib.request
import datetime
import json

import pandas as pd


def get_request_url(url):
    client_id = "eulRYJfAaNOLYPP0P7su"
    client_secret = "GuHjJADpd9"

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-ID", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() ==200:
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print(f"Error for URL: {url}")

def get_naver_search(node, search_text, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    query_string = f"{urllib.parse.quote(search_text)}"

    parameters = ("?query={}&start={}&display={}".format(query_string,start,display))

    url = base + node + parameters
    response = get_request_url(url)

    if response is None:
        return None
    else:
        return json.loads(response)


def get_post_data(post, json_result_list, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')


    print(f'[{cnt}]', end=" ")
    print(title, end=": ")
    print(pdate, end=" ")
    print(link)

    json_result_list.append([cnt, pdate, title, description, org_link, link])



def main():
    node = 'news'
    search_text='신인 그룹'
    cnt = 0
    json_result_list=[]

    json_response = get_naver_search(node, search_text, 1, 100)
    while (json_response is not None) and (json_response['display'] !=0):
        for post in json_response['items']:
            cnt +=1
            get_post_data(post, json_result_list, cnt)

        start = json_response['start'] + json_response['display']
        json_response = get_naver_search(node, search_text, start, 100)

    print(f'전체 검색 수: {cnt}')

    columns = ['count', 'date', 'title', 'description', 'org_link', 'link']
    result_df =pd.DataFrame(json_result_list, columns=columns)
    result_df.to_csv(f'{search_text}_naver_{node}.csv', index=False, encoding='utf-8')


if __name__=='__main__':
    main()