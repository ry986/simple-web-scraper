import requests
from bs4 import BeautifulSoup

# 東京の天気ページ（Yahoo!天気）
url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"

# HTML取得
response = requests.get(url)
response.encoding = response.apparent_encoding  # 日本語対応

# BeautifulSoupで解析
soup = BeautifulSoup(response.text, "html.parser")

# 天気の情報を取得
weather = soup.find("p", class_="pict").text.strip()
high_temp = soup.find("li", class_="high").find("em").text.strip()
low_temp = soup.find("li", class_="low").find("em").text.strip()

# 出力
print(f"今日の東京の天気：{weather}")
print(f"最高気温：{high_temp}℃")
print(f"最低気温：{low_temp}℃")
