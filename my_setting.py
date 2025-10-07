import pymol
from pymol import cmd
#import commands
def V1():
	cmd.do('viewport 800, 800')
	cmd.do('set specular, 0')
	cmd.do('set ray_shadow, off')
	cmd.do('set valence, off')
	cmd.do('set antialias, 2')
	cmd.do('set ray_trace_mode, 1')
	cmd.do('set ray_trace_disco_factor, 1')
	cmd.do('set ray_trace_gain, 0.1')
	cmd.do('set power, 0.2')
	cmd.do('set ambient, 0.4')
	cmd.do('set ray_trace_color, gray30')
	cmd.do('set cartoon_sampling,10')
	cmd.do('set cartoon_discrete_colors, on')
	
def V2():
	cmd.do('viewport 800, 800')
	cmd.do('set cartoon_loop_radius, 0.4')
	cmd.do('set ray_trace_mode, 1')
	cmd.do('set ray_shadows,0')
	cmd.do('set specular, 0')
	cmd.do('space cmyk')
	cmd.do('set ray_trace_color, [0,0,0]')
	
def V3():
	cmd.do('viewport 800, 800')
	cmd.do('set specular, 0')
	cmd.do('set ray_shadow, off')
	cmd.do('set antialias, 2')
	cmd.do('set ray_trace_mode, 1')
	cmd.do('set ray_trace_disco_factor, 1')
	cmd.do('set ray_trace_gain, 0.1')
	cmd.do('set power, 0.2')
	cmd.do('set ambient, 0.4')
	cmd.do('set direct, 0.45')
	cmd.do('set cartoon_sampling, 10')
	cmd.do('set ray_trace_color, black')
	cmd.do('set line_width, 3')
	cmd.do('set cartoon_transparency, 0')
	cmd.do('set cartoon_flat_sheets, off')

def V4():
    #cmd.do('# Basic display settings')
    cmd.do('set cartoon_loop_radius, 0.4')
    cmd.do('set cartoon_sampling, 10')
    cmd.do('set cartoon_transparency, 0')
    cmd.do('set line_width, 3')

    #cmd.do('# Ray tracing settings')
    cmd.do('set ray_trace_mode, 1')
    cmd.do('set ray_shadows, 0')
    cmd.do('set ray_trace_gain, 0.1')
    cmd.do('set ray_trace_disco_factor, 1')
    cmd.do('set ray_trace_color, black')

    #cmd.do('# Lighting and material settings')
    cmd.do('set antialias, 2')
    cmd.do('set specular, 0')
    cmd.do('set power, 0.2')
    cmd.do('set ambient, 0.4')
    cmd.do('set direct, 0.45')
    cmd.do('set valence, 0')


def V5():
	cmd.do('viewport 800, 800')
	cmd.do('bg_color white')
	cmd.do('set orthoscopic, 1')
	cmd.do('set two_sided_lighting, 1')
	cmd.do('set antialias, 1')
	cmd.do('set ray_shadows, 0')
	cmd.do('set ray_trace_mode, 1')

def ligand01():
	cmd.do('show sticks')
	cmd.do('set ray_opaque_background, off')
	cmd.do('set stick_radius, 0.11')
	cmd.do('show spheres')
	cmd.do('set sphere_scale, 0.2, all')
	cmd.do('set sphere_scale, 0.12, elem H')
	cmd.do('color good_lightblue, elem C')
	cmd.do('color good_red, elem O')
	cmd.do('set sphere_quality, 200')
	cmd.do('set stick_quality, 200')
	cmd.do('set sphere_transparency, 0')
	cmd.do('set stick_transparency, 0')
	cmd.do('set ray_shadow, on')
	cmd.do('set orthoscopic, 1')
	cmd.do('set antialias, 2')
	cmd.do('set specular, 0')
	cmd.do('set ray_shadow, on')
	cmd.do('set ray_trace_color, black')
	cmd.do('set line_width, 4')
	#cmd.do('ray 1024,768'


