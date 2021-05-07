class Chart:
def	init	(self, rows):
'''An Earley chart is a list of rows for every input word''' self.rows = rows

def		len	(self): '''Chart length''' return len(self.rows)

def	repr	(self):
'''Nice string representation''' st = '<Chart>\n\t'
st+= '\n\t'.join(str(r) for r in self.rows) st+= '\n</Chart>'
return st

def add_row(self, row):
 
'''Add a row to chart, only if wasn't already there''' if not row in self.rows:
self.rows.append(row)

class ChartRow:
def	init	(self, rule, dot=0, start=0, previous=None, completing=None):
'''Initialize a chart row, consisting of a rule, a position index inside the rule, index of starting chart and pointers to parent rows'''
self.rule = rule self.dot = dot self.start = start
self.completing = completing self.previous = previous

def	len	(self):
'''A chart's length is its rule's length''' return len(self.rule)

def	repr	(self):
'''Nice string representation:
<Row <LHS -> RHS .> [start]>'''
rhs = list(self.rule.rhs) rhs.insert(self.dot, '.')
rule_str = "[{0} -> {1}]".format(self.rule.lhs, ' '.join(rhs)) return "<Row {0} [{1}]>".format(rule_str, self.start)

def	cmp	(self, other):
'''Two rows are equal if they share the same rule, start and
 
dot'''
 

if len(self) == len(other): if self.dot == other.dot:
if self.start == other.start: if self.rule == other.rule:
return 0
 
return 1

def is_complete(self):
'''Returns true if rule was completely parsed, i.e. the dot is at the end'''
return len(self) == self.dot def next_category(self):
 

dot'''
 
'''Return next category to parse, i.e. the one after the

if self.dot < len(self): return self.rule[self.dot]
return None
 

def prev_category(self):
'''Returns last parsed category''' if self.dot > 0:
return self.rule[self.dot-1] return None
