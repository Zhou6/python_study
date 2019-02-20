# coding=utf-8
import itchat
from itchat.content import TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO

BUSY_MSG = '现在有事，稍后联系(此条自动回复)'.decode('u8')
BUSY = False
TO_USER_NAME = ''


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print msg.User.NickName, msg.User.RemarkName, msg.type, msg.text, msg
    name = msg.User.RemarkName if msg.User.RemarkName else msg.User.NickName
    callback = itchat.send('%s:%s' % (name, msg.text), TO_USER_NAME)
    print 'callback', callback
    if BUSY:
        return BUSY_MSG
    else:
        return None


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def map_reply(msg):
    print msg.User.NickName, msg.User.RemarkName, msg.type, msg.text, msg
    name = msg.User.RemarkName if msg.User.RemarkName else msg.User.NickName
    msg.download(msg.fileName)
    typeSymbol = {PICTURE: 'img', VIDEO: 'vid', }.get(msg.type, 'fil')
    callback = itchat.send('%s:%s:%s' % (name, typeSymbol, msg.fileName), TO_USER_NAME)
    print 'callback', callback
    if BUSY:
        return BUSY_MSG
    else:
        return None


@itchat.msg_register(itchat.content.FRIENDS)
def map_reply(msg):
    print msg.User.NickName, msg.User.RemarkName, msg.type, msg.text, msg
    name = msg.User.RemarkName if msg.User.RemarkName else msg.User.NickName
    callback = itchat.send('%s:%s' % (name, msg.text), TO_USER_NAME)
    print 'callback', callback
    # if BUSY:
    #     return BUSY_MSG
    # else:
    return None


@itchat.msg_register(itchat.content.SYSTEM)
def map_reply(msg):
    print msg.type, msg
    # name = msg.User.RemarkName if msg.User.RemarkName else msg.User.NickName
    callback = itchat.send('%s:%s' % (u'系统', msg.text), TO_USER_NAME)
    print 'callback', callback
    return None


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print msg.type, msg
    name = msg.User.RemarkName if msg.User.RemarkName else msg.User.NickName
    callback = itchat.send('%s:%s' % (name, msg.text), TO_USER_NAME)
    print 'callback', callback
    if msg.isAt:
        msg.user.send(u'@%s  received: %s' % (
            msg.type, msg.text))


def lcb():
    print '上线'
    # callback = itchat.send(u'关联用户上线', TO_USER_NAME)
    # print 'callback', callback


def ecb():
    print '下线', TO_USER_NAME
    callback = itchat.send(u'关联用户下线', TO_USER_NAME)
    print 'callback', callback


itchat.auto_login(hotReload=True, enableCmdQR=False, loginCallback=lcb, exitCallback=ecb)
friends = itchat.search_friends(nickName=u'周六')
for friend in friends:
    if friend.get('IsOwner', 1) == 0:
        TO_USER_NAME = friend.UserName
if not TO_USER_NAME:
    print 'exit, no to_user_name'
    exit()
print 'to_user_name', TO_USER_NAME
callback = itchat.send(u'关联用户上线', TO_USER_NAME)
print 'callback', callback
itchat.run()