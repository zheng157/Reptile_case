import scrapy
from scrapy import Request
import json
from zy.items import ZyItem

class YiSpider(scrapy.Spider):
    name = "yi"
    allowed_domains = ["gxggzy.gxzf.gov.cn"]

    def start_requests(self):
        for i in range(1, 11):
            yield Request(url="http://gxggzy.gxzf.gov.cn/igs/front/search/list.html?&filter%5BDOCTITLE%5D=&pageNumber={}&pageSize=10&index=gxggzy_jyfw&type=jyfw&filter%5Bparentparentid%5D=84165&filter%5Bparentchnldesc%5D=%E9%93%81%E8%B7%AF%E5%B7%A5%E7%A8%8B&filter%5Bchnldesc%5D=%E6%8B%9B%E6%A0%87%E5%85%AC%E5%91%8A&filter%5BSITEID%5D=234&orderProperty=PUBDATE&orderDirection=desc&filter%5BAVAILABLE%5D=true".format(i))

    def parse(self, response):
        china_data = json.loads(response.text)
        china_data = china_data['page']['content']
        for i in china_data:
            url = i['DOCPUBURL']
            yield scrapy.Request(url=url, callback=self.pa)

    def pa(self,response):
        timu = response.xpath('//div[@class="ewb-page-main"]/div/div/h1/text()').extract_first().strip()
        shijian = response.xpath('//div[@class="ewb-page-line"]/div[2]/text()').extract_first().strip().replace("\n", "")
        div = response.xpath('//center//tr/td')

        neirong = div.xpath('string()').extract_first().strip().replace("\t\n", "")

        movie = ZyItem(timu=timu,shijian=shijian,neirong=neirong)
        yield movie