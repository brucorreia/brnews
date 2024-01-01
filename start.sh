#!/bin/sh
cd news
spiders=$(scrapy list)

for spider in $spiders ; do
    scrapy crawl $spider
done