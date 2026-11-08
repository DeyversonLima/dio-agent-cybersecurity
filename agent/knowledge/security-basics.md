# Fundamentos de segurança

- **Vulnerabilidade** é uma fraqueza no código, na configuração ou no processo.
- **Ameaça** é uma causa potencial de dano, como uma pessoa tentando contornar um login.
- **Risco** combina a possibilidade de um evento danoso e suas consequências no contexto do ativo. Exposição, pré-requisitos e controles influenciam essa avaliação.

## Confidencialidade, integridade e disponibilidade

| Propriedade | Pergunta para a análise |
|---|---|
| Confidencialidade | Quem poderia ler dados que deveriam ser restritos? |
| Integridade | Quem poderia modificar dados ou configurações sem autorização? |
| Disponibilidade | Que serviço poderia ficar inacessível e para quem? |

## Práticas defensivas

- Delimite o escopo e use dados fictícios em laboratório.
- Separe instruções SQL de valores com consultas parametrizadas.
- Aplique privilégio mínimo, atualizações, controle de exposição e autenticação adequada.
- Trate senhas de aplicações reais com hash apropriado. O login em memória deste projeto usa valores fictícios para isolar o efeito da parametrização.
- Preserve evidências sem expor segredos. Repita o teste original após a correção e confirme o funcionamento normal.
- Use o [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/) quando o cenário envolver exploração de uma aplicação exposta publicamente para acesso inicial. Descreva a fraqueza no código separadamente da técnica de ataque.
