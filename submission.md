CloudMart Deployment – Milestone 3 Submission

## 1. Azure Login and Resource Verification

I logged into Azure using the lab environment and verified all deployed resources.

Resource Group: Student-RG-2037990

Resources created:
- Azure Container Instance (ACI)
- Azure Container Registry (ACR)
- Cosmos DB

### Screenshot 1: Resource Group Overview
![Resource Group](https://github.com/user-attachments/assets/4c94c9ed-2d2f-4564-bb4f-af5d34327e7a)

## 2. Azure Deployment

### Screenshot 2: Container Instance Details (Status + URL)
![ACI Details]()

### Screenshot 3: Cosmos DB Data Explorer (Products, Cart, Orders)
![Cosmos DB](https://github.com/user-attachments/assets/d6277db8-291b-40cb-9b8e-bd5808f04f29)

### Screenshot 4: Container Logs (Application Startup)
![Logs](https://github.com/user-attachments/assets/54662131-6817-4393-b6dc-a030980734e5)

### Screenshot 5: 
(https://github.com/user-attachments/assets/a5b4f21e-6bc5-4786-9fb4-09707d0e9222)

### Screenshot 6: 
(https://github.com/user-attachments/assets/06889cd3-8aa5-47e4-a263-b2ee1b8c6a46)

### Screenshot 7: 
(https://github.com/user-attachments/assets/dbb6411e-082b-48a3-8131-d69b01b7482c)

### Screenshot 8: 
(https://github.com/user-attachments/assets/cb0cb394-bfea-4558-a647-2ef06e1a51bc)
### Screenshot 9: 
(https://github.com/user-attachments/assets/ec41a3b3-f489-4c25-809e-7c9b0eb09fc4)

### Screenshot 10: 
(https://github.com/user-attachments/assets/ca444f5b-c953-4b71-b960-bee3fc177af3")

### Screenshot 11: 
(https://github.com/user-attachments/assets/3e12fbfc-85d3-4b83-86e7-b8d84718a859)

### Screenshot 12: 
(https://github.com/user-attachments/assets/77a72fea-42a3-4f76-b29f-5b8d44a2f46a)

### Screenshot 13: 
(https://github.com/user-attachments/assets/3c083901-3afa-4859-a468-bc9824b3363b)

### Screenshot 14: 
(https://github.com/user-attachments/assets/34dbd9cc-6b9c-43e3-a7fd-1adffb8c185c)
### Screenshot 15: 
(https://github.com/user-attachments/assets/673816f1-0cdc-4345-bec3-429a1039791e)

### Screenshot 16: 
(https://github.com/user-attachments/assets/566723c1-4d12-4763-8913-b41216c8077d)

### Screenshot 17: 
(https://github.com/user-attachments/assets/748e7ff3-a255-4f21-8ca3-804c56b95751)

### Screenshot 18: 
(https://github.com/user-attachments/assets/c5b9177e-79db-45d6-a43c-f47af2615e31)

### Screenshot 19: 
(https://github.com/user-attachments/assets/4ccc5c9a-496b-4fa9-8840-f6918f8d4001)

### Screenshot 20: 

(https://github.com/user-attachments/assets/a7cb077c-596c-4a5b-9275-8dc0a3f9daeb)

### Screenshot 21: 
(https://github.com/user-attachments/assets/7d13e302-a526-4879-beab-749e02839827)
### Screenshot 22: 
(https://github.com/user-attachments/assets/0a793c24-9af2-4496-8abf-f9549bd5323b")
### Screenshot 23: 
(https://github.com/user-attachments/assets/48dd838a-6006-424d-afb2-4dc21d7fcaeb)

### Screenshot 24: 
(https://github.com/user-attachments/assets/2a399a8c-de54-4b62-bf9b-68b277063599")

### Screenshot 25: 
(https://github.com/user-attachments/assets/060735c3-f744-4485-8954-d55501bb7b94)
### Screenshot 26: 
(https://github.com/user-attachments/assets/6eb5fad7-0faa-4269-9f8b-156a0fe6d747)
### Screenshot 27:
(https://github.com/user-attachments/assets/6a73d899-34f2-449e-bdd4-7fd81688aa38)
### Screenshot 28:
(https://github.com/user-attachments/assets/6489027a-84ac-41c5-ae69-7bd386306460")
### Screenshot 29:
(https://github.com/user-attachments/assets/3f08ddfc-ab03-4ec0-b9e4-88bf01557f8c)

Reflection on Milestone 3

Milestone 3, which involved deploying the CloudMart application on Azure using containerized infrastructure, significantly expands on the work completed in earlier milestones. The deployment of a publicly exposed Azure Container Instance (ACI) introduces a different security model when compared to the network security group (NSG)-protected virtual machines (VMs) from Milestone 1. In Milestone 1, NSGs provided a layer of network-level security, allowing only specific IPs or ranges to access the VM, and this was crucial for managing traffic flow. However, with an ACI, the container is publicly exposed by default, which creates more potential vulnerabilities, especially if it's directly accessible from the internet. In production, additional protections would be necessary, such as configuring a virtual network (VNet) for the container and using Azure Firewall to filter traffic, enabling encryption in transit, and implementing API authentication to prevent unauthorized access.

Applying the monitoring techniques from Milestone 2 to this containerized deployment would involve several strategies. For instance, I could leverage Azure Monitor to collect container logs and performance metrics to detect any unusual activities or bottlenecks. The flow logs that were used for tracking network traffic in Milestone 2 could be configured to monitor the container’s inbound and outbound traffic, ensuring that malicious attempts to access the container are detected. Additionally, integrating an Intrusion Detection System (IDS) could help identify suspicious traffic patterns or attempts to exploit vulnerabilities in the containerized environment.

Lastly, if CloudMart had 10,000 concurrent users, the current architecture would need significant scaling adjustments. One immediate change would be moving from a single ACI instance to a more robust setup involving Azure Kubernetes Service (AKS), which provides horizontal scaling of containers to handle large traffic loads. In addition, using Azure Load Balancer to distribute traffic across multiple containers and implementing auto-scaling for the application would be crucial to maintaining performance and availability under high demand. Additionally, database optimization and the use of caching mechanisms could improve response times and reduce strain on the Cosmos DB.

In summary, Milestone 3 builds on previous milestones by introducing containerization but also highlights the need for enhanced security, monitoring, and scalability when moving to a production-level deployment.


