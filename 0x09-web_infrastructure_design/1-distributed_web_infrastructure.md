**Why are we adding these elements?**
We are adding a load balancer to distribute traffic across multiple servers. This will help to ensure that the website remains available even if one of the servers fails.
We are adding a second database server to create a primary-replica (master-slave) cluster. This will help to ensure that the website's data is always available, even if one of the database servers fails.

**Load balancer distribution algorithm**
The load balancer is configured with the round robin distribution algorithm. This means that each request is randomly sent to one of the web servers.

**Active-Active vs. Active-Passive**
The load balancer is configured in an active-active setup. This means that both web servers are serving traffic at the same time. In an active-passive setup, only one web server is serving traffic at a time. The other web server is in standby mode and takes over if the active web server fails.

**Database primary-replica cluster**
The database cluster is configured in a master-slave configuration. The primary node is responsible for writing data to the database. The replica node is responsible for reading data from the database.

**Primary node vs. Replica node**
The primary node is the only node that can write data to the database. The replica node can only read data from the database.

**Issues
**

**Single point of failure (SPOF)**: The load balancer is a single point of failure. If the load balancer fails, all traffic will be routed to one of the web servers, which could overload the server and cause it to fail.
**Security issues**: The infrastructure does not have a firewall or HTTPS enabled. This means that the website is vulnerable to attacks.
**No monitoring**: The infrastructure is not being monitored. This means that we will not be able to detect problems with the infrastructure until it is too late.
