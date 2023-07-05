import requests,re,json,csv
import time



with open('淘宝耳机.csv', 'a', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['名字', '价格', '生产地方', '相片'])

i = 0
for i in range(0,10):
        print(f'------下载第{i}页完成-------')
        if (i==0):
                url = 'https://s.taobao.com/search?q=%E8%80%B3%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20230625&ie=utf8&bcoffset=10&p4ppushleft=2%2C48&ntoffset=10&s=0'
        else:
                url= f'https://s.taobao.com/search?q=%E8%80%B3%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20230625&ie=utf8&bcoffset=4&p4ppushleft=2%2C48&ntoffset=4&s={i*44}'
        header  ={
        'Cookie':'miid=661948176383522386; enc=vFjc%2FqvZmb37%2BoP28hmpQNB5tuwXlzqlPQELlSfaXZUInbchXRtRLlcY0phq2J2Y3K6%2FjL41IT7zux%2FNE4hs%2FhTV1ItrmJ18Ja5WIEvCjRrEB4CaoceJY51NYNydtr3u; _m_h5_tk=4055a5ab2d84b28a908ea694acbca45f_1687627850007; _m_h5_tk_enc=1d4841908ff80b443d2f32fae143e961; cna=gMwQHYQM3w8CAaslzJUCYgej; xlly_s=1; t=e9d579910c633627405fe3f769a7c154; sgcookie=E1004gg4e2bBWWdPDQPouJmKBgp%2BB%2BMaDjF%2FXW94lqtL3b6mZH2TBFlnsJmH8MMdKwhYM%2Bt7gnH0GvxqFPCteNP9%2BYfo8YxY2oVoLc%2FAAiJjdik%3D; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&nk2=GcA1v%2FECgbLld0njJjrIuw%3D%3D&id2=UNN78EuEBV7b%2Bw%3D%3D&vt3=F8dCsGOwwFR6s%2B6Fh9k%3D; lgc=zheng17777551774; uc4=nk4=0%40GwlEf7NJtlbZEly8tlw03KABGbxkssoCDBug&id4=0%40UgQz068StiU34hNsmBDf%2F1QapaOf; tracknick=zheng17777551774; _cc_=U%2BGCWk%2F7og%3D%3D; thw=cn; mt=ci=-1_0; uc1=cookie14=Uoe8jR05d%2FxrMA%3D%3D; _tb_token_=3049e1a685301; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=6ED395491A24594B6949B5214F15C0D9; tfstk=cJ9NBg2GsAHaLFKxy9X2z6_7Fx6OZybcPJSPs2cz_G042GfGi34AxoY1YirUo1f..; l=fBEK49N7NA9eDOmzBOfaFurza77tSIRYSuPzaNbMi9fP_L5p5U-RW16lH3Y9CnGVF6zkR3lDK4dwBeYBqIv4n5U62j-la6kmnmOk-Wf..;isg=BJGRzrc_kTcYSP0j4ZjfM8xvoJ0r_gVw0a6KLXMmhNhlGrFsu0wqQIR4vO78F52o; _samesite_flag_=true; cookie2=16a783183d9c5b5be3febea420abb151',
        'Referer':'https://www.taobao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        r = requests.get(url = url,headers = header).content.decode(' utf -8')
        r1 = re.findall('g_page_config = (.*);',r)[0]
        r2 = json.loads(r1)
        r3 = r2['mods']['itemlist']['data']['auctions']
        for r4 in r3:
                try:
                        raw_title = r4['raw_title']
                        view_price =r4['view_price']
                        item_loc = r4['item_loc']
                        pic_url = r4['pic_url']
                        print(raw_title,'\n',view_price,'\n',item_loc,'\n',pic_url)
                        with open('淘宝耳机.csv', 'a', encoding='utf-8', newline='') as f:
                                csv_writer = csv.writer(f)
                                csv_writer.writerow([raw_title, view_price, item_loc, pic_url])
                                csv_writer = f.close()
                                # time.sleep(0.5)
                except:
                        pass