def show_residues(object1, ligand):  #show_residues("7epf","resn J9U")
	cmd.do('bg_color white')
	cmd.do('hide solvent')
	cmd.do('set cartoon_fancy_helices')
	cmd.do('set cartoon_color, hydrogen')
	cmd.do('set cartoon_transparency, 0.6')
	cmd.do(f'util.cbag {object1} and {ligand}')
		
	cmd.do(f'select bs, {object1} and byres name CA within 6 of {ligand}')
	cmd.do('show sticks, bs') 
	cmd.do(f'hide {object1} and hydro)"')
	cmd.do('util.cbay bs')
	cmd.do('orient bs')
	cmd.do('deselect')
	cmd.do('set ray_trace_mode, 1')




### Define custom colors
cmd.set_color('limegreen', [ 0.00, 238.00, 0.00])
cmd.set_color('blauw', [ 0.00, 191.00, 255.00])
cmd.set_color('goud',[ 255.00, 193.00, 37.00])
cmd.set_color('blauw2',[ 30, 144,255])
cmd.set_color('blauw3',[ 0, 154, 205])
cmd.set_color('crimson',[ 220, 20, 60])
cmd.set_color('indianred',[ 176, 23, 31])
cmd.set_color('cadmiumorange',[ 255, 97, 3])
cmd.set_color('orangered1', [ 255, 69, 0])
cmd.set_color('palecyan1',[ 180, 255, 255])
cmd.set_color('palecyan2',[ 166, 255, 255])
cmd.set_color('red', [ 238, 64, 0])


good_models = []
temp = []

### Globals for object_focus function
UP, DOWN = -1, 1
in_focus = 0

def separate_by_chain(pdb):
    """
    Extract each chain of pdb as separate object.
    """
    for i in cmd.get_chains(pdb):
        cmd.extract(pdb+'_'+i, 'chain '+i+' and '+pdb)
    cmd.delete(pdb)

def starting_view():
    cmd.hide("all")
    cmd.show('cartoon')
    cmd.show('lines')
    cmd.show("sticks")
    cmd.set("stick_radius", 0.1)
    cmd.hide('(h.)')
    cmd.bg_color('black')
    cmd.set('dash_color', 'yellow')
    #util.color_chains("(all and elem c)",_self=cmd)
    cmd.color('goud', 'chain A')
    cmd.color('white', 'chain C')
    cmd.color('splitpea', 'chain B')
    cmd.color('blauw3', 'chain D')
    cmd.color('cadmiumorange', 'chain E')
    cmd.color('palecyan', 'chain F')
    util.cnc("all")
    cmd.set('cartoon_oval_length',1.15)
    cmd.set('cartoon_oval_width',0.35)
    cmd.set('specular',0)
    cmd.set('surface_quality',1)
    #cmd.set('ambient_occlusion_mode', 1)
    cmd.set('cartoon_transparency', 0.2)
    cmd.remove('solvent')
    cmd.show('spheres','name OXT')
    cmd.set('cartoon_highlight_color','gray60')


def save_seperate(prefix=''):
    """
    from PyMOL wiki
    save_separate <prefix>
    saves multiple objects into multiple files using an optional prefix name.
    """
    obj_list = cmd.get_names("all")

    if obj_list:
        for i in range(len(obj_list)):
            obj_name = "%s%s.pdb" % (prefix, obj_list[i])
            cmd.save(obj_name, obj_list[i])
            print("Saving %s" %  obj_name)
    else:
        print("No objects found")


