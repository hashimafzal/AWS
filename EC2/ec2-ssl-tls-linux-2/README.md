# [Tutorial: Configure SSL/TLS on Amazon Linux 2022](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2022.html)

- Connecting through ssh:
```bash
ssh -i ec2-ssl-tls-linux-2-key.pem ec2-user@ec2-54-147-144-140.compute-1.amazonaws.com
```
- Update packages: `sudo yum update -y`
- Install Apache server: `sudo yum install -y httpd`
- Start the server: `sudo systemctl start httpd`
- Verify its running: `sudo systemctl is-enabled httpd`
- Install TLS support for apache server: `sudo yum install -y mod_ssl`
    - Once this runs your instance now has the following files that you use to configure your secure server and create a certificate for testing:
        - /etc/httpd/conf.d/ssl.conf: The configuration file for mod_ssl. It contains directives telling Apache where to find encryption keys and certificates, the TLS protocol versions to allow, and the encryption ciphers to accept.
        - /etc/pki/tls/certs/make-dummy-cert: A script to generate a self-signed X.509 certificate and private key for your server host. This certificate is useful for testing that Apache is properly set up to use TLS. Because it offers no proof of identity, it should not be used in production. If used in production, it triggers warnings in Web browsers.
- Go into /etc/pki/tls/certs and run `sudo ./make-dummy-cert localhost.crt`. This generates a new file localhost.crt. This file contains both a self-signed certificate and the certificate's private key. Apache requires the certificate and key to be in PEM format, which consists of Base64-encoded ASCII characters.
- Open the /etc/httpd/conf.d/ssl.conf and comment out the following line: SSLCertificateKeyFile /etc/pki/tls/private/localhost.key. 
- Restart Apache: `sudo systemctl restart httpd` 
- Your are set to access the page through https on port 443.Because you are connecting to a site with a self-signed, untrusted host certificate, your browser may display a series of security warnings. 