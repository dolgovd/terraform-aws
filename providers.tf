terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
    # profile                  = "vscode"
    region                   = "us-east-1"
    shared_credentials_files = ["~/.aws/credentials"]
}