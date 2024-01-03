import scrapy
import json
from src.common.log import LoggerDefault
from src.common.jsonconverter import StringToJsonConverter
from src.repo.mongo import MongoDBInteractor
from src.repo.messages import TelegramNewsSender

class NewsSpider(scrapy.Spider):
    name = 'veja'
    start_urls = ['https://veja.abril.com.br/']

    def parse(self, response):
        logger = LoggerDefault()
        telegram_sender = TelegramNewsSender()
        site = "veja.abril.com.br"
        try:
            title = response.xpath('//h2[@class="title "][1]/text()').extract()[0].strip()
            url = response.xpath('//div[@class="card d"][1]/a[1]/@href').extract()[0]
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