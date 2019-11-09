import javalang
import javac_parser

from stuff import *


def parse(filename):
   tree = javalang.parse.parse(open(filename).read())

   head = tree.types[0]

   recurse(head)

def recurse(node, padding=""):

   ignore = [
      javalang.tree.StatementExpression,
      javalang.tree.Assignment,
      javalang.tree.Literal,
      javalang.tree.BlockStatement,
      javalang.tree.BinaryOperation,
      javalang.tree.MemberReference,
      tuple
   ]

   end = [
      javalang.tree.LocalVariableDeclaration,
      javalang.tree.ReturnStatement,
   ]

   if type(node) == tuple or type(node) == list:
      for n in node:
         if type(n) not in ignore:
            # recurse(n, padding+"--")
            print(padding, type(n))
      return

   if type(node) in ignore:
      return
   
   print(padding, type(node))
   
   tn = type(node)

   try:

      if tn in end:
         # Nothing needs to be done
         pass 
      elif tn == javalang.tree.IfStatement:
         # print(type(node.then_statement))
         recurse(node.then_statement,padding+"  ")
      elif tn == javalang.tree.SwitchStatement:
         for c in node.cases:
            recurse(c.statements, padding+"  ")
      else:
         for c in node.body:
            recurse(c, padding+"  ")
   except AttributeError:
      print(padding, "-----")
      
   # body = [
   #    javalang.tree.ClassDeclaration,
   #    javalang.tree.MethodDeclaration,
   # ]

   # statements = [
   #    javalang.tree.WhileStatement,
   # ]

   # t = type(node)

   # if t in body:
   #    for c in node.body:
   #       recurse(c, padding+"  ")
   # elif t in statements:
   #    for c in node.body.statements:
   #       recurse(c, padding+"  ")
   # elif t == javalang.tree.IfStatement:
   #    for c in node.then_statement:
   #       recurse(c, padding+"  ")
   # elif t == tuple:
   #    for c in node:
   #       recurse(c, padding+"  ")
      # print(padding, type(node.body.statements[0]))

   # try:
   #    for c in node.body:
   #       recurse(c, padding+"  ")
   # except AttributeError:
   #    if type(node) == javalang.tree.IfStatement:
   #       recurse(node.then_statement,padding+"  ")
   #    elif type(node) == javalang.tree.BlockStatement:
   #       # pass
   #       recurse(node.statements,padding+"  ")
   #    elif type(node) == tuple:
   #       for c in node:
   #          recurse(c,padding+"  ")
   #    elif type(node) == list:
   #       for c in node:
   #          recurse(c,padding+"  ")
   #    else:
   #       print(padding, "="*20)

