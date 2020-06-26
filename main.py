from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


with open('./clientcert.pem', 'rb') as f:
    pem_data = f.read()
    clientcert = x509.load_pem_x509_certificate(pem_data, default_backend())


from cryptography.hazmat.primitives.serialization import load_pem_public_key


with open('./cacert.pem', 'rb') as f:
    pem_data = f.read()
    cacert = x509.load_pem_x509_certificate(pem_data, default_backend())
    public_key = cacert.public_key()


public_key.verify(
    signature=clientcert.signature,
    data=clientcert.tbs_certificate_bytes,
    padding=padding.PKCS1v15(),
    algorithm=clientcert.signature_hash_algorithm,
)
