# Identify data sources
resource "aws_ami" "server_ami" {
  most_recent = true
  owners      = ["099720109477"]

  # Set filters for getting requried AMI
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}