def object_focus(direction):
    """
    Viewing script, half code is from pymolwiki. Scroll to next obj by pressing F2
    and prev with F1.
    If present in pdb file, it will print RIF residues to pymol shell and make/layout
    selection of RIF resi.
    Will print certain metrics to pymol shell if present in pdb.
    Center on selection using this command in shell: center = 'selection'
    Keep model visualized at all time: fix = 'objname'
    """
    global in_focus, UP, DOWN,temp
    cmd.wizard()
    names = cmd.get_names("public_objects")
    in_focus += direction

    if in_focus<0:
        in_focus = 0
    if in_focus > len(names)-1:
        in_focus = len(names)-1

    cur_obj = names[in_focus]
    cmd.zoom(cur_obj, animate=0)
    cmd.wizard("message", "Object: %s" % (cur_obj))
    cmd.disable('all')
    cmd.enable(cur_obj)
    commands.getoutput('echo '+cur_obj+' | pbcopy')


    try:
        # In pymol shell type: interpolar=True
        inter_hbonds = interpolar
        if inter_hbonds:
            util.interchain_distances(cur_obj+"_interchain_polar",cur_obj,mode=2)
            cmd.dist(cur_obj+"_sc_bb_polar_conts",cur_obj,cur_obj+" & !bb.",quiet=1,mode=2,label=0,reset=1)
            cmd.enable(cur_obj+"_sc_bb_polar_conts")
    except:
        pass
    else:
        pass

    try:
        # In pymol shell type: intrapolar=True
        intra_hbonds = intrapolar
        if intra_hbonds:
            cmd.dist(cur_obj+"_polar_conts",cur_obj+" & bb.",cur_obj+" & bb.",quiet=1,mode=2,label=0,reset=1)
            cmd.enable(cur_obj+"_polar_conts")
    except:
        pass
    else:
        pass

    try:
        # In pymol shell type: center = 'selection_name'
        x = center
        cmd.center(x)
        cmd.zoom(center,20)
    except:
        pass
    else:
        pass

    try:
        # In pymol shell type: fix = 'object_name'
        y = fix
        cmd.enable(y)
    except:
        pass
    else:
        pass

    ### Read metrics and rifresidues from pdb and print to pymol shell
    try:
        rifres = []
        with open(cur_obj+'.pdb', 'r') as f:
            RIF=False
            for line in f.readlines():
                if 'cavity_volume' in line:
                    print(line.rstrip())
                if 'ddg ' in line:
                    print(line.rstrip())
                if 'ddg_per_1000sasa ' in line:
                    print(line.rstrip())
                if 'ddg_fa_atr_norepack_per_1000sasa' in line:
                    print(line.rstrip())
                if 'DISULFIDIZE' in line:
                    print(line.rstrip())
                if 'interface_sc ' in line:
                    print(line.rstrip())
                if 'interface_buried_sasa' in line:
                    print(line.rstrip())
                if 'interface_unsat_hbond2' in line:
                    print(line.rstrip())
                if 'packable' in line:
                    print(line.rstrip())
                if 'pack_stat' in line:
                    print(line.rstrip())
                if 'RIFRES' in line:
                    RIF=True
                    rifres.append(line.split()[2])
            if RIF:
                print('RIFRES: '+str(rifres))
                sele = '+'.join(rifres)
                cmd.select('RIF_'+cur_obj,'resi '+sele+' and chain A and '+cur_obj)
                cmd.center('RIF_'+cur_obj)
                cmd.zoom('RIF_'+cur_obj,17.5)
                cmd.show('sticks','RIF_'+cur_obj)
                cmd.set('stick_radius', 0.25, 'RIF_'+cur_obj)
                cmd.hide("(all and hydro)")
                util.cba(6,"RIF_"+cur_obj, _self=cmd)
                cmd.disable('RIF_'+cur_obj)

    except:
        pass
    else:
        pass
    print('\n')

    temp = []
    temp.append(cur_obj)

def align_all_to_target(target):
    for i in cmd.get_object_list():
        cmd.align(i, target)


def super_all_to_target(target):
    for i in cmd.get_object_list():
        cmd.super(i, target)


def make_polyala():
    for i in cmd.get_object_list():
        cmd.remove(i+' and not name C+CA+CO+N+CB+O')
        cmd.alter(i,'resn="ALA"')
        cmd.alter('chain A', 'chain="B"')
        cmd.save(i+'_polyala.pdb',i)


def separate_surfaces():
    cmd.create('chain_A', 'chain A')
    cmd.create('chain_B', 'chain B')
    cmd.create('chain_C', 'chain C')
    cmd.show('surface', 'chain_A')
    cmd.set('surface_color', 'goud', 'chain_A')
    cmd.show('surface', 'chain_B')
    cmd.set('surface_color', 'gray80', 'chain_B')
    cmd.show('surface', 'chain_C')
    cmd.set('surface_color', 'splitpea', 'chain_C')


