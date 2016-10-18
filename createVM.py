import os
for i in xrange(0,1):
    print 'VM named:centos6-%s creation started'%str(i)
    try:
        os.system("virt-install \
        --name centos6-%s \
        --ram 14336 \
        --disk path=/var/lib/libvirt/images/centos6-%s.img,size=200 \
        --vcpus 1 \
        --os-type linux \
        --os-variant rhel6 \
        --network bridge=br0 \
        --graphics none \
        --console pty,target_type=serial \
        --location 'http://mirror.i3d.net/pub/centos/6/os/x86_64/' \
        --extra-args 'console=ttyS0,115200n8 serial' \
        --noautoconsole"%(str(i),str(i)))
        print 'VM named:centos6-%s creation completed successfully'%str(i)
    except:
       print 'VM named:centos6-%s creation error'%str(i)
       break
