# Instalando UV

primeiro é necessario criar uma pasta vazia pr começar o processo.

1. entramos no seguinte site 
    https://github.com/astral-sh/uv

    uv: gerenciador de pacotes e projetos, ele permite manter a configuração de um projeto separada de outro projeto

OBS: o melhor seria instalar o uv pelo curl, mas se não for possivel intalamos como explicado abaixo

2. intalamos o pip, para instalar o uv

    $sudo apt install python3-pip

3. instalamos o uv

    $pip install uv

4. agora instalamos o uv pelo snap

    $sudo snap install astral-uv --classic

# Executando UV

1. executamos

    $uv help init

2. depois

    $uv init --bare 

3. instalamos a extenção do vscode "python" do microsoft e "toml" para o arquivo criado por uv 

4. depois executamos

    $uv sync

    para criar um ambiente virtual com as especificações do pyproject.toml, toda vez que modifiquemos o ambiente virtual teremos que executar o $(uv sync)

5. para acresentar dependencias podemos utilizar

    $uv add <dependencia>
    ex: $uv add numpy

    isso fara com que a dependencia numpy seja baixada e acresentada automaticamente no arquivo pyproject.toml 


Para executar nosso venv diretamente no terminal, executamos:

    source /<nome do ambiente>/bin/activate.<terminal>