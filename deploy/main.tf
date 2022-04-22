terraform {
  backend "s3" {
    bucket         = "mytaxboard-devops-tf-state"
    key            = "mytaxboard.tfstate"
    region         = "ap-south-1"
    encrypt        = true
    dynamodb_table = "mytaxboard-devops-tf-state-lock"
  }
}

provider "aws" {
  region = "ap-south-1"
}


locals {
  prefix = "${var.prefix}-${terraform.workspace}"
}


locals {
  common_tags = {
    Environment = terraform.workspace
    Project     = var.project
    Owner       = var.contact
    ManagedBy   = "Terraform"
  }
}

data "aws_region" "current" {}




