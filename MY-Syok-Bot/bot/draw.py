##
 # @author Joseph Goh
 # @email [joseph.kokchin.goh@outlook.com]
 # @create date 2019-07-20 15:09:24
 # @modify date 2019-07-20 15:09:24
 # @desc [The following code will extract the 4D Results]
 #/

""" Lucky Draw Methods """
from requests import get
from parsel import Selector as sel

def Magnum4D():
    """Magnum4D Methods!"""

    # Connect to Source
    url='https://www.gidapp.com/lottery/malaysia/4d'
    data=get(url)

    # Find latest Result
    latest_result_date=sel(text=data.text).xpath('.//article/div/div[1]/header/div/h5[1]/time/text()').get()

    # TOP PRIZES
    first=sel(text=data.text).xpath('.//article/div/div[1]/table/tbody/tr[2]/td[1]/span/text()').get()
    second=sel(text=data.text).xpath('.//article/div/div[1]/table/tbody/tr[2]/td[2]/span/text()').get()
    third=sel(text=data.text).xpath('.//article/div/div[1]/table/tbody/tr[2]/td[3]/span/text()').get()

    top_text = "1st - " + first + "\n2nd - " + second + "\n3rd - " + third + "\n\n"

    # SPECIAL PRIZE
    special_prize_ls=sel(text=data.text).xpath('.//article/div/div[1]/table/tbody/tr[4]/td//text()').getall()
    special_prize_ls=list(filter(lambda a: a !=' ', special_prize_ls))
    special_prize = "Special/Starter Prizes\n\n"
    for i in special_prize_ls:
            special_prize += i + "  "

    # CONSOLATION PRIZE
    consol_prize_ls=sel(text=data.text).xpath('.//article/div/div[1]/table/tbody/tr[6]/td//text()').getall()
    consol_prize_ls=list(filter(lambda a: a !=' ', consol_prize_ls))
    consol_prize = "\n\nConsolation Prizes\n\n"
    for i in consol_prize_ls:
            consol_prize += i + "  "

    # Create Reply
    chat_reply = "<b>Latest Magnum 4D Draw Results on " + latest_result_date + "</b> \n\n"
    chat_reply += top_text
    chat_reply += special_prize
    chat_reply += consol_prize
    chat_reply += "\n\n No need check la sure never win!"

    return chat_reply

def TOTO4D():
    """TOTO4D Methods!"""

    # Connect to Source
    url='https://www.gidapp.com/lottery/malaysia/4d'
    data=get(url)

    # Find latest Result
    latest_result_date=sel(text=data.text).xpath('.//article/div/div[2]/header/div/h5[1]/time/text()').get()

    # TOP PRIZES
    first=sel(text=data.text).xpath('.//article/div/div[2]/table/tbody/tr[2]/td[1]/span/text()').get()
    second=sel(text=data.text).xpath('.//article/div/div[2]/table/tbody/tr[2]/td[2]/span/text()').get()
    third=sel(text=data.text).xpath('.//article/div/div[2]/table/tbody/tr[2]/td[3]/span/text()').get()

    top_text = "1st - " + first + "\n2nd - " + second + "\n3rd - " + third + "\n\n"

    # SPECIAL PRIZE
    special_prize_ls=sel(text=data.text).xpath('.//article/div/div[2]/table/tbody/tr[4]/td//text()').getall()
    special_prize_ls=list(filter(lambda a: a !=' ', special_prize_ls))
    special_prize = "Special/Starter Prizes\n\n"
    for i in special_prize_ls:
            special_prize += i + "  "

    # CONSOLATION PRIZE
    consol_prize_ls=sel(text=data.text).xpath('.//article/div/div[2]/table/tbody/tr[6]/td//text()').getall()
    consol_prize_ls=list(filter(lambda a: a !=' ', consol_prize_ls))
    consol_prize = "\n\nConsolation Prizes\n\n"
    for i in consol_prize_ls:
            consol_prize += i + "  "

    # Create Reply
    chat_reply = "<b>Latest Sports TOTO 4D Draw Results on " + latest_result_date + "</b> \n\n"
    chat_reply += top_text
    chat_reply += special_prize
    chat_reply += consol_prize
    chat_reply += "\n\n No need check la sure never win!"

    return chat_reply

def DaMaCai4D():
    """DaMaCai4D Methods!"""

    # Connect to Source
    url='https://www.gidapp.com/lottery/malaysia/4d'
    data=get(url)

    # Find latest Result
    latest_result_date=sel(text=data.text).xpath('.//article/div/div[3]/header/div/h5[1]/time/text()').get()

    # TOP PRIZES
    first=sel(text=data.text).xpath('.//article/div/div[3]/table/tbody/tr[2]/td[1]/span/text()').get()
    second=sel(text=data.text).xpath('.//article/div/div[3]/table/tbody/tr[2]/td[2]/span/text()').get()
    third=sel(text=data.text).xpath('.//article/div/div[3]/table/tbody/tr[2]/td[3]/span/text()').get()

    top_text = "1st - " + first + "\n2nd - " + second + "\n3rd - " + third + "\n\n"

    # SPECIAL PRIZE
    special_prize_ls=sel(text=data.text).xpath('.//article/div/div[3]/table/tbody/tr[4]/td//text()').getall()
    special_prize_ls=list(filter(lambda a: a !=' ', special_prize_ls))
    special_prize = "Special/Starter Prizes\n\n"
    for i in special_prize_ls:
            special_prize += i + "  "

    # CONSOLATION PRIZE
    consol_prize_ls=sel(text=data.text).xpath('.//article/div/div[3]/table/tbody/tr[6]/td//text()').getall()
    consol_prize_ls=list(filter(lambda a: a !=' ', consol_prize_ls))
    consol_prize = "\n\nConsolation Prizes\n\n"
    for i in consol_prize_ls:
            consol_prize += i + "  "

    # Create Reply
    chat_reply = "<b>Latest DaMaCai 4D Draw Results on " + latest_result_date + "</b> \n\n"
    chat_reply += top_text
    chat_reply += special_prize
    chat_reply += consol_prize
    chat_reply += "\n\n No need check la sure never win!"

    return chat_reply

