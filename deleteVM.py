import os,sys

vmName = str(sys.argv[1])

os.system('sudo virsh destroy %s'%vmName)
os.system('sudo virsh undefine %s'%vmName)
os.system('sudo virsh vol-delete --pool testPool %s.img'%vmName)

print ('VM %s deleted.'%vmName)

