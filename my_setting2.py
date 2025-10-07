from pymol import cmd

def color_obj():
    """

AUTHOR

    Gareth Stockwell

USAGE

    color_obj(rainbow=0)

    This function colours each object currently in the PyMOL heirarchy
    with a different colour.  Colours used are either the 22 named
    colours used by PyMOL (in which case the 23rd object, if it exists,
    gets the same colour as the first), or are the colours of the rainbow

SEE ALSO

    util.color_objs()
    """

    # Process arguments
    rainbow=0
    rainbow = int(rainbow)

    # Get names of all PyMOL objects
    obj_list = cmd.get_names('objects')

    if rainbow:

        print("\nColouring objects as rainbow\n")

        nobj = len(obj_list)

        # Create colours starting at blue(240) to red(0), using intervals
        # of 240/(nobj-1)
        for j in range(nobj):
            hsv = (240 - j * 240 / (nobj - 1), 1, 1)
            # Convert to RGB
            rgb = hsv_to_rgb(hsv)
            # Define the new colour
            cmd.set_color("col" + str(j), rgb)
            print(obj_list[j], rgb)
            # Colour the object
            cmd.color("col" + str(j), obj_list[j])

    else:

        print("\nColouring objects using PyMOL defined colours\n")

        # List of available colours
        colours = [
        'my_color_0', 'my_color_1', 'my_color_2', 'my_color_3',
        'my_color_4', 'my_color_5', 'my_color_6', 'my_color_7',
        'my_color_8', 'my_color_9', 'my_color_10', 'my_color_11'
    ]

        ncolours = len(colours)

        # Loop over objects
        i = 0
        for obj in obj_list:
            print("  ", obj, colours[i])
            cmd.color(colours[i], obj)
            i = i + 1
            if(i == ncolours):
                i = 1


def color_obj2():

    # Process arguments
    rainbow=0
    rainbow = int(rainbow)

    # Get names of all PyMOL objects
    obj_list = cmd.get_names('objects')

    if rainbow:

        print("\nColouring objects as rainbow\n")

        nobj = len(obj_list)

        # Create colours starting at blue(240) to red(0), using intervals
        # of 240/(nobj-1)
        for j in range(nobj):
            hsv = (240 - j * 240 / (nobj - 1), 1, 1)
            # Convert to RGB
            rgb = hsv_to_rgb(hsv)
            # Define the new colour
            cmd.set_color("col" + str(j), rgb)
            print(obj_list[j], rgb)
            # Colour the object
            cmd.color("col" + str(j), obj_list[j])

    else:

        print("\nColouring objects using PyMOL defined colours\n")

        # List of available colours
        colours = ['limegreen', 'blauw3','goud','crimson','indianred','cadmiumorange','orangered1', 'palecyan1','red','blauw2','blauw','palecyan2'
    ]

        ncolours = len(colours)

        # Loop over objects
        i = 0
        for obj in obj_list:
            print("  ", obj, colours[i])
            cmd.color(colours[i], obj)
            i = i + 1
            if(i == ncolours):
                i =1


def color_obj3():

    # Process arguments
    rainbow=0
    rainbow = int(rainbow)

    # Get names of all PyMOL objects
    obj_list = cmd.get_names('objects')

    if rainbow:

        print("\nColouring objects as rainbow\n")

        nobj = len(obj_list)

        # Create colours starting at blue(240) to red(0), using intervals
        # of 240/(nobj-1)
        for j in range(nobj):
            hsv = (240 - j * 240 / (nobj - 1), 1, 1)
            # Convert to RGB
            rgb = hsv_to_rgb(hsv)
            # Define the new colour
            cmd.set_color("col" + str(j), rgb)
            print(obj_list[j], rgb)
            # Colour the object
            cmd.color("col" + str(j), obj_list[j])

    else:

        print("\nColouring objects using PyMOL defined colours\n")

        # List of available colours
        colours = ["good_teal","good_navaho", "good_melon",  "good_pink", "good_lightgreen", "good_purple", "good_lightblue", "good_green", "good_peach","good_blue",  "good_gray",  "good_red",  "good_yellow",  "good_darkblue"
    ]

        ncolours = len(colours)

        # Loop over objects
        i = 0
        for obj in obj_list:
            print("  ", obj, colours[i])
            cmd.color(colours[i], obj)
            i = i + 1
            if(i == ncolours):
                i =1