def DaMaCai3D():
    """DaMaCai3D Methods!"""

    # Connect to Source
    url='https://www.gidapp.com/lottery/malaysia/damacai'
    data=get(url)

    # Find latest Result
    latest_result_date=sel(text=data.text).xpath('.//*[@id="result-prizes3"]/div/div/h5[1]/b/time/text()').get()

    # TOP PRIZES
    first=sel(text=data.text).xpath('.//*[@id="result-prizes3"]/table/tbody/tr/td[1]/p/span/text()').get()
    second=sel(text=data.text).xpath('.//*[@id="result-prizes3"]/table/tbody/tr/td[1]/p/span/text()').get()
    third=sel(text=data.text).xpath('.//*[@id="result-prizes3"]/table/tbody/tr/td[1]/p/span/text()').get()

    top_text = "1st - " + first + "\n2nd - " + second + "\n3rd - " + third

    # Create Reply
    chat_reply = "<b>Latest DaMaCai 3D Draw Results on " + latest_result_date + "</b> \n\n"
    chat_reply += top_text
    chat_reply += "\n\n No need check la sure never win!"

    return chat_reply

def DaMaCai3DJackPot():
    """DaMaCai3DJackPot Methods!"""

    # Connect to Source
    url='https://www.gidapp.com/lottery/malaysia/damacai'
    data=get(url)

    # Find latest Result
    latest_result_date=sel(text=data.text).xpath('.//*[@id="result-jackpot3"]/div/div/h5[1]/b/time/text()').get()

    # Winning numbers
    winning_numbers= "Winning Numbers\n\n"
    for i in range(1,(len(sel(text=data.text).xpath('//*[@id="result-jackpot3"]/table/tbody/tr/td/p/span')))+1):
        result=sel(text=data.text).xpath('.//*[@id="result-jackpot3"]/table/tbody/tr/td/p/span'+"["+str(i)+"]"+'//text()').getall()
        result=''.join(result)
        winning_numbers+=result + "  "

    # Create Reply
    chat_reply = "<b>Latest DaMaCai 3D JackPot Draw Results on " + latest_result_date + "</b> \n\n"
    chat_reply += winning_numbers
    chat_reply += "\n\n No need check la sure never win!"

    return chat_reply

def DaMaCai4DJackPot():
    """DaMaCai4DJackPot Methods!"""

    # Connect to Source
    url='https://www.gidapp.com/lottery/malaysia/damacai'
    data=get(url)

    # Find latest Result
    latest_result_date=sel(text=data.text).xpath('.//*[@id="result-jackpot3"]/div/div/h5[1]/b/time/text()').get()

    # Winning numbers
    winning_numbers= "Winning Numbers\n\n"
    for i in range(1,(len(sel(text=data.text).xpath('//*[@id="result-jackpot3"]/table/tbody/tr/td/p/span')))+1):
        result=sel(text=data.text).xpath('.//*[@id="result-jackpot3"]/table/tbody/tr/td/p/span'+"["+str(i)+"]"+'//text()').getall()
        result=''.join(result)
        winning_numbers+=result + "  "

    # Create Reply
    chat_reply = "<b>Latest DaMaCai 3D JackPot Draw Results on " + latest_result_date + "</b> \n\n"
    chat_reply += winning_numbers
    chat_reply += "\n\n No need check la sure never win!"

    return chat_reply

def DaMaCaiDMCJackPot():
    """DaMaCaiDMCJackPot Methods!"""

    # Connect to Source
    url='https://www.gidapp.com/lottery/malaysia/damacai'
    data=get(url)

    # Find latest Result
    latest_result_date=sel(text=data.text).xpath('.//*[@id="result-jackpotdmc"]/div/div/h5[1]/b/time/text()').get()

    # Winning numbers 1
    jp1_winning_numbers= "Jackpot1 Winning Numbers\n\n"
    for i in range(1,(len(sel(text=data.text).xpath('//*[@id="result-jackpotdmc"]/table[1]/tbody/tr/td/p[1]/span')))+1):
        result=sel(text=data.text).xpath('.//*[@id="result-jackpotdmc"]/table[1]/tbody/tr/td/p[1]/span'+"["+str(i)+"]"+'//text()').getall()
        result=''.join(result)
        jp1_winning_numbers+=result + "  "

    # Winning numbers 2
    jp2_winning_numbers= "\n\nJackpot2 Winning Numbers\n\n"
    for i in range(1,(len(sel(text=data.text).xpath('//*[@id="result-jackpotdmc"]/table[2]/tbody/tr/td/p[1]/span')))+1):
        result=sel(text=data.text).xpath('.//*[@id="result-jackpotdmc"]/table[2]/tbody/tr/td/p[1]/span'+"["+str(i)+"]"+'//text()').getall()
        result=''.join(result)
        jp2_winning_numbers+=result + "  "

    # Create Reply
    chat_reply = "<b>Latest DaMaCai DMC JackPot Draw Results on " + latest_result_date + "</b> \n\n"
    chat_reply += jp1_winning_numbers
    chat_reply += jp2_winning_numbers
    chat_reply += "\n\n No need check la sure never win!"

    return chat_reply

if __name__ == "__main__":
    DaMaCai3DJackPot()
