# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

import pem
from cryptography import x509
from cryptography.hazmat.backends import default_backend

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"


def print_perms(filename: str):
    pem_data = pem.parse_file(filename)

    cert = x509.load_pem_x509_certificate(pem_data[0].as_bytes(), default_backend())
    #Print the subject of the certificate
    print(cert.subject)
    #print the content of the certificate
    print(pem_data[0].as_text())