
# /Users/gogo/dev/remote/github/Hilbert/core/parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'B816FFD9DF15C8178989CA494B365442'
    
_lr_action_items = {'VAR':([0,4,7,11,12,13,14,15,16,20,21,23,41,],[2,18,18,18,18,18,18,18,18,18,18,35,18,]),'INTE_D_DYM':([8,10,17,18,24,25,26,27,28,31,33,37,38,40,],[-14,-16,-12,-15,-9,-11,-8,-10,-7,36,-13,-4,-3,-5,]),'^':([1,2,8,10,17,18,22,24,25,26,27,28,29,31,32,33,37,38,40,42,],[12,-15,-14,-16,-12,-15,12,-9,12,-8,-10,-7,12,12,12,-13,-4,-3,-5,12,]),'-':([0,1,2,4,7,8,10,11,12,13,14,15,16,17,18,20,21,22,24,25,26,27,28,29,31,32,33,37,38,40,41,42,],[4,13,-15,4,4,-14,-16,4,4,4,4,4,4,-12,-15,4,4,13,-9,13,-8,-10,-7,13,13,13,-13,-4,-3,-5,4,13,]),'*':([1,2,8,10,17,18,22,24,25,26,27,28,29,31,32,33,37,38,40,42,],[11,-15,-14,-16,-12,-15,11,-9,11,11,-10,11,11,11,11,-13,-4,-3,-5,11,]),'/':([1,2,8,10,17,18,22,24,25,26,27,28,29,31,32,33,37,38,40,42,],[14,-15,-14,-16,-12,-15,14,-9,14,14,-10,14,14,14,14,-13,-4,-3,-5,14,]),'+':([1,2,8,10,17,18,22,24,25,26,27,28,29,31,32,33,37,38,40,42,],[15,-15,-14,-16,-12,-15,15,-9,15,-8,-10,-7,15,15,15,-13,-4,-3,-5,15,]),'NUMBER':([0,4,7,11,12,13,14,15,16,20,21,23,30,41,],[8,8,8,8,8,8,8,8,8,8,8,34,34,8,]),'DIFF_SYM':([0,4,7,11,12,13,14,15,16,20,21,41,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'(':([0,4,5,6,7,9,11,12,13,14,15,16,19,20,21,41,],[7,7,20,21,7,23,7,7,7,7,7,7,30,7,7,7,]),'$end':([1,2,3,8,10,17,18,24,25,26,27,28,29,33,37,38,40,42,],[-6,-15,0,-14,-16,-12,-15,-9,-11,-8,-10,-7,-1,-13,-4,-3,-5,-2,]),')':([8,10,17,18,22,24,25,26,27,28,32,33,34,35,36,37,38,40,],[-14,-16,-12,-15,33,-9,-11,-8,-10,-7,37,-13,38,39,40,-4,-3,-5,]),'INTE_SYM':([0,4,7,11,12,13,14,15,16,20,21,41,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'=':([2,39,],[16,41,]),'VAR_MULTI':([0,4,7,11,12,13,14,15,16,20,21,41,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'FUNC_VAR':([0,4,7,11,12,13,14,15,16,20,21,41,],[9,19,19,19,19,19,19,19,19,19,19,19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,7,11,12,13,14,15,16,20,21,41,],[1,17,22,24,25,26,27,28,29,31,32,42,]),'statement':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> VAR = expression','statement',3,'p_statement_assign','h_parser.py',21),
  ('statement -> FUNC_VAR ( VAR ) = expression','statement',6,'p_statement_def_func','h_parser.py',25),
  ('expression -> FUNC_VAR ( NUMBER )','expression',4,'p_statement_eval_func','h_parser.py',29),
  ('expression -> DIFF_SYM ( expression )','expression',4,'p_expression_diff_func','h_parser.py',34),
  ('expression -> INTE_SYM ( expression INTE_D_DYM )','expression',5,'p_expression_inte_func','h_parser.py',38),
  ('statement -> expression','statement',1,'p_statement_expr','h_parser.py',42),
  ('expression -> expression + expression','expression',3,'p_expression_binop','h_parser.py',46),
  ('expression -> expression - expression','expression',3,'p_expression_binop','h_parser.py',47),
  ('expression -> expression * expression','expression',3,'p_expression_binop','h_parser.py',48),
  ('expression -> expression / expression','expression',3,'p_expression_binop','h_parser.py',49),
  ('expression -> expression ^ expression','expression',3,'p_expression_binop','h_parser.py',50),
  ('expression -> - expression','expression',2,'p_expression_uminus','h_parser.py',58),
  ('expression -> ( expression )','expression',3,'p_expression_group','h_parser.py',62),
  ('expression -> NUMBER','expression',1,'p_expression_number','h_parser.py',66),
  ('expression -> VAR','expression',1,'p_expression_var','h_parser.py',70),
  ('expression -> VAR_MULTI','expression',1,'p_expression_var_multi','h_parser.py',74),
]