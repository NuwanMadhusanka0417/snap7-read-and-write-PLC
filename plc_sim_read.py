import snap7.client
from snap7.snap7types import *
from snap7.util import *
import time
class DBObject(object):
    pass

offsets = { "Bool":2,"Int": 2,"Real":4,"DInt":6,"String":256}


# Copy of my database in plc
db=\
"""
door	Bool	0.0
bulb	Bool	0.1
count	Int	2.0
switch	Bool	4.0
"""
def Read_DB(plc,db_num,length,dbitems):
    data = plc.read_area(areas['DB'],db_num,0,length)
    obj = DBObject()
    for item in dbitems:
        value = None
        offset = int(item['bytebit'].split('.')[0])
        if item['datatype']=='Real':
            value = get_real(data,offset)

        if item['datatype']=='Bool':
            bit =int(item['bytebit'].split('.')[1])
            value = get_bool(data,offset,bit)
            # check is this switch or another one
            if offset==4:  
                if value==1:
                    set_bool(data,offset,bit,0)
                else:
                    set_bool(data,offset,bit,1)
        if item['datatype']=='Int':
            value = get_int(data, offset)

        if item['datatype']=='String':
            value = get_string(data, offset)

        obj.__setattr__(item['name'], value)
    plc.write_area(areas["DB"],1,0,data)
    return obj

def db_size(array,bytekey,datatypekey):
    seq,length = [x[bytekey] for x in array],[x[datatypekey] for x in array]
    idx = seq.index(max(seq))  # get index of max value
    lastByte = int(max(seq).split('.')[0])+(offsets[length[idx]]) # max val+offset of max val datatype
    return lastByte

if __name__=="__main__":
    plc = snap7.client.Client()
    plc.connect('127.0.0.1',0,1)
    db_number = 1  # Database Number
    itemlist = filter(lambda a:a!='',db.split('\n'))
    deliminator='\t'
    items = [
        {
            "name":x.split(deliminator)[0],
            "datatype":x.split(deliminator)[1],
            "bytebit":x.split(deliminator)[2]
         } for x in itemlist
    ]
   
    length = db_size(items,'bytebit','datatype') #get length of datablock
    meh = Read_DB(plc,db_number,length,items)
    print ("door:\t{}\nbulb:\t{}\ncount:\t{}\nswitch:\t{}".format(meh.door,meh.bulb,meh.count,meh.switch)) 
