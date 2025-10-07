from pymol import cmd

my_list = cmd.get_object_list('*')
for str in my_list:
    cmd.dist("%s_polar_conts" %(str),
             "(%s)" %(str),
             "(%s) & sc." %(str),
             quiet=1,mode=2,label=0,reset=1)
    cmd.enable("%s_polar_conts" %(str))
