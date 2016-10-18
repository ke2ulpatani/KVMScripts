echo 'Adding the bridge'
sudo brctl addbr br0
echo 'Adding the interfaces'
sudo brctl addif br0 eno1
echo 'Rebooting'
sudo reboot
