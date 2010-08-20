#!/usr/bin/env python
#coding=utf-8
#filename pythontemplate.py
class DictionaryTemplate:
    def __init__(self, dict={}, **keywords):
        self.dict = dict
        self.dict.update(keywords)

    def __str__(self):
        return self._template % self

    def __getitem__(self, key):
            return self._process(key.split("|"))

    def _process(self, l):
        arg = l[0]
        if len(l) == 1:
            if arg in self.dict:
                return self.dict[arg]
            elif hasattr(self, arg) and callable(getattr(self, arg)):
                return getattr(self, arg)()
            else:
                raise KeyError(arg)
        else:
            func_name = l[1]
            if func_name in self.dict:
                func = self.dict[func_name]
            else:
                func = getattr(self, func_name)
            return func(self._process([arg]))

class ListTemplate:

    def __init__(self, input_list=[]):
        self.input_list = input_list

    def __str__(self):
        return "\n".join([self._template % x for x in self.input_list])

class IntervieweeList_Template(DictionaryTemplate):
    _template = """
      <div>
        <h1>Articles</h1>
        %(lst|li)s
      </div>"""

class Interviewee_Template(ListTemplate):
    _template = """
        <div>
          <h2>%(heading)s</h2>
          <p class="date">%(date)s</p>
          <p>%(abstract)s</p>
          <p><a href="%(link)s">Link</a></p>
        </div>"""