def color_obj4():

    # Process arguments
    rainbow=0
    rainbow = int(rainbow)

    # Get names of all PyMOL objects
    obj_list = cmd.get_names('objects')

    if rainbow:

        print("\nColouring objects as rainbow\n")

        nobj = len(obj_list)

        # Create colours starting at blue(240) to red(0), using intervals
        # of 240/(nobj-1)
        for j in range(nobj):
            hsv = (240 - j * 240 / (nobj - 1), 1, 1)
            # Convert to RGB
            rgb = hsv_to_rgb(hsv)
            # Define the new colour
            cmd.set_color("col" + str(j), rgb)
            print(obj_list[j], rgb)
            # Colour the object
            cmd.color("col" + str(j), obj_list[j])

    else:

        print("\nColouring objects using PyMOL defined colours\n")

        # List of available colours
        colours = ["C1","C2","C3","C4","C5","C6","good_blue","good_yellow","good_green"
    ]

        ncolours = len(colours)

        # Loop over objects
        i = 0
        for obj in obj_list:
            print("  ", obj, colours[i])
            cmd.color(colours[i], obj)
            i = i + 1
            if(i == ncolours):
                i =1


def color_obj5():

    # Process arguments
    rainbow=0
    rainbow = int(rainbow)

    # Get names of all PyMOL objects
    obj_list = cmd.get_names('objects')
    cmd.set_color("good_gray",       [220,220,220]) #dcdcdc
    cmd.set_color("good_teal",      [ 0.310, 0.725, 0.686 ]) #4FB9AF
    cmd.set_color("good_navaho",     [255,224,172]) #FFE0AC
    cmd.set_color("good_melon",      [255,198,178]) #FFC6B2
    cmd.set_color("good_pink",       [255,172,183]) #FFACB7
    cmd.set_color("good_purple",     [213,154,181]) #D59AB5
    cmd.set_color("good_lightblue",  [149,150,198]) #9596C6
    cmd.set_color("good_blue",       [102,134,197]) #6686C5
    cmd.set_color("good_darkblue",   [75,95,170]) #4B5FAA

    if rainbow:

        print("\nColouring objects as rainbow\n")

        nobj = len(obj_list)

        # Create colours starting at blue(240) to red(0), using intervals
        # of 240/(nobj-1)
        for j in range(nobj):
            hsv = (240 - j * 240 / (nobj - 1), 1, 1)
            # Convert to RGB
            rgb = hsv_to_rgb(hsv)
            # Define the new colour
            cmd.set_color("col" + str(j), rgb)
            print(obj_list[j], rgb)
            # Colour the object
            cmd.color("col" + str(j), obj_list[j])

    else:

        print("\nColouring objects using PyMOL defined colours\n")

        # List of available colours
        colours = ["good_gray","good_teal","good_navaho","good_melon","good_pink", "good_purple","good_lightblue","good_blue","good_darkblue"
    ]

        ncolours = len(colours)

        # Loop over objects
        i = 0
        for obj in obj_list:
            print("  ", obj, colours[i])
            cmd.color(colours[i], obj)
            i = i + 1
            if(i == ncolours):
                i =1


def resicolor(selection='all'):
    
    '''USAGE: resicolor <selection>
    colors all or the given selection with arbitrary
    coloring scheme.
    '''
    cmd.select ('calcium','resn ca or resn cal')
    cmd.select ('acid','resn asp or resn glu or resn cgu')
    cmd.select ('basic','resn arg or resn lys or resn his')
    cmd.select ('nonpolar','resn met or resn phe or resn pro or resn trp or resn val or resn leu or resn ile or resn ala')
    cmd.select ('polar','resn ser or resn thr or resn asn or resn gln or resn tyr')
    cmd.select ('cys','resn cys or resn cyx')
    cmd.select ('backbone','name ca or name n or name c or name o')
    cmd.select ('none')

    print(selection)
    code={'acid'    :  'red'    ,
          'basic'   :  'blue'   ,
          'nonpolar':  'orange' ,
          'polar'   :  'green'  ,
          'cys'     :  'yellow'}
    cmd.select ('none')
    for elem in code:
        line='color '+code[elem]+','+elem+'&'+selection
        print(line)
        cmd.do (line)
    word='color white,backbone &'+selection
    print(word)
    cmd.do (word)                  #Used to be in code, but looks like
                                   #dictionnaries are accessed at random
    cmd.hide ('everything','resn HOH')





from pymol import cmd, stored

