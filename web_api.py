import requests
import time

# IDを取得する
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(top_stories_url)
top_stories = response.json()

# 結果リスト
news_list = []

# トップ10件のニュースを取得する
for story_id in top_stories[:10]:
    # 必要に応じて数を変更
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story_response = requests.get(story_url)
    story_data = story_response.json()

    # タイトルとリンクを確認して、保存する
    if "title" in story_data and "url" in story_data:
        news_list.append({"title": story_data["title"], "link": story_data["url"]})
    else:
        # タイトルはあるけど、リンクがない場合
        news_list.append({"title": story_data.get("title", "No Title"), "link": None})

    time.sleep(1)

for news in news_list:
    print(news)
