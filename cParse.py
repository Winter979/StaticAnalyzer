import sys
import clang.cindex as cl
from ctypes.util import find_library

from stuff import *

if sys.platform.startswith("darwin"):
   cl.Config.set_library_file("/Library/Developer/CommandLineTools/usr/lib/libclang.dylib")
elif sys.platform.startswith("linux"):
   cl.Config.set_library_file("/usr/lib/llvm-6.0/lib/libclang.so")

KIND_MAP = {
   cl.CursorKind.FOR_STMT              : Kind.LOOP,
   cl.CursorKind.TRANSLATION_UNIT      : Kind.TOP,
   cl.CursorKind.VAR_DECL              : Kind.VARIABLE,
   cl.CursorKind.FUNCTION_DECL         : Kind.FUNCTION,
   cl.CursorKind.COMPOUND_STMT         : Kind.USE_CHILDREN,
   cl.CursorKind.DECL_STMT             : Kind.VARIABLE,
   cl.CursorKind.IF_STMT               : Kind.IF,
   cl.CursorKind.GOTO_STMT             : Kind.GOTO,
   cl.CursorKind.LABEL_REF             : Kind.GOTO,
   cl.CursorKind.LABEL_STMT            : Kind.LABEL,
   cl.CursorKind.CASE_STMT             : Kind.CASE,
   cl.CursorKind.DEFAULT_STMT          : Kind.CASE,
   cl.CursorKind.SWITCH_STMT           : Kind.SWITCH,
   cl.CursorKind.WHILE_STMT            : Kind.LOOP,
   cl.CursorKind.RETURN_STMT           : Kind.RETURN,
   cl.CursorKind.BREAK_STMT            : Kind.BREAK,
   cl.CursorKind.CONTINUE_STMT         : Kind.CONTINUE,
   cl.CursorKind.CALL_EXPR             : Kind.FUNC_CALL,
   cl.CursorKind.DO_STMT               : Kind.LOOP,
   cl.CursorKind.NULL_STMT             : Kind.NULL,
   cl.CursorKind.BINARY_OPERATOR       : Kind.BINARY_OPERATOR,
   cl.CursorKind.UNARY_OPERATOR        : Kind.UNARY,
   cl.CursorKind.StmtExpr              : Kind.STMT,
   cl.CursorKind.PAREN_EXPR            : Kind.PAREN,

   cl.CursorKind.PARM_DECL             : Kind.IGNORE,
   cl.CursorKind.ENUM_DECL             : Kind.IGNORE,
   cl.CursorKind.UNEXPOSED_EXPR        : Kind.IGNORE,
   cl.CursorKind.INTEGER_LITERAL       : Kind.IGNORE,
   cl.CursorKind.FLOATING_LITERAL      : Kind.IGNORE,
   cl.CursorKind.CHARACTER_LITERAL     : Kind.IGNORE,
   cl.CursorKind.INIT_LIST_EXPR        : Kind.IGNORE,
   cl.CursorKind.CSTYLE_CAST_EXPR      : Kind.IGNORE,
   cl.CursorKind.ARRAY_SUBSCRIPT_EXPR  : Kind.IGNORE,
   cl.CursorKind.CXX_UNARY_EXPR        : Kind.IGNORE,
   cl.CursorKind.CONDITIONAL_OPERATOR  : Kind.IGNORE,
   cl.CursorKind.STRING_LITERAL        : Kind.IGNORE,
   cl.CursorKind.DECL_REF_EXPR         : Kind.IGNORE,
   cl.CursorKind.STRUCT_DECL           : Kind.IGNORE,
   cl.CursorKind.TYPEDEF_DECL          : Kind.IGNORE,
   cl.CursorKind.TYPE_REF              : Kind.IGNORE,
   cl.CursorKind.MEMBER_REF_EXPR       : Kind.IGNORE,

   cl.CursorKind.COMPOUND_ASSIGNMENT_OPERATOR  : Kind.IGNORE,
}

def parse(filename):
   try:
      index = cl.Index.create()
      tu = index.parse(filename)
      tree = recurse(tu.cursor, None, filename)
      return tree
   except cl.TranslationUnitLoadError:
      return None

def recurse(cursor, parent, filename):

   if cursor.location.file is not None and str(cursor.location.file) != filename:
      return None

   # if str(cursor.location.file).startswith("/usr/"):
   #    return None

   # if str(cursor.location.file).endswith(".h"):
   #    return None

   try:
      kind = KIND_MAP[cursor.kind]
   except KeyError:
      print(cursor.kind, cursor.location)
      return None

   if kind == Kind.IGNORE:
      return None

   children = []

   node = Node()
   node.parent = parent
   node.raw = cursor
   node.kind = kind

   node.spelling = cursor.spelling if cursor.spelling is not "" else None


   for c in cursor.get_children():
      child = recurse(c,node, filename)
      if child is not None:
         if child.kind == Kind.USE_CHILDREN:
            children.extend(child.children)
         else:
            children.append(child)

   if len(children) == 1 and node.kind == children[0].kind:
      node = children[0]
   else:
      node.children = children

   return node
