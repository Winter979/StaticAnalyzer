
from enum import Enum,auto

COLOURS={
   "reset"  : "\033[0;0m",
   "black"  : "\033[1;30m",
   "red"    : "\033[1;31m",
   "green"  : "\033[1;32m",
   "yellow" : "\033[1;33m",
   "blue"   : "\033[1;34m",
   "purple" : "\033[1;35m",
   "cyan"   : "\033[1;36m",
   "white"  : "\033[1;37m",
}

class Kind(Enum):
   TOP = auto()
   FUNCTION = auto()
   VARIABLE = auto()

   LOOP = auto()
   
   BREAK = auto()
   CONTINUE = auto()
   IF = auto()
   RETURN = auto()
   GOTO = auto()
   SWITCH = auto()
   CASE = auto()
   LABEL = auto()
   FUNC_CALL = auto()
   USE_CHILDREN = auto()
   UNKNOWN = auto()
   IGNORE = auto()

   PAREN = auto()
   STMT = auto()
   UNARY = auto()
   BINARY_OPERATOR = auto()
   NULL = auto()

class Node:
   parent = None
   children = []
   kind = Kind.UNKNOWN
   # location = None
   raw = None

class Curse:
   node = None
   message = ""
   function = None

   def __init__(self, node, message, function):
      self.node = node
      self.message = message
      self.function = function

