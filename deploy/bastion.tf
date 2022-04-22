data "aws_ami" "amazon_linux" {
  most_recent = true
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-2.0.20211005.0-x86_64-gp2"]
  }
  owners = ["amazon"]
}

resource "aws_iam_role" "bastion" {
  name               = "${local.prefix}-bastion"
  assume_role_policy = file("${path.module}/templates/bastion/instance-profile-policy.json")

  tags = local.common_tags
}

resource "aws_iam_role_policy_attachment" "bastion_attach_policy" {
  role       = aws_iam_role.bastion.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

resource "aws_iam_instance_profile" "bastion" {
  name = "${local.prefix}-bastion-instance-profile"
  role = aws_iam_role.bastion.name
}


resource "aws_instance" "bastion" {
  ami                  = data.aws_ami.amazon_linux.id
  instance_type        = "t2.micro"
  iam_instance_profile = aws_iam_instance_profile.bastion.name
  user_data            = file("./templates/bastion/user-data.sh")
  # for_each       = true ? toset(var.azs) : toset([])
  # subnet_id      = module.vpc_main.aws_subnet.public[each.key].id
  subnet_id = aws_subnet.public_a.id
  # subnet_id      = module.vpc_main.aws_subnet.public[each.key].id
  #   subnet_id            =module.vpc.subnets1
  # subnet_id            =join("", tolist(module.vpc.subnets1["public_val"])[0])
  key_name = var.bastion_key_name
  vpc_security_group_ids = [
    aws_security_group.bastion.id
  ]

  tags = merge(
    local.common_tags,
    tomap({ Name : "${local.prefix}-bastion" })
  )
}

resource "aws_security_group" "bastion" {
  description = "Control bastion inbound and outbound access"
  name        = "${local.prefix}-bastion"
  vpc_id      = aws_vpc.main.id

  ingress {
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol    = "tcp"
    from_port   = 443
    to_port     = 443
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol    = "tcp"
    from_port   = 80
    to_port     = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 5432
    to_port   = 5432
    protocol  = "tcp"
    cidr_blocks = [
      aws_subnet.private_a.cidr_block,
      aws_subnet.private_b.cidr_block,
    ]
    #  cidr_blocks = [
    #   "10.1.10.0/24",
    #   "10.1.11.0/24",
    # ]
    # cidr_blocks = values(module.vpc.subnets["private_val"])
  }

  tags = local.common_tags
}
