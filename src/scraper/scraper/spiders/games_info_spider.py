import scrapy
import pathlib

class GamesInfoSpider(scrapy.Spider):
    name = "gamesinfo"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/category/GAME"]

    def parse(self, response):
        for category in response.css("div.Ktdaqe"):
            category_name = category.css("h2.sv0AUd.bs3Xnd::text").extract_first()

            for game in response.css("div.ZmHEEd.fLyRuc"):
                game_name = game.css("div.Vpfmgd div.WsMG1c.nnK0zc::text").extract_first()
                with open("scraped_data.txt", "a") as f:
                    f.write(f"APP/{category_name}/{game_name}\n")
