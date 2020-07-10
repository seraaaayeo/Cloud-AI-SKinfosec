from bs4 import BeautifulSoup
from urllib import request

def test_crawling():
    target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
    soup = BeautifulSoup(target, "html.parser")

    for location in soup.select("location"):
        print("도시: ", location.select_one("city").string)
        print("날씨: ", location.select_one("wf").string)
        print("최저기온: ", location.select_one("tmn").string)
        print("최고기온: ", location.select_one("tmx").string)
        print("=="*12)

def main():
    test_crawling()

if __name__ == "__main__":
    main()