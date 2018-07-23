# encoding: utf-8
import itchat

itchat.auto_login(hotReload=True)

# users = itchat.search_friends(name="A媳妇")
# print(users)

account=itchat.get_friends()
# #获取自己的UserName
userName = account[0]['UserName']
print(userName)