def protein_protein_interface():
    #reset
    cmd.hide('sticks')
    cmd.hide('surface')

    # Select central residue interface --> center = 'sele' in pymol shell
    x = "sele"
    cmd.center()

    cmd.select('ppi', x+' around 12.5')
    cmd.show('sticks', 'ppi and not name C+O+N')
    cmd.show('sticks', x+' and not name C+O+N')
    cmd.hide('(h.)')
    cmd.select('ppi_A', 'ppi and chain A')
    cmd.select('ppi_B', 'ppi and chain B')
    cmd.create('ppi_B_surf', 'ppi_B')
    cmd.show('surface', 'ppi_B_surf')
    cmd.set('surface_color','gray80')
    cmd.set('transparency', 0.25)
    cmd.set('cartoon_highlight_color','gray80')
    cmd.create('ppi_A_surf', 'ppi_A')
    cmd.show('surface', 'ppi_A_surf')
    cmd.set('surface_color','blauw3','ppi_A_surf')
    cmd.set('transparency', 0.25)
    cmd.set('cartoon_highlight_color','gray80')


def axes():
    '''
    From PyMOL wiki
    '''
    from pymol.cgo import CYLINDER, cyl_text
    from pymol import cmd
    from pymol.vfont import plain
    # create the axes object, draw axes with cylinders coloured red, green,
    #blue for X, Y and Z
    obj = [
       CYLINDER, 0., 0., 0., 10., 0., 0., 0.2, 1.0, 1.0, 1.0, 1.0, 0.0, 0.,
       CYLINDER, 0., 0., 0., 0., 10., 0., 0.2, 1.0, 1.0, 1.0, 0., 1.0, 0.,
       CYLINDER, 0., 0., 0., 0., 0., 10., 0.2, 1.0, 1.0, 1.0, 0., 0.0, 1.0,
       ]

    # add labels to axes object
    cyl_text(obj,plain,[-5.,-5.,-1],'Origin',0.20,axes=[[3,0,0],[0,3,0],[0,0,3]])
    cyl_text(obj,plain,[10.,0.,0.],'X',0.20,axes=[[3,0,0],[0,3,0],[0,0,3]])
    cyl_text(obj,plain,[0.,10.,0.],'Y',0.20,axes=[[3,0,0],[0,3,0],[0,0,3]])
    cyl_text(obj,plain,[0.,0.,10.],'Z',0.20,axes=[[3,0,0],[0,3,0],[0,0,3]])

    # then we load it into PyMOL
    cmd.load_cgo(obj,'axes')


def print_protein_sequences(protein_object):
    '''Print aa sequence to shell of each chain in object
    Use: print_protein_sequences <objectname without .pdb>'''
    for i in cmd.get_chains(protein_object):
        print('CHAIN_'+i+'_'+protein_object)
        print(cmd.get_fastastr(protein_object+' and chain '+i))


def write_good_models():
    '''Write good_models to list and new directory'''
    print(set(good_models))
    print(len(good_models))
    with open('selected_models.list','w') as fout:
        for model in set(good_models):
            fout.write(model+'.pdb\n')
    commands.getoutput("mkdir sel; for i in `cat selected_models.list`; do cp $i sel; done")


def store_good_models():
    '''Saves current model to good_models list upon pressing F4 key'''
    good_models.append(temp[0])


def super_allfrag_to_target_frag(target, frag):
    for i in cmd.get_object_list():
        cmd.super(i+' and i. '+frag, target+' and i. '+frag)


def frag_aln_spr(aln_type, target, frag):
    if aln_type == 'align':
        for i in cmd.get_object_list():
            cmd.align(i+' and i. '+frag, target+' and i. '+frag)
    else:
        for i in cmd.get_object_list():
            cmd.super(i+' and i. '+frag, target+' and i. '+frag)



from pymol import stored
import random
import os.path

def objName_resiNo_append(resn,resi,model):
    stored.ObjNameResiduesToAnnotate = {}
    if not model in stored.ObjNameResiduesToAnnotate:
        stored.ObjNameResiduesToAnnotate[model] = []
    
    aadict = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
              'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
              'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
              'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
    
    if resn in aadict:
        stored.ObjNameResiduesToAnnotate[model].append((aadict[resn],resi))


