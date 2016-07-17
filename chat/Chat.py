from __future__ import print_function

import re
import random


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

class Chat(object):
    def __init__(self, pairs, reflections={}):
 
        self.pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
        self.reflections = reflections
        self.regex = self.compile_reflections()
    def compile_reflections(self):
        sorted_refl = sorted(self.reflections.keys(), key=len,
                reverse=True)
        return  re.compile(r"\b({0})\b".format("|".join(map(re.escape,
            sorted_refl))), re.IGNORECASE)
    def substitute(self, str):
        return self._regex.sub(lambda mo:
                self.reflections[mo.string[mo.start():mo.end()]],
                    str.lower())
    def wildcards(self, response, match):
        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos+1:pos+2])
            response = response[:pos] + \
                self.substitute(match.group(num)) + \
                response[pos+2:]
            pos = response.find('%')
        return response
    def respond(self, str):
        for (pattern, response) in self.pairs:
            match = pattern.match(str)
            if match:
                resp = random.choice(response)  
                resp = self.wildcards(resp, match) 
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

    def converse(self, a):
        b = self.respond(a)
        return b
