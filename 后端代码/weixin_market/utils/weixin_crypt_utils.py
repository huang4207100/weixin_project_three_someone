# -*- coding: utf-8 -*-

'''
微信的加解密接口
'''

from .wx_crypy import WXBizMsgCrypt as wxMsgCrypt


'''
微信pgp加密/解密工具类
'''

class WeiXinCryptUtil:
    def __init__(self, token, key, component_appid):
        self.token = token
        self.key = key
        self.component_appid = component_appid
        pass

    def __del__(self):
        pass

    '''
    pgp加密，第三方平台回复加密消息给公众平台；
    '''

    def encrypt_msg(self, decryp_xml, nonce):
        # 测试加密接口
        wx_biz_msg_crypt = wxMsgCrypt.WXBizMsgCrypt(self.token, self.key, self.component_appid)
        ret, encrypt_xml = wx_biz_msg_crypt.EncryptMsg(decryp_xml, nonce)
        return ret, encrypt_xml

    '''
    pgp解密，第三方平台收到公众平台发送的消息，验证消息的安全性，并对消息进行解密。
    '''

    def decrypt_msg(self, encrypt_xml, msg_sign, timestamp, nonce):
        wx_biz_msg_crypt = wxMsgCrypt.WXBizMsgCrypt(self.token, self.key, self.component_appid)
        ret, decryp_xml = wx_biz_msg_crypt.DecryptMsg(encrypt_xml, msg_sign, timestamp, nonce)
        return ret, decryp_xml





