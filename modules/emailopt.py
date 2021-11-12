# -*- coding: utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


class EmailOpt:
    __info_dict = dict()

    def __init__(self, u_name, u_pwd):
        self.__context = ""
        self.__info_dict["email_addr"] = u_name
        self.__info_dict["email_pwd"] = u_pwd
        self.__info_dict["qq_smtp"] = "smtp.qq.com"
        self.__info_dict.setdefault("destination", "")
        self.__info_dict.setdefault("send_data", None)

    def set_send_data(self, element):
        self.__context = str(element)
        data = MIMEText(self.__context, 'plain', 'utf-8')
        self.__info_dict["send_data"] = data

    def set_destination_info(self, destination):
        self.__info_dict["destination"] = destination

    def set_header_info(self, element):
        self.__info_dict["email_header"] = element

    @staticmethod
    def _format_address(element):
        name, address = parseaddr(element)
        return formataddr((Header(name, 'utf-8').encode(), address))

    def _build_email_format(self):
        if not self.__context:
            raise ValueError("邮件内容为空，请编辑邮件内容！")

        self.__info_dict["send_data"]['From'] = \
            self._format_address(u'<%s>' % self.__info_dict["email_addr"])
        self.__info_dict["send_data"]['To'] = \
            self._format_address(u'<%s>' % self.__info_dict["destination"])
        self.__info_dict["send_data"]['Subject'] = \
            Header(u'%s' % self.__info_dict["email_header"], 'utf-8').encode()

    def send_email(self):
        try:
            server = smtplib.SMTP_SSL(self.__info_dict["qq_smtp"], 465)
            # server.set_debuglevel(1)
            server.login(self.__info_dict["email_addr"], self.__info_dict["email_pwd"])
            self._build_email_format()
            server.sendmail(self.__info_dict["email_addr"],
                            self.__info_dict["destination"],
                            self.__info_dict["send_data"].as_string())
            server.quit()
        except smtplib.SMTPAuthenticationError as e:
            print("鉴权失败，请查看邮箱账号和密码是否正确...\n", e.args)
            return False
        except ValueError as e:
            print(e.args)
            return False

        return True
