# pip3 install scrapy
# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class FrasesSpider(Spider):
    name = "frases"
    start_urls = ("http://quotes.toscrape.com/login",)

    def parse(self, response):
        return FormRequest.from_response(
            response,
            formdata={"password": "foobar", "username": "foobar"},
            callback=self.scrape_pages,
        )

    def scrape_pages(self, response):
        print(response)
        open_in_browser(response)
        # html body div.container div.row div.col-md-8 div.quote
        for frase in response.css("div.quote"):
            yield {
                # html body div.container div.row div.col-md-8 div.quote span.text
                "texto": frase.css("span.text::text").get(),
                # html body div.container div.row div.col-md-8 div.quote span small.author
                "autor": frase.css("small.author::text").get(),
                # html body div.container div.row div.col-md-8 div.quote div.tags a.tag
                "tags": frase.css("div.tags a.tag::text").getall(),
            }
        # ruta css html body div.container div.row div.col-md-8 nav ul.pager li.next a
        next_page_url = response.xpath(
            "/html/body/div/div[2]/div[1]/nav/ul/li/a/@href"
        ).extract()
        if len(next_page_url) > 1:
            next_page_url = next_page_url[1]
        else:
            next_page_url = next_page_url[0]
        print("css de siguiente pagina: ", next_page_url)
        if next_page_url is not None:
            yield Request(
                url="http://quotes.toscrape.com" + next_page_url,
                callback=self.scrape_pages,
            )
