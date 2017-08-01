# coding:utf-8
#如果输入一个句子，该函数会将句子拆成很多个单词
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

#对拆解后的单词排序
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#打印出原始句子的第一个单词
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

#打印出原始句子的最后一个单词
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

#获取一个完整的句子然后返回排序后的单词
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

#打印出句子首位两个单词
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#打印出排序后句子首位两个单词
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 - 3
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


started = 10000
beans, jars, crates = secret_formula(started)

print "With a starting point of: %d" % started
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

started = started / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(started)

#需要引用第25个练习代码，才能完成后面的内容，且引用后会直接在终端显示结果，
#无需像上面的内容要在终端中输入代码再打印
import ex25

sentence = "All good\tthings come to those who wait."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
