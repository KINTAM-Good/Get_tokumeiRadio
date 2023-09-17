import requests
import urllib.request

base_url = "https://omocoro.heteml.net/radio/tokumei/"
falemessage = "取得できませんでした：匿名ラジオ"

def catch_url(this_url, rank_100, rank_10, rank_1):
    i = 0
    url_ = this_url+str(rank_100)+str(rank_10)+str(rank_1)+".mp3" 
    responce = requests.get(url_)
    if responce.status_code != 200:
        print(f"{falemessage}{rank_100}{rank_10}{rank_1}")
        return(falemessage)
    return(url_)

def save_file(min, max):
    
    for i in range(max-min+1):
        this_time = min+i
        rank_100 = this_time//100
        under_10 = this_time%100
        rank_10 = under_10//10
        rank_1 = under_10%10
        this_url = base_url
        
        save_url = catch_url(this_url, rank_100, rank_10, rank_1)
        if not(save_url in falemessage):
            urllib.request.urlretrieve(save_url, f"{rank_100}{rank_10}{rank_1}.mp3")


if __name__ == "__main__":

    max = int(input("max"))
    min = int(input("min"))
    save_file(min, max)