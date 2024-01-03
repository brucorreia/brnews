import scrapy
import json
from src.common.log import LoggerDefault
from src.common.jsonconverter import StringToJsonConverter
from src.repo.mongo import MongoDBInteractor
from src.repo.messages import TelegramNewsSender

class NewsSpider(scrapy.Spider):
    name = 'bbc'
    start_urls = ['https://www.bbc.com/portuguese']

    def parse(self, response):
        logger = LoggerDefault()
        telegram_sender = TelegramNewsSender()
        site = "bbc.com/portuguese"
        try:
            title = response.xpath('//a[@class="focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0"][1]/text()').extract()[0]
            url = response.xpath('//a[@class="focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0"][1]/@href').extract()[0]
            logger.register_info(f"Crawled from {site}, {title} {url}")

            converter = StringToJsonConverter()
            json_output = converter.convert(site=site, title=title, url=url)

            mongo_interactor = MongoDBInteractor()

            check_if_exist = mongo_interactor.get(json_output)

            if check_if_exist:
                logger.register_info(f"There is no news {check_if_exist}")

            else:
                telegram_sender.send(title, url)
                logger.register_info(f"New sended to Telegram {json_output}")

                mongo_interactor.insert(json_output)
                logger.register_info(f"New registred {json_output}")

        except Exception as e:
            logger.register_error("Error during an operation.", exception=e)