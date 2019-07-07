 
import os
def CutOut(filename, start, end):
    """ Cut out lines from start to end from file filename """
 
    # check it's worth even reading the file (sanity check)
    if start >= end:
        return
 
    # read the entire file in as separate lines
    filelines = file(filename).readlines()
 
    # make sure start is a sane value
    if start > len(filelines):
       return
 
    # make sure end is a sane value
    if end > len(filelines):
       end = len(filelines)
 
    # chop out the bit we don't want
    filelines = filelines[:start] + filelines[end:]
 
    # could do this instead (not sure which is quicker):
    # del filelines[start:end]
 
    # write out the new set of lines
    file(filename,"w").writelines(filelines)
 