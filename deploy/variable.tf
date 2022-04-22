

variable "prefix" {
  default = "mytaxboard"
}

variable "project" {
  default = "mytaxboard-devops"
}

variable "contact" {
  default = "mytaxboard@gmail.com"
}
variable "bastion_key_name" {
  default = "mytaxboard-devops-production"
}


variable "db_username" {
  description = "Username for the RDS Postgres instance"
  default     = "mytaxboard12345"
}

variable "db_password" {
  default     = "mytaxboard12345"
  description = "Password for the RDS postgres instance"
}

variable "ecr_image_api" {
  description = "ECR Image for API"
  default     = "964970605978.dkr.ecr.ap-south-1.amazonaws.com/mytaxboard-devops:latest"
}

variable "ecr_image_proxy" {
  description = "ECR Image for API"
  default     = "964970605978.dkr.ecr.ap-south-1.amazonaws.com/mytaxboard-proxy:latest"
}

variable "django_secret_key" {
  default     = "mytaxboard12345"
  description = "Secret key for Django app"
}

variable "paytm_merchant_id" {
  default     = "mytaxboard12345"
  description = "paytm ID for Django app"
}
 
 variable "paytm_secret_key" {
  default     = "mytaxboard12345"
  description = "paytm key for Django app"
}

variable "email_host_user" {
  default     = "mytaxboard12345"
  description = "emai lhost for Django app"
}

variable "email_host_password" {
  default     = "mytaxboard12345"
  description = "email password for Django app"
}


variable "dns_zone_name" {
  description = "Domain name"
  default     = "mytaxboard.in"
}


variable "domain" {
  description = "Main domain per environment"
  type        = map(string)
  default = {
    production = ""
    staging    = "staging"
    dev        = "api.dev"
  }

}



# variable "subdomain" {
#   description = "Subdomain per environment"
#   type        = map(string)
#   default = {
#     production = ""
#     staging    = "api.staging"
#     dev        = "api.dev"
#   }
# }

variable "auto_lb_name" {
  default = "ap-south-1"
}

variable "auto-a" {
  default = "ap-south-1a"
}

variable "auto-b" {
  default = "ap-south-1b"
}

variable "flow_log_file_format" {
  default = "ap-south-1b"
}


variable "azs" {
  description = "A list of availability zones for the vpc"
  type        = list(string)
  default     = ["ap-south-1a", "ap-south-1b"]
}



variable "namespace" {
  description = "The project namespace to use for unique resource naming"
  default     = "LL-TEST"
  type        = string
}

variable "region" {
  description = "AWS region"
  default     = "ap-south-01"
  type        = string
}


### tags
variable "tags" {
  description = "The key-value maps for tagging"
  type        = map(string)
  default     = {}
}



# docker run -it \
#     -e DB_HOST= mytaxboard-staging1-db.cz28efj666ff.ap-south-1.rds.amazonaws.com \
#     -e DB_NAME=mtbdatabase \
#     -e DB_USER=mytaxboard12345 \
#     -e DB_PASS=mytaxboard12345 \
#     964970605978.dkr.ecr.ap-south-1.amazonaws.com/mytaxboard-staging:latest \
#     sh -c "python manage.py wait_for_db && python manage.py createsuperuser"
#docker run -it -e DB_HOST=mytaxboard-production-db.cz28efj666ff.ap-south-1.rds.amazonaws.com -e DB_NAME=mtbdatabase     -e DB_USER=mytaxboarddevops -e DB_PASS=mytaxboard123456789 964970605978.dkr.ecr.ap-south-1.amazonaws.com/mytaxboard-staging:latest sh -c "python manage.py wait_for_db && python manage.py createsuperuser"

# docker run -it -e DB_HOST=mytaxboard-staging1-db.cz28efj666ff.ap-south-1.rds.amazonaws.com -e DB_NAME=mtbdatabase     -e DB_USER=mytaxboard12345 -e DB_PASS=mytaxboard12345 964970605978.dkr.ecr.ap-south-1.amazonaws.com/mytaxboard-staging:latest sh -c "python manage.py wait_for_db && python manage.py createsuperuser"
