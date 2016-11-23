import scrapy
from lkdbinit.items import HospitalCheckItem
from lkdbinit.items import HosptailCheckPacakgeItem

class VipCheckItemSpider(scrapy.Spider):
    name = "viptj"
    allowed_domains = ["viptijian.com"]
    start_urls = [
        "http://www.viptijian.com/0592/xmxhfy-combo-25053",
        "http://www.viptijian.com/0592/xmxhfy-combo-25054",
        "http://www.viptijian.com/0592/xmxhfy-combo-25055",
        "http://www.viptijian.com/0592/xmxhfy-combo-25041",
        "http://www.viptijian.com/0592/xmxhfy-combo-25042",
        "http://www.viptijian.com/0592/xmxhfy-combo-25043",
        "http://www.viptijian.com/0592/xmxhfy-combo-25044",
        "http://www.viptijian.com/0592/xmxhfy-combo-25045",
        "http://www.viptijian.com/0592/xmxhfy-combo-25046",
        "http://www.viptijian.com/0592/xmxhfy-combo-25047",
        "http://www.viptijian.com/0592/xmxhfy-combo-25048",
        "http://www.viptijian.com/0592/xmxhfy-combo-25049",
        "http://www.viptijian.com/0592/xmxhfy-combo-25050",
        "http://www.viptijian.com/0592/xmxhfy-combo-25051",
        "http://www.viptijian.com/0592/xmxhfy-combo-25052",
        "http://www.viptijian.com/0592/xmxhfy-combo-25056",
        "http://www.viptijian.com/0592/xmxhfy-combo-25057",
        "http://www.viptijian.com/0592/xmxhfy-combo-25058"
    ]
    # start_urls = [
    #     "http://www.viptijian.com/0592/xmzs2-combo-23587",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23588",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23589",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23590",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23591",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23592",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23593",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23594",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23595",
    #     "http://www.viptijian.com/0592/xmzs2-combo-25844",
    #     "http://www.viptijian.com/0592/xmzs2-combo-25847",
    #     "http://www.viptijian.com/0592/xmzs2-combo-25849",
    #     "http://www.viptijian.com/0592/xmzs2-combo-25843",
    #     "http://www.viptijian.com/0592/xmzs2-combo-25840",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23596",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23597",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23578",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23579",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23598",
    #     "http://www.viptijian.com/0592/xmzs2-combo-23580",
    # ]

    # 抓取详情页的检查项目
    def parse(self, response):
        items = []
        # 抓取详情内容
        contentHtml = response.xpath('//body')
        hcpItem = HosptailCheckPacakgeItem()
        hcpItem['title'] = response.xpath('//div[@class="tcnameinfo"]/h1/text()').extract()
        hcpItem['image'] = response.xpath('//div[@class="tcimg"]/img/@src').extract()
        hcpItem['feature'] = response.xpath('//div[@class="tcname-info"]/text()').extract()
        hcpItem['price'] = response.xpath('//div[@class="tc-pri"]/span/em/text()').extract()

        # 抓取详情页中的检查项目
        for sel in response.xpath('//div[@class="Programlistbox"]'):
            item = HospitalCheckItem()
            item['title'] = sel.xpath('div[@class="Programname-txt"]/text()').extract()
            item['remark'] = sel.xpath('div[@class="Programworth-txt"]/text()').extract()
            # yield item
            items.append(item)
        hcpItem['items'] = items
        return hcpItem