def show_cavities(selection=None,chain=None):
    if selection is None:
        selection = 'sele'
    if chain is None:
        chain = 'a'
    try: 
        type(stored.cavities_to_delete)
    except:
        stored.cavities_to_delete=[]
    
    objName = cmd.get_object_list(selection)[0]
    cmd.iterate(objName, 'objName_resiNo_append(resn,resi,model)')
    
    #useRosettaRadii()
    
    cmd.set('surface_cavity_mode','1')
    cmd.set('surface_color', 'good_melon')
    cmd.set('transparency', '0.2')
        
    cmd.create('cavities_'+objName,objName,zoom=0)
    cmd.hide('everything','cavities_'+objName)
    cmd.show('surface','cavities_'+objName)
    (stored.cavities_to_delete).append('cavities_'+objName)

def hide_cavities(selection=None):
    for objName in stored.cavities_to_delete:
        cmd.delete(objName)
    cmd.set('surface_cavity_mode','0')

def show_interface(selection=None):
    if selection is None:
        selection = 'sele'
    objName = cmd.get_object_list(selection)[0]
    cmd.iterate(objName, 'objName_resiNo_append(resn,resi,model)')
    #useRosettaRadii()
    for objName in stored.ObjNameResiduesToAnnotate:
        cmd.select("interface", "none")
        cmd.select("heavy_interface", "none")
        cmd.select("aroundb","%s and chain B around 6.0"%(objName))
        cmd.select("arounda","%s and chain A around 6.0"%(objName))
        cmd.select("interfacea","aroundb or arounda")
        cmd.select("interface","byres(interfacea)")
        cmd.show( "sticks", "%s and interface"%(objName) )
        cmd.show( "lines", "not interface" )
        cmd.hide("(all and hydro and (elem c extend 1))") # all hydrogen, but polar
        cmd.show( "cartoon", "(not interface) or byres(neighbor(interface)) or byres(neighbor(byres(neighbor(interface))))" )
        cmd.delete('heavy_interface')
        cmd.delete('interface')
        cmd.dist("interfacea_polar_conts","interfacea","interfacea",quiet=1,mode=2,label=0,reset=1);cmd.enable("interfacea_polar_conts")
        cmd.delete('aroundb')
        cmd.delete('arounda')
        cmd.delete('interfacea')

        try:
            util.cba(33,"chain A and %s"%(objName)) # For some reason commands after this cannot be added?!?!
        except:
            pass
        util.cba(11,"chain B and %s"%(objName)) # For some reason commands after this cannot be added?!?!

def orient():
    cmd.orient()
    

## 都需要先选中sele，如果是show interface的话

cmd.extend("show_cavities", show_cavities)
cmd.extend("hide_cavities", hide_cavities)
cmd.extend("show_interface", show_interface)
cmd.extend("orient", orient)





cmd.set_key('F3', starting_view)
cmd.extend('s', starting_view)
cmd.extend('separate_by_chain', separate_by_chain)
cmd.extend('protein_protein_interface', protein_protein_interface)
cmd.extend('print_protein_sequences', print_protein_sequences)
cmd.extend('align_all_to_target', align_all_to_target)
cmd.extend('separate_surfaces', separate_surfaces)
cmd.set_key("pgup", object_focus, [UP])
cmd.set_key("pgdn", object_focus, [DOWN])
cmd.extend('make_polyala', make_polyala)
cmd.extend('save_seperate', save_seperate)
cmd.extend('super_all_to_target', super_all_to_target)
cmd.extend('axes',axes)
cmd.extend('write_good_models', write_good_models)
cmd.extend('super_allfrag_to_target_frag', super_allfrag_to_target_frag)
cmd.extend('frag_aln_spr',frag_aln_spr)
cmd.set_key('F4', store_good_models)
                
cmd.extend('V1', V1)
cmd.extend('V2', V2)
cmd.extend('V3', V3)
cmd.extend('V4', V4)
cmd.extend('V5', V5)
cmd.extend('Ligand1', ligand01)
cmd.extend('show_residues',show_residues)
