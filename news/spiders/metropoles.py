import scrapy
import json
from src.common.log import LoggerDefault
from src.common.jsonconverter import StringToJsonConverter
from src.repo.mongo import MongoDBInteractor
from src.repo.messages import TelegramNewsSender

class NewsSpider(scrapy.Spider):
    name = 'metropoles'
    start_urls = ['https://www.metropoles.com/']

    def parse(self, response):
        logger = LoggerDefault()
        telegram_sender = TelegramNewsSender()
        site = "metropoles.com.br"
        try:
            title = response.xpath('//*[@class="Text__TextBase-sc-1d75gww-0 IFscC noticia__titulo"]/a/@title').extract()[0].strip()
            url = response.xpath('//*[@class="Text__TextBase-sc-1d75gww-0 IFscC noticia__titulo"]/a/@href').extract()[0]
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