#nmap -sn -PE --min-hostgroup 1024 --min-parallelism 1024 -oX nmap.xml $1
#-sn 不进行端口扫描，只进行ping检测
#-PE 通过ICMP echo来判定主机是否存活
#--min-hostgroup 1024 最小分组设置1024个Ip地址
#--min-parallelism 1024 将探针的数量设置最小为1024
if [$# -lt 1];then
  echo 'Example:$0 192.168.1.1/24'
  exit 1

fi
nmap -sn -PE --min-hostgroup 1024 --min-parallelism 1024 -oX nmap.xml $1

./web_c_sacn.py