def interfaceResidues(cmpx, cA='c. A', cB='c. B', cutoff=1.0, selName="interface"):
    """
    interfaceResidues -- finds 'interface' residues between two chains in a complex.
    
    PARAMS
        cmpx
            The complex containing cA and cB
        
        cA
            The first chain in which we search for residues at an interface
            with cB
        
        cB
            The second chain in which we search for residues at an interface
            with cA
        
        cutoff
            The difference in area OVER which residues are considered
            interface residues.  Residues whose dASA from the complex to
            a single chain is greater than this cutoff are kept.  Zero
            keeps all residues.
            
        selName
            The name of the selection to return.
            
    RETURNS
        * A selection of interface residues is created and named
            depending on what you passed into selName
        * An array of values is returned where each value is:
            ( modelName, residueNumber, dASA )
            
    NOTES
        If you have two chains that are not from the same PDB that you want
        to complex together, use the create command like:
            create myComplex, pdb1WithChainA or pdb2withChainX
        then pass myComplex to this script like:
            interfaceResidues myComlpex, c. A, c. X
            
        This script calculates the area of the complex as a whole.  Then,
        it separates the two chains that you pass in through the arguments
        cA and cB, alone.  Once it has this, it calculates the difference
        and any residues ABOVE the cutoff are called interface residues.
            
    AUTHOR:
        Jason Vertrees, 2009.       
    """
    # Save user's settings, before setting dot_solvent
    oldDS = cmd.get("dot_solvent")
    cmd.set("dot_solvent", 1)
    
    # set some string names for temporary objects/selections
    tempC, selName1 = "tempComplex", selName+"1"
    chA, chB = "chA", "chB"
    
    # operate on a new object & turn off the original
    cmd.create(tempC, cmpx)
    cmd.disable(cmpx)
    
    # remove cruft and inrrelevant chains
    cmd.remove(tempC + " and not (polymer and (%s or %s))" % (cA, cB))
    
    # get the area of the complete complex
    cmd.get_area(tempC, load_b=1)
    # copy the areas from the loaded b to the q, field.
    cmd.alter(tempC, 'q=b')
    
    # extract the two chains and calc. the new area
    # note: the q fields are copied to the new objects
    # chA and chB
    cmd.extract(chA, tempC + " and (" + cA + ")")
    cmd.extract(chB, tempC + " and (" + cB + ")")
    cmd.get_area(chA, load_b=1)
    cmd.get_area(chB, load_b=1)
    
    # update the chain-only objects w/the difference
    cmd.alter( "%s or %s" % (chA,chB), "b=b-q" )
    
    # The calculations are done.  Now, all we need to
    # do is to determine which residues are over the cutoff
    # and save them.
    stored.r, rVal, seen = [], [], []
    cmd.iterate('%s or %s' % (chA, chB), 'stored.r.append((model,resi,b))')

    cmd.enable(cmpx)
    cmd.select(selName1, 'none')
    for (model,resi,diff) in stored.r:
        key=resi+"-"+model
        if abs(diff)>=float(cutoff):
            if key in seen: continue
            else: seen.append(key)
            rVal.append( (model,resi,diff) )
            # expand the selection here; I chose to iterate over stored.r instead of
            # creating one large selection b/c if there are too many residues PyMOL
            # might crash on a very large selection.  This is pretty much guaranteed
            # not to kill PyMOL; but, it might take a little longer to run.
            cmd.select( selName1, selName1 + " or (%s and i. %s)" % (model,resi))

    # this is how you transfer a selection to another object.
    cmd.select(selName, cmpx + " in " + selName1)
    # clean up after ourselves
    cmd.delete(selName1)
    cmd.delete(chA)
    cmd.delete(chB)
    cmd.delete(tempC)
    # show the selection
    cmd.enable(selName)
    
    # reset users settings
    cmd.set("dot_solvent", oldDS)
    
    return rVal



from pymol import cmd

