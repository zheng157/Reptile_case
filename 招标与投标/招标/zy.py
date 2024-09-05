from lxml import etree
import requests
import json

for i in range(1,11):

    url = "http://gxggzy.gxzf.gov.cn/igs/front/search/list.html?&filter%5BDOCTITLE%5D=&pageNumber={}&pageSize=10&index=gxggzy_jyfw&type=jyfw&filter%5Bparentparentid%5D=84165&filter%5Bparentch" \
      "nldesc%5D=%E9%93%81%E8%B7%AF%E5%B7%A5%E7%A8%8B&filter%5Bchnldesc%5D=&filter%5BSITEID%5D=234&orderProperty=PUBDATE&orderDirection=desc&filter%5BAVAILABLE%5D=true".format(i)
    response = requests.get(url)


    json_data = response.content.decode('utf-8')

    json_obj = json.loads(json_data)

    url_list = json_obj['page']['content']


    for url_item in url_list:

        url3 = url_item['DOCPUBURL']

        response = requests.get(url3).content.decode('utf-8')
        url3_html = etree.HTML(response)
        timu = url3_html.xpath('//div[@class="ewb-page-main"]/div/div/h1/text()')[0].strip()
        shijian = url3_html.xpath('//div[@class="ewb-page-line"]/div[2]/text()')[0].strip().replace('\r\n', '')
        td_list = url3_html.xpath('//div[@class="ewb-details-info"]//tbody')
        if td_list:
            td = td_list[0]
        else:
            td_list =td_list
        content = td.xpath('string()').strip().replace('\r\n', '')
        data = {
            'timu': timu,
            'shijian': shijian,
            'content': content
        }
        with open('招标公告.json', 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
            f.write('\n')



