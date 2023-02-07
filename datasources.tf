# Identify data sources
data "aws_ami" "server_ami" {
  most_recent = true
  owners      = ["137112412989"]

  # Set filters for getting requried AMI
  filter {
    name   = "name"
    values = ["amzn2-ami-kernel-5.10-hvm-2.0.20230119.1-x86_64-gp2"]
  }
}