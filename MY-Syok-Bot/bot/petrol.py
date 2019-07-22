from requests import get
from parsel import Selector as sel


def PetrolPrice():
    """DaMaCaiDMCJackPot Methods!"""

    # Connect to Source
    url='https://hargapetrol.my/malaysia-petrol-prices-list.html'
    data=get(url,headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,zh-TW;q=0.7,zh;q=0.6','Cache-Control': 'max-age=0','Connection': 'keep-alive','DNT': '1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'})

    # Find the valid range
    date_from=sel(text=data.text).xpath('.//div[@class="daterange active"][1]/text()').get()
    date_till=sel(text=data.text).xpath('.//div[@class="daterange active"][2]/text()').get()
    
    # Price
    ron95=sel(text=data.text).xpath('//div[@class="ron95 active"][1]/text()').get()
    ron97=sel(text=data.text).xpath('//div[@class="ron97 active"][1]/text()').get()
    diesel=sel(text=data.text).xpath('//div[@class="diesel active"][1]/text()').get()
    ron95_lw=sel(text=data.text).xpath('.//span[2]//span[@itemprop="priceComponent"]//div[@class="ron95"]/text()').get()
    ron97_lw=sel(text=data.text).xpath('.//span[2]//span[@itemprop="priceComponent"]//div[@class="ron97"]/text()').get()
    diesel_lw=sel(text=data.text).xpath('.//span[2]//span[@itemprop="priceComponent"]//div[@class="diesel"]/text()').get()
    ron95_diff=round((float(ron95)-float(ron95_lw)))
    ron95_diff='+'+'{:.2f}'.format(ron95_diff) if ron95_diff>=0 else'-'+str(ron95_diff)
    ron97_diff=round((float(ron97)-float(ron97_lw)),3)
    ron97_diff='+'+'{:.2f}'.format(ron97_diff) if ron97_diff>=0 else'-'+str(ron97_diff)
    diesel_diff=round((float(diesel)-float(diesel_lw)),3)
    diesel_diff='+'+'{:.2f}'.format(diesel_diff) if diesel_diff>=0 else'-'+str(diesel_diff)
    
    prices = "RON95 - " + "RM"+str(ron95)+"({})".format(ron95_diff) + "\nRON97 - " + "RM"+str(ron97)+"({})".format(ron97_diff) + "\nDiesel - " + "RM"+str(diesel)+"({})".format(diesel_diff)
    
    
    # Create Reply
    chat_reply = "<b>Petrol prices from " + str(date_from) + " until " + str(date_till) + "</b> \n\n"
    chat_reply += prices

    return chat_reply