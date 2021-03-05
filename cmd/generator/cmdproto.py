import os
import yaml
import random
import cmd.generator.redis.key as rkey
import cmd.generator.redis.string as rstr
import cmd.generator.redis.integer as rint
import cmd.generator.redis.float as rflo
import cmd.generator.redis.hash as rhas
import cmd.generator.redis.ihash as rihas
import cmd.generator.redis.list as rlis
import cmd.generator.redis.set as rset
import cmd.generator.redis.zset as rzse
import cmd.generator.redis.mstring as rmst
import cmd.generator.redis.minteger as rmin
import cmd.generator.redis.mhash as rmha
import cmd.generator.redis.mlist as rmli
import cmd.generator.redis.mset as rmse
import cmd.generator.redis.mzset as rmzs
import cmd.generator.redis.geo as rgeo

class CmdProto:
    Types = {'key':rkey.Key, 'string':rstr.String, 'integer':rint.Integer, 'float':rflo.Float,\
            'ihash':rihas.IHash,'hash':rhas.Hash, 'list':rlis.List, 'set':rset.Set, 'zset':rzse.Zset,\
            'mstring':rmst.MString, 'minteger':rmin.MInteger, 'geo':rgeo.Geo,\
            'mhash':rmha.MHash, 'mlist':rmli.MList, 'mset':rmse.MSet, 'mzset':rmzs.MZset}
    Names = list(Types.keys())

    #CmdProto.Hub:{'hash': {'create': [{'HSET': 'HSET {key} {field} {val}'},]...}
    Hub = {}

    def __init__(self, template):
        normal = './cmd/generator/template/redis/normal/'
        abnormal = './cmd/generator/template/redis/abnormal/'
        basedir = normal if template=='normal' else abnormal
        #dirs:["string","integer","hash","list","set","zset"...]
        dirs = os.listdir(basedir)
        for redtype in dirs: 
            cmdsmap = {'create':[], 'require':[], 'update':[], 'delete':[]}
            for operation in cmdsmap:
                path = '%s/%s/%s.yaml' %(basedir, redtype, operation)
                with open(path, 'r') as f:
                    cmdsmap[operation] = yaml.safe_load(f.read())
            CmdProto.Hub[redtype] = cmdsmap
        print('CmdProto.Hub:::', CmdProto.Hub.keys())

    def rand(self):
        name = random.choice(CmdProto.Names)
        return CmdProto.Types[name], CmdProto.Hub[name]

    def get(self, name=None):
        if not name or not CmdProto.Hub.get(name) or not CmdProto.Types.get(name):
            print('Error, failed CmdProto.get ', name)
            return self.rand()
        return CmdProto.Types[name], CmdProto.Hub[name]
