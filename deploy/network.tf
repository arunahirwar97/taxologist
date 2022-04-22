# resource "aws_vpc" "main" {
#   cidr_block           = "10.1.0.0/16"
#   enable_dns_support   = true
#   enable_dns_hostnames = true

#   # tags = merge(
#   #   local.common_tags,
#   #   map("Name", "${local.prefix}-vpc")
#   # )
# }
# ############ Internet gateway ###########
# resource "aws_internet_gateway" "main" {
#   vpc_id = aws_vpc.main.id

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-main" })
#   )
# }

# #####################################################
# # Public Subnets  #
# #####################################################
# resource "aws_subnet" "public_a" {
#   cidr_block              = "10.1.1.0/24"
#   map_public_ip_on_launch = true
#   vpc_id                  = aws_vpc.main.id
#   availability_zone       = "${data.aws_region.current.name}a"

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-public-a" })
#   )
# }
# resource "aws_subnet" "public_b" {
#   cidr_block              = "10.1.2.0/24"
#   map_public_ip_on_launch = true
#   vpc_id                  = aws_vpc.main.id
#   availability_zone       = "${data.aws_region.current.name}b"

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-public-b" })
#   )
# }
# ##############Public Route Table #########
# #####################################

# resource "aws_route_table" "public" {
#   vpc_id = aws_vpc.main.id

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-public" })
#   )
# }


# #######################################

# resource "aws_route_table_association" "public_a" {
#   subnet_id      = aws_subnet.public_a.id
#   route_table_id = aws_route_table.public.id
# }


# resource "aws_route_table_association" "public_b" {
#   subnet_id      = aws_subnet.public_b.id
#   route_table_id = aws_route_table.public.id
# }


# ################ Nat Gateway ######################

# resource "aws_nat_gateway" "public" {
#   allocation_id = aws_eip.public.id
#   subnet_id     = aws_subnet.public_a.id
#   depends_on    = [aws_eip.public]
#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-public-a" })

#   )
# }


# resource "aws_route" "private_a_internet_out" {
#   route_table_id         = aws_route_table.private.id
#   nat_gateway_id         = aws_nat_gateway.public.id
#   destination_cidr_block = "0.0.0.0/0"
# }

# ################ Nat Gateway ######################

# ###################################################
# # Private Subnets #
# ###################################################
# resource "aws_subnet" "private_a" {
#   cidr_block        = "10.1.10.0/24"
#   vpc_id            = aws_vpc.main.id
#   availability_zone = "${data.aws_region.current.name}a"

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-private-a" })
#   )
# }

# resource "aws_subnet" "private_b" {
#   cidr_block        = "10.1.11.0/24"
#   vpc_id            = aws_vpc.main.id
#   availability_zone = "${data.aws_region.current.name}b"

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-private-b" })
#   )
# }

# ##############Private Route Table #########
# ###########################################
# resource "aws_route_table" "private" {
#   vpc_id = aws_vpc.main.id

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-private" })
#   )
# }

# ############################################

# resource "aws_route_table_association" "private_a" {
#   subnet_id      = aws_subnet.private_a.id
#   route_table_id = aws_route_table.private.id
# }

# resource "aws_route_table_association" "private_b" {
#   subnet_id      = aws_subnet.private_b.id
#   route_table_id = aws_route_table.private.id
# }



# ###############################################

# ################# Elastic IP ##################


# resource "aws_eip" "public" {
#   vpc                       = true
#   associate_with_private_ip = "10.0.0.5"
#   depends_on                = [aws_internet_gateway.main]

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-public" })
#   )
# }


# #############################################

# ##################################################
# #######################Public Access Subnet ######

# resource "aws_route" "public_internet_access" {
#   route_table_id         = aws_route_table.public.id
#   destination_cidr_block = "0.0.0.0/0"
#   gateway_id             = aws_internet_gateway.main.id
# }

# ##########################################################



resource "aws_vpc" "main" {
  cidr_block           = "10.1.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  # tags = merge(
  #   local.common_tags,
  #   map("Name", "${local.prefix}-vpc")
  # )
}
############ Internet gateway ###########
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-main" })
  )
}

#####################################################
# Public Subnets  #
#####################################################
resource "aws_subnet" "public_a" {
  cidr_block              = "10.1.1.0/24"
  map_public_ip_on_launch = true
  vpc_id                  = aws_vpc.main.id
  availability_zone       = "${data.aws_region.current.name}a"

  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-public-a" })
  )
}
resource "aws_subnet" "public_b" {
  cidr_block              = "10.1.2.0/24"
  map_public_ip_on_launch = true
  vpc_id                  = aws_vpc.main.id
  availability_zone       = "${data.aws_region.current.name}b"

  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-public-b" })
  )
}

##############Public Route Table #########
#####################################

resource "aws_route_table" "public_a" {
  vpc_id = aws_vpc.main.id

  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-public" })
  )
}


resource "aws_route_table" "public_b" {
  vpc_id = aws_vpc.main.id

  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-public -public_b" })
  )
}

#######################################

resource "aws_route_table_association" "public_a" {
  subnet_id      = aws_subnet.public_a.id
  route_table_id = aws_route_table.public_a.id
}


resource "aws_route_table_association" "public_b" {
  subnet_id      = aws_subnet.public_b.id
  route_table_id = aws_route_table.public_b.id
}


# ################  Start Nat Gateway ######################


resource "aws_security_group" "vpc" {
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
    protocol    = "tcp"
    description = "Allow communication to Snowflake OSCP URL"
  }

  ingress {
    from_port   = 443
    to_port     = 443
    cidr_blocks = ["0.0.0.0/0"]
    protocol    = "tcp"
    description = "Allow communication to Snowflake Account URL"
  }
}


