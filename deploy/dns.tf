data "aws_route53_zone" "zone" {
  name = "${var.dns_zone_name}."
}

data "aws_elb_hosted_zone_id" "main" {}


resource "aws_route53_record" "mytaxboard" {
  zone_id = data.aws_route53_zone.zone.zone_id
  name    = "${lookup(var.domain, terraform.workspace)}${data.aws_route53_zone.zone.name}"
  type    = "A"

  alias {
    name                   = aws_lb.api.dns_name
    zone_id                = data.aws_elb_hosted_zone_id.main.id
    evaluate_target_health = true
  }

}

resource "aws_acm_certificate" "cert" {
  domain_name       = aws_route53_record.mytaxboard.fqdn
  validation_method = "DNS"

  tags = local.common_tags

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route53_record" "cert_validation" {
  name    = tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_name
  type    = tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_type
  zone_id = data.aws_route53_zone.zone.zone_id
  records = [
    tolist(aws_acm_certificate.cert.domain_validation_options)[0].resource_record_value
  ]
  ttl = "60"
}

resource "aws_acm_certificate_validation" "cert" {
  certificate_arn         = aws_acm_certificate.cert.arn
  validation_record_fqdns = [aws_route53_record.cert_validation.fqdn]
}