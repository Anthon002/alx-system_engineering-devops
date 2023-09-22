**Why are we adding these elements?**

We are adding a firewall to each server to protect the server from unauthorized access.
We are adding a load balancer to distribute traffic across the two web servers. This will help to ensure that the website remains available even if one of the web servers fails.
We are adding an SSL certificate to secure the traffic between the user's browser and the load balancer. This will help to protect the user's data from being intercepted by unauthorized parties.
We are adding a monitoring client to each server to collect data about the server's performance. This data can be used to identify problems with the server and take corrective action before they cause outages.

**Firewalls**
Firewalls are used to protect networks from unauthorized access. They can be configured to block traffic from certain IP addresses or ports.

**HTTPS**
HTTPS is a secure protocol that encrypts traffic between the user's browser and the server. This helps to protect the user's data from being intercepted by unauthorized parties.

**Monitoring**
Monitoring is used to collect data about the performance of a system. This data can be used to identify problems with the system and take corrective action before they cause outages.

**Monitoring tool**
The monitoring tool is collecting data about the server's performance using metrics such as CPU usage, memory usage, and disk space usage. This data can be used to identify problems with the server and take corrective action before they cause outages.

**Web server QPS**
To monitor the web server QPS, we can use a monitoring tool to collect data about the number of requests that the web server is handling per second.

**Issues**
Terminating SSL at the load balancer level is an issue because it means that all of the traffic between the user's browser and the load balancer is encrypted. This can add overhead to the load balancer and can also make it more difficult to troubleshoot problems with the load balancer.
Having only one MySQL server capable of accepting writes is an issue because if the MySQL server fails, the website will be unable to write data to the database.
Having servers with all the same components (database, web server and application server) might be a problem because if one server fails, all of the components will be unavailable.
