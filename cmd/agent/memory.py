import os

class Receiver:
    def __init__(self):
        self.occupy_tmpl = """
#!/bin/bash
mkdir /tmp/perismem
mount -t tmpfs -o size=%dM tmpfs /tmp/perismem 
dd if=/dev/zero of=/tmp/perismem/block """ 
        self.clear_tmpl = """
#!/bin/bash
rm /tmp/perismem/block  
umount /tmp/perismem  
rmdir /tmp/perismem  """


    def occupy(num):
        sh = self.occupy_tmpl % (num)
        os.system(sh)

    def clear():
        sh = self.clear_tmpl % (num)
        os.system(sh)
