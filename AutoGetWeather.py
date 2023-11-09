import os
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# auto email
def send_email(content):
    mail_host = "smtp.qq.com"  # 填写邮箱服务器:这个是qq邮箱服务器，直接使用smtp.qq.com
    mail_pass = 'chlzwavkcodtbfge'  # 填写在qq邮箱设置中获取的授权码
    sender = '943649026@qq.com'  # 填写邮箱地址
    receivers = ['18761099420@163.com']  # 填写收件人的邮箱，QQ邮箱或者其他邮箱，可多个，中间用,隔开

    subject = 'AutoWeather'  #发送的主题
        
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    message['From'] = Header("William_from_github <943649026@qq.com>")  # 'utf-8'  #邮件发送者姓名 
    message['To'] = Header("William")    #邮件接收者姓名


    smtpObj = smtplib.SMTP_SSL(mail_host, 465) #建立smtp连接，qq邮箱必须用ssl边接，因此边接465端口
    smtpObj.login(sender, mail_pass)  #登陆
    smtpObj.sendmail(sender, receivers, message.as_string())  #发送
    smtpObj.quit()


if __name__ == '__main__':
    # updata time in the repo
    with open('log.txt','w+') as f:
        f.write('AutoWeather time log: '+ str(time.asctime( time.localtime(time.time()) )))
    
    # send email
    send_email('Test of AutoGetWeather')