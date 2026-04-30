
> [!NOTE]
> Todos os passos abaixo eu fiz e deram certo, se vc é burro a culpa não é minha. Talvez T.I. não seja sua praia. 

# Como subir os serviços necessários?
## Instale o docker
### Execute os comandos:
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Adicione o repositório do Docker na lista de sources do Ubuntu:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Dê permissão para rodar o Docker com seu usuário corrente:
```bash
sudo usermod -aG docker $USER
```

### Inicie o serviço:
```bash
sudo service docker start
```

### Reinicie sua maquina:
```bash
sudo reboot
```

### Clone o repositório [Mentorstec_infra] (Calma que ainda estará em repositório separado, ainda não deu tempo!! )

> [!CAUTION]
> Vamos assumir que vc sabe o que está fazendo!!

1. Dentro da pasta `infra` existe um arquivo `Makefile` reponsável por construir todos os serviços. Altere os nomes e tags das imagens conforme necessidade.

2. Construir a imagem do Airflow:
```bash 
make build-airflow
```

3. Construir a imagem do Embulk:
```bash
make build-embulk
```

4. Subir containers do Airflow:
```bash 
make compose-up-airflow`
```

5. Subir container do Embulk:
```bash 
make compose-up-embulk`
```

6. Subir demais containers (Dremio, Minio, Nessie) :
```bash 
make compose-up-services`
```

7. Construir TODAS as imagens:
```bash 
make build`
```

8. Subir TODOS os serviços:
```bash
Make compose-up
```

