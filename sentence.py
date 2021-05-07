# -*- encoding: utf-8 -*- import re

class Word:
def		init	(self, word = '', tags = []): '''Initialize a word with a list of tags''' self.word = word
self.tags = tags

def	str	(self):
'''Nice string representation'''
return "{0}<{1}>".format(self.word, ','.join(self.tags))

class Sentence:
def	init	(self, words = []):
'''A sentence is a list of words''' self.words = words

def	str	(self):
'''Nice string representation'''
return ' '.join(str(w) for w in self.words)

def		len	(self): '''Sentence's length''' return len(self.words)

def	getitem	(self, index):
'''Return a word of a given index''' if index >= 0 and index < len(self):
return self.words[index] else:
return None

def add_word(self, word): '''Add word to sentence''' self.words.append(word)
 
@staticmethod
def from_string(text):
'''Create a Sentence object from a given string in the Apertium
stream format:
time/time<N> flies/flies<N>/flies<V> like/like<P>/like<V>
an/an<D> arrow/arrow<N>'''
#TODO handle Apertium format's beginning ^ and ending $
 
symbols
 


# prepare regular expressions to find word and tags lemmarex = re.compile('^[^\/]*')
tagsrex = re.compile('\/[^\<]*\<([^\>]*)\>')

sentence = Sentence()
words = text.strip().split(' ') for word in words:
lemma = lemmarex.match(word).group(0) tags = tagsrex.findall(word)
w = Word(lemma, tags) sentence.add_word(w)

return sentence
 

