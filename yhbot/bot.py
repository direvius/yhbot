#!/usr/bin/python
# -*- coding: utf-8 -*-
from jabberbot import JabberBot
from jabberbot import botcmd


class YHBot(JabberBot):
    @botcmd
    def echo(self, mess, args):
        return 'mess: %s, args: %s' % (mess, args,)

    def unknown_command(self, mess, cmd, args):
        return u'Вы сказали: %s' % mess


def main():
    username = 'yhbot@jabber.ru'
    password = 'uq0Pb2Frl'
    bot = YHBot(username, password)
    bot.serve_forever()
