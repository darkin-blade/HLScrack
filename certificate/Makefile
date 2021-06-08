NAME=localhost

run1:
	echo ${NAME}
	# 创建认证中心, Certificate Authority(CA)
	openssl genrsa -des3 -out myCA.key 2048
	openssl req -x509 -new -nodes -key myCA.key -sha256 -days 825 -out myCA.pem
	# 域名列表
	make write
	# 创建证书
	openssl genrsa -out ${NAME}.key 2048
	openssl req -new -key ${NAME}.key -out ${NAME}.csr
	openssl x509 -req -in ${NAME}.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial -out ${NAME}.crt -days 825 -sha256 -extfile ${NAME}.ext

write:
	@echo "authorityKeyIdentifier=keyid,issuer" > ${NAME}.ext
	@echo "basicConstraints=CA:FALSE" >> ${NAME}.ext
	@echo "keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment" >> ${NAME}.ext
	@echo "subjectAltName = @alt_names" >> ${NAME}.ext
	@echo "[alt_names]" >> ${NAME}.ext
	@echo "DNS.1 = ${NAME}" >> ${NAME}.ext
	# DNS.2 = xxx
	# IP.1 = 
	
verify:
	openssl verify -CAfile myCA.pem -verify_hostname ${NAME} ${NAME}.crt
