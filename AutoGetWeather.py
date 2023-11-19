import os
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
from bs4 import BeautifulSoup


# define the function to get weather of nanjing, china
def get_weather():
    # city code
    url = 'https://tianqi.2345.com/jiangning2d/70447.htm'
    r = requests.get(url)
    r.encoding = 'utf-8'
    bs = BeautifulSoup(r.text, 'html.parser')
    data_tommorrow = bs.find_all('div', class_='real-mess')[0]
    # Extracting the weather information
    date_info = data_tommorrow.find('p', {'class': 'real-wea-info'}).text
    temperature = data_tommorrow.find('span', {'class': 'real-t'}).text
    air_quality = data_tommorrow.find('span', {'class': 'real-rank'}).text
    date, tomorrow_weather = data_tommorrow.find('div', {'class': 'real-today'}).text.split("：")
    wind_info = data_tommorrow.find('em', {'class': 'wea-info-wind'}).parent.text
    humidity_info = data_tommorrow.find('em', {'class': 'wea-info-humidity'}).parent.text
    uv_info = data_tommorrow.find('em', {'class': 'wea-info-sunblack'}).parent.text
    pressure_info = data_tommorrow.find('em', {'class': 'wea-info-pa'}).parent.text

    # organize context
    content = f"Date Info: {date} {date_info}\nTomorrow's Weather: {tomorrow_weather}\nAVG Temperature: {temperature}\nAir Quality: {air_quality}\n\Wind Info: {wind_info}\nHumidity Info: {humidity_info}\nUV Info: {uv_info}\nPressure Info: {pressure_info}\n"
    #print(context)
    return content

# auto email
def send_email(content):
    mail_host = "smtp.qq.com"  # 填写邮箱服务器:这个是qq邮箱服务器，直接使用smtp.qq.com
    mail_pass = 'chlzwavkcodtbfge'  # 填写在qq邮箱设置中获取的授权码
    sender = '943649026@qq.com'  # 填写邮箱地址
    receivers = ['18761099420@163.com','1270142056@qq.com']  # 填写收件人的邮箱，QQ邮箱或者其他邮箱，可多个，中间用,隔开

    subject = 'AutoWeather'  #发送的主题
        
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    message['From'] = Header("William_from_github <943649026@qq.com>")  # 'utf-8'  #邮件发送者姓名 
    message['To'] = Header("Weather Info")    #邮件接收者姓名


    smtpObj = smtplib.SMTP_SSL(mail_host, 465) #建立smtp连接，qq邮箱必须用ssl边接，因此边接465端口
    smtpObj.login(sender, mail_pass)  #登陆
    smtpObj.sendmail(sender, receivers, message.as_string())  #发送
    smtpObj.quit()


if __name__ == '__main__':
    # get weather
    context = get_weather()
    # send email
    send_email(context)
    # updata time in the repo
    with open('log.txt','w+') as f:
        f.write('AutoWeather time log: '+ str(time.asctime( time.localtime(time.time()) )))