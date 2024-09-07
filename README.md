
# Gerador de Senhas Seguras - Aplicação Web com Flask

Este projeto é uma aplicação web simples para gerar senhas seguras. O usuário pode definir o comprimento da senha e personalizar os tipos de caracteres incluídos (letras maiúsculas, letras minúsculas, números e símbolos).

## Funcionalidades

- Definir o comprimento da senha (entre 4 e 32 caracteres).
- Escolher entre incluir/excluir letras maiúsculas, minúsculas, números e símbolos.
- Geração de senhas aleatórias seguras diretamente no navegador.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para a lógica de geração de senhas.
- **Flask**: Framework web para o backend da aplicação.
- **HTML/CSS**: Interface web simples e funcional.
- **random, string**: Bibliotecas do Python utilizadas para gerar as senhas.

## Instalação

### Pré-requisitos

- Python 3.x instalado no seu ambiente.
- Biblioteca Flask instalada. Para isso, execute o seguinte comando:

    ```bash
    pip install flask
    ```

### Rodando a aplicação

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/gerador-de-senhas.git
```

## Navegue até o diretório do projeto:

```bash
cd gerador-de-senhas
```

## Execute a aplicação:

```bash
python app.py
```

## Acesse a aplicação no seu navegador em [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Estrutura do Projeto:

```php
gerador-de-senhas/
│
├── app.py              # Arquivo principal com a lógica do backend (Flask)
├── templates/          # Pasta para templates HTML
│   └── index.html      # Página principal da aplicação
└── static/             # Pasta para arquivos estáticos (CSS/JS)
    └── style.css       # Estilo básico da página (opcional)
```

## Personalização

Você pode facilmente personalizar as opções de geração de senha, modificando as opções no arquivo `app.py`, como o comprimento padrão da senha ou habilitar/desabilitar certos tipos de caracteres.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, novas funcionalidades ou correções. Para isso:

1. Faça um fork do projeto.
2. Crie uma nova branch:

    ```bash
    git checkout -b minha-melhoria
    ```

3. Envie suas mudanças:

    ```bash
    git add .
    git commit -m "Adicionando minha melhoria"
    git push origin minha-melhoria
    ```

4. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a MIT License.
