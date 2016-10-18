import os,sys

currentVM = str(sys.argv[1])
cloneVM = str(sys.argv[2])

os.system('virsh shutdown %s'%str(currentVM))
os.system('virt-clone -o %s -n %s -f /var/lib/libvirt/images/%s.img'%(str(currentVM),str(cloneVM),str(cloneVM)))
os.system('virt-sysprep -d %s'%str(cloneVM))

print ('VM %s cloned.'%currentVM)

