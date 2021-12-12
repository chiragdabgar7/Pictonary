# Vagrant.configure("2") do |config|
#   config.vm.box = "ubuntu/bionic64"
# #  config.vm.provider "virtualbox" do |v|
#  # 	v.default_nic_type = "82543GC"
#  # end
# end

# Vagrant.configure("2") do |n1|
#   n1.vm.box = "ubuntu/bionic64"
#   n1.vm.hostname = "n1"
#   n1.vm.network "private_network", ip: "192.168.56.10"
# #  config.vm.provider "virtualbox" do |v|
#  # 	v.default_nic_type = "82543GC"
#  # end
# end

Vagrant.configure("2") do |config|
  config.vm.define "n1" do |n1|
    n1.vm.box = "ubuntu/bionic64"
    n1.vm.hostname = 'n1'
    # n1.vm.box_url = "ubuntu/bionic64"

    n1.vm.network :private_network, ip: "192.168.56.101"

    # n1.vm.provider :virtualbox do |v|
    #   v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    #   v.customize ["modifyvm", :id, "--memory", 512]
    #   v.customize ["modifyvm", :id, "--name", "n1"]
    # end
  end

  config.vm.define "n2" do |n2|
    n2.vm.box = "ubuntu/bionic64"
    n2.vm.hostname = 'n2'
    # n2.vm.box_url = "ubuntu/bionic64"

    n2.vm.network :private_network, ip: "192.168.56.102"

    # n2.vm.provider :virtualbox do |v|
    #   v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    #   v.customize ["modifyvm", :id, "--memory", 512]
    #   v.customize ["modifyvm", :id, "--name", "n2"]
    # end
  end
end
