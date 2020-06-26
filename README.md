Certificate Playground
======================

**OpenSSL を使用してクライアント証明書を作成する**

```
$ openssl genrsa -out ca.key 2048

$ openssl req -x509 -new -nodes -key ca.key -sha256 -days 1024 -out cacert.pem

$ openssl genrsa -out client.key 2048

$ openssl req -new -key client.key -out client.csr

$ openssl x509 -req -in client.csr -CA cacert.pem \
    -CAkey ca.key -CAcreateserial \
    -out clientcert.pem -days 500 -sha256
```

**作成されたクライアント証明書の署名方式**

```
$ openssl x509 -text -in clientcert.pem
# `Signature Algorithm` が XXXwithRSAEncryption だと PKCS#1 v1.5 署名である
```

内部的には `signatureAlgorithm` で定義され、 `tbsCertificate` を署名している
cf. https://tools.ietf.org/html/rfc5280.html#section-4.1.1
