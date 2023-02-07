# Diagrams lets you draw the cloud system architecture in Python code.
# Diagram as Code allows you to track the architecture diagram changes in any version control system.
# https://diagrams.mingrammer.com

from diagrams import Cluster, Diagram
from diagrams.aws.general import Client
from diagrams.aws.compute import EC2Instance
from diagrams.aws.analytics import CloudsearchSearchDocuments
from diagrams.aws.management import SystemsManagerDocuments
from diagrams.aws.network import InternetGateway
from diagrams.aws.network import RouteTable

with Diagram("", show=False):
    with Cluster("GitHub"):
        with Cluster("Bootstrap script"):
            bootstrap = CloudsearchSearchDocuments("userdata.tpl")

        with Cluster("Terraform configs"):
            configs = SystemsManagerDocuments("*.tf")
        
    local_machine = Client("Workstation")
    
    with Cluster("VPC"):
        IGW = InternetGateway("Internet Gateway")
        public_route_table = RouteTable("Public Route Table")
        
        with Cluster("Security Group"):
            with Cluster("Public Subnet"):
                ec2_instance = EC2Instance("Dev Node")
    
    local_machine >> IGW >> public_route_table >> ec2_instance
    configs >> local_machine
    bootstrap >> ec2_instance