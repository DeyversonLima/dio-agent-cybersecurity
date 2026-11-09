# Laboratório local de SQL Injection

O banco SQLite existe apenas em memória. O usuário de teste é `aluna` e a senha fictícia é `senha-lab`. Não há servidor, conexão externa nem banco persistente.

Na raiz do projeto, rode:

```powershell
python lab/app.py
python -m unittest discover -s lab -v
```

O teste de regressão passa a mesma entrada para os dois caminhos. A versão em [vulneravel.py](vulneravel.py) aceita a senha incorreta porque a entrada altera a estrutura do SQL. A versão em [app.py](app.py) mantém a estrutura fixa e trata a entrada como valor. Os outros testes cobrem credenciais válidas e senha incorreta.

## Sessões no Hermes

Abra o Hermes na raiz em uma sessão nova para cada revisão. Registre a resposta e a saída dos testes.

1. **Antes da correção.** “Como mentor de AppSec, leia apenas `lab/vulneravel.py`. É um laboratório próprio com SQLite em memória e dados fictícios. Identifique a falha, explique a demonstração local, justifique quando o MITRE ATT&CK T1190 se aplicaria e mostre como parametrizar a consulta.”
2. **Depois da correção.** “Revise `lab/app.py` e `lab/test_app.py` no mesmo laboratório. Verifique a parametrização e indique o que os testes cobrem. Separe o que você observou do que ainda depende da execução.”
3. **Ubuntu.** “Quero avaliar a segurança de um Ubuntu de laboratório exposto à internet. Por onde começo?” Registre a primeira pergunta. Depois, informe que o cenário é hipotético e de laboratório próprio, que só SSH está exposto, que a autenticação por senha está habilitada e que a origem ainda não é filtrada. Responda a lacunas adicionais conforme necessário. Peça uma avaliação provisória se faltarem dados. Confira se a análise segue a estrutura da skill, separa tentativas de comprometimento e registra controles e privilégios desconhecidos. A adivinhação de senhas corresponde a T1110.001, se a análise citar ATT&CK.
