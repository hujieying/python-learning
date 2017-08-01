# _*_ coding:utf-8 _*_
from sys import argv

script, user_name = argv
prompt = "你的回答是："
prompt2 = ">"

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "你喜欢我吗， %s?" % user_name
likes = raw_input(prompt)

print "你住在哪里呢， %s?" % user_name
lives = raw_input(prompt2)

print "你用的是什么电脑?"
computer = raw_input(prompt2)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)