def color_h(selection='all'):
    s = str(selection)
    print(s)
    cmd.set_color('color_ile',[0.996,0.062,0.062])
    cmd.set_color('color_phe',[0.996,0.109,0.109])
    cmd.set_color('color_val',[0.992,0.156,0.156])
    cmd.set_color('color_leu',[0.992,0.207,0.207])
    cmd.set_color('color_trp',[0.992,0.254,0.254])
    cmd.set_color('color_met',[0.988,0.301,0.301])
    cmd.set_color('color_ala',[0.988,0.348,0.348])
    cmd.set_color('color_gly',[0.984,0.394,0.394])
    cmd.set_color('color_cys',[0.984,0.445,0.445])
    cmd.set_color('color_tyr',[0.984,0.492,0.492])
    cmd.set_color('color_pro',[0.980,0.539,0.539])
    cmd.set_color('color_thr',[0.980,0.586,0.586])
    cmd.set_color('color_ser',[0.980,0.637,0.637])
    cmd.set_color('color_his',[0.977,0.684,0.684])
    cmd.set_color('color_glu',[0.977,0.730,0.730])
    cmd.set_color('color_asn',[0.973,0.777,0.777])
    cmd.set_color('color_gln',[0.973,0.824,0.824])
    cmd.set_color('color_asp',[0.973,0.875,0.875])
    cmd.set_color('color_lys',[0.899,0.922,0.922])
    cmd.set_color('color_arg',[0.899,0.969,0.969])
    cmd.color("color_ile","("+s+" and resn ile)")
    cmd.color("color_phe","("+s+" and resn phe)")
    cmd.color("color_val","("+s+" and resn val)")
    cmd.color("color_leu","("+s+" and resn leu)")
    cmd.color("color_trp","("+s+" and resn trp)")
    cmd.color("color_met","("+s+" and resn met)")
    cmd.color("color_ala","("+s+" and resn ala)")
    cmd.color("color_gly","("+s+" and resn gly)")
    cmd.color("color_cys","("+s+" and resn cys)")
    cmd.color("color_tyr","("+s+" and resn tyr)")
    cmd.color("color_pro","("+s+" and resn pro)")
    cmd.color("color_thr","("+s+" and resn thr)")
    cmd.color("color_ser","("+s+" and resn ser)")
    cmd.color("color_his","("+s+" and resn his)")
    cmd.color("color_glu","("+s+" and resn glu)")
    cmd.color("color_asn","("+s+" and resn asn)")
    cmd.color("color_gln","("+s+" and resn gln)")
    cmd.color("color_asp","("+s+" and resn asp)")
    cmd.color("color_lys","("+s+" and resn lys)")
    cmd.color("color_arg","("+s+" and resn arg)")


def color_h2(selection='all'):
    s = str(selection)
    print(s)
    cmd.set_color("color_ile2",[0.938,1,0.938])
    cmd.set_color("color_phe2",[0.891,1,0.891])
    cmd.set_color("color_val2",[0.844,1,0.844])
    cmd.set_color("color_leu2",[0.793,1,0.793])
    cmd.set_color("color_trp2",[0.746,1,0.746])
    cmd.set_color("color_met2",[0.699,1,0.699])
    cmd.set_color("color_ala2",[0.652,1,0.652])
    cmd.set_color("color_gly2",[0.606,1,0.606])
    cmd.set_color("color_cys2",[0.555,1,0.555])
    cmd.set_color("color_tyr2",[0.508,1,0.508])
    cmd.set_color("color_pro2",[0.461,1,0.461])
    cmd.set_color("color_thr2",[0.414,1,0.414])
    cmd.set_color("color_ser2",[0.363,1,0.363])
    cmd.set_color("color_his2",[0.316,1,0.316])
    cmd.set_color("color_glu2",[0.27,1,0.27])
    cmd.set_color("color_asn2",[0.223,1,0.223])
    cmd.set_color("color_gln2",[0.176,1,0.176])
    cmd.set_color("color_asp2",[0.125,1,0.125])
    cmd.set_color("color_lys2",[0.078,1,0.078])
    cmd.set_color("color_arg2",[0.031,1,0.031])
    cmd.color("color_ile2","("+s+" and resn ile)")
    cmd.color("color_phe2","("+s+" and resn phe)")
    cmd.color("color_val2","("+s+" and resn val)")
    cmd.color("color_leu2","("+s+" and resn leu)")
    cmd.color("color_trp2","("+s+" and resn trp)")
    cmd.color("color_met2","("+s+" and resn met)")
    cmd.color("color_ala2","("+s+" and resn ala)")
    cmd.color("color_gly2","("+s+" and resn gly)")
    cmd.color("color_cys2","("+s+" and resn cys)")
    cmd.color("color_tyr2","("+s+" and resn tyr)")
    cmd.color("color_pro2","("+s+" and resn pro)")
    cmd.color("color_thr2","("+s+" and resn thr)")
    cmd.color("color_ser2","("+s+" and resn ser)")
    cmd.color("color_his2","("+s+" and resn his)")
    cmd.color("color_glu2","("+s+" and resn glu)")
    cmd.color("color_asn2","("+s+" and resn asn)")
    cmd.color("color_gln2","("+s+" and resn gln)")
    cmd.color("color_asp2","("+s+" and resn asp)")
    cmd.color("color_lys2","("+s+" and resn lys)")
    cmd.color("color_arg2","("+s+" and resn arg)")


cmd.extend('color_h',color_h)
cmd.extend('color_h2',color_h2)
cmd.extend ('ri',resicolor)
cmd.extend("interfaceResidues", interfaceResidues)


cmd.do('color_obj()')
cmd.extend('c1', color_obj)
cmd.extend('c2', color_obj2)
cmd.extend('c3', color_obj3)
cmd.extend('c4', color_obj4)
cmd.extend('c5', color_obj5)

