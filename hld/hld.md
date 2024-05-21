# System Design

## Approach to system design

- scope the problem and ask clarifying questions. (usecases, constraints, goal, what does success look like in the system - there is no single right answer - its all about tradeoffs)
- which area and what degree you gonna focus on your optimization and scaling on.

## Core building blocks for scaling up an apllication

### Load balancing

- for scaling any web application.
- solves overloading of web server as more and more clients access the web server.
- job of loadbalancer is to distribute (or redirect) loads to bunch of different web servers.
- simply redirecting a url request is going to be far lighter weight and less processor intensive than actually handling the requests and generating the response.
- loadbalancer is really just another machine like a linux server running some specialized software like NGINX, AWS elastic load balancing, etc.
- what if the loadbalancer itself gets overloaded? solution - multiple loadbalancers
  - ![multiple_loadbalancers](./images/multiple_loadbalancers.png)
- we can configure the way loadbalancer distributes the load across the web servers. some common algorithms like round robin, least load, or custom scripts, etc. We can also configure ping to check the health of web servers.
- one more way in which you can do load balancing is really just at the application level. Dividing the application by its features like mail service, web service, chat service, db service, etc (microservices).
- essentially with load balancing technology, people no longer needed a single very strong monolithic powerful server, instead we can have tons of cheap commodity level servers, CPUs, memory and then just add these machines to the load balancer and easily start scaling up a web app across millions of people. So now we are able to have infinite computing power.
- problem: single point of failure for loadbalancer. solution: multiple loadbalancers.

### Caching

- how to scale up data?