resource "aws_vpc_endpoint" "s3" {
  vpc_id       = aws_vpc.main.id
  service_name = "com.amazonaws.ap-south-1.s3"
  # service_name      = "com.amazonaws.${data.aws_region.current.name}.s3"
  vpc_endpoint_type = "Gateway"
  route_table_ids   = [aws_route_table.private_a.id,aws_route_table.private_b.id]

  tags = {
    Name = "VCPendpoint S3"
  }
}


resource "aws_vpc_endpoint" "ecr-dkr" {
  vpc_id       = aws_vpc.main.id
  service_name = "com.amazonaws.ap-south-1.ecr.dkr"
  # service_name      = "com.amazonaws.${data.aws_region.current.name}.ecr.dkr"
  vpc_endpoint_type = "Interface"

  # security_group_ids = [aws_security_group.vpce.id]

  security_group_ids = [aws_security_group.vpc.id]

  subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_b.id]

  private_dns_enabled = true

  tags = {
    Name = "VCPendpoint ecr dkr "
  }
}


resource "aws_vpc_endpoint" "ecr-api" {
  vpc_id              = aws_vpc.main.id
  private_dns_enabled = true
  service_name        = "com.amazonaws.ap-south-1.ecr.api"
  # service_name        = "com.amazonaws.${var.region}.api"
  vpc_endpoint_type  = "Interface"
  security_group_ids = [aws_security_group.vpc.id]

  subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_b.id]

  tags = {
    Name = "VCPendpoint ecr-api"
  }
}


resource "aws_vpc_endpoint" "logs" {
  vpc_id              = aws_vpc.main.id
  private_dns_enabled = true
  service_name        = "com.amazonaws.ap-south-1.logs"
  # service_name        = "com.amazonaws.${data.aws_region.current.name}.logs"
  vpc_endpoint_type  = "Interface"
  security_group_ids = [aws_security_group.vpc.id]
  subnet_ids         = [aws_subnet.private_a.id, aws_subnet.private_b.id]

  tags = {
    Name = "VCPendpoint logs"
  }
}

# resource "aws_route" "private_a_internet_out" {
#     route_table_id  = aws_route_table.private.id
#     vpc_endpoint_id = module.ecr.id
# #   # nat_gateway_id         = aws_nat_gateway.public.id
#     destination_cidr_block = "0.0.0.0/0"
# }
# /* resource "aws_security_group" "vpce" {
#   name   = "vpce"
#   vpc_id = aws_vpc.main.id
#   ingress {
#     from_port   = 443
#     to_port     = 443
#     protocol    = "tcp"
#     cidr_blocks = [aws_vpc.main.cidr_block]
#   }
#   tags = {
#     Environment = "dev"
#   }
# }
# resource "aws_vpc_endpoint" "s3" {
#   vpc_id            = aws_vpc.main.id
#   service_name      = "com.amazonaws.${data.aws_region.current.name}.s3"
#   vpc_endpoint_type = "Gateway"
#   route_table_ids   = [aws_route_table.private.id]

#   tags = {
#     Name        = "s3-endpoint"
#     Environment = "dev"
#   }
# }

# resource "aws_vpc_endpoint" "dkr" {
#   vpc_id              = aws_vpc.main.id
#   private_dns_enabled = true
#   service_name        = "com.amazonaws.${data.aws_region.current.name}.ecr.dkr"
#   vpc_endpoint_type   = "Interface"
#   security_group_ids = [
#     aws_security_group.vpce.id,
#   ]
#   subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_b.id]

#   tags = {
#     Name        = "dkr-endpoint"
#     Environment = "dev"
#   }
# }

#  */
# ################ Close Nat Gateway ######################

# ###################################################
# # Private Subnets #
# ###################################################
resource "aws_subnet" "private_a" {
  cidr_block        = "10.1.10.0/24"
  vpc_id            = aws_vpc.main.id
  availability_zone = "${data.aws_region.current.name}a"

  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-private-a" })
  )
}

resource "aws_subnet" "private_b" {
  cidr_block        = "10.1.11.0/24"
  vpc_id            = aws_vpc.main.id
  availability_zone = "${data.aws_region.current.name}b"

  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-private-b" })
  )
}

##############Private Route Table #########
###########################################
resource "aws_route_table" "private_a" {
  vpc_id = aws_vpc.main.id
  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-private-a" })
  )
}

resource "aws_route_table" "private_b" {
  vpc_id = aws_vpc.main.id
  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-private_b-" })
  )
}
############################################

resource "aws_route_table_association" "private_a" {
  subnet_id      = aws_subnet.private_a.id
  route_table_id = aws_route_table.private_a.id
}

resource "aws_route_table_association" "private_b" {
  subnet_id      = aws_subnet.private_b.id
  route_table_id = aws_route_table.private_b.id
}



###############################################

################# Elastic IP ##################


# resource "aws_eip" "public" {
#   vpc                       = true
#   associate_with_private_ip = "10.0.0.5"
#   # depends_on                = [aws_vpc_endpoint.ecr]

#   tags = merge(
#     local.common_tags,
#     tomap({ Name : "${local.prefix}-public" })
#   )
# }


#############################################

##################################################
#######################Public Access Subnet ######

resource "aws_route" "public_internet_access_a" {
  route_table_id         = aws_route_table.public_a.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.main.id
}

resource "aws_route" "public_internet_access_b" {
  route_table_id         = aws_route_table.public_b.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.main.id
}

# ##########################################################






