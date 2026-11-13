# Registro dos ciclos TDD — Cálculo de frete

Comando usado em todos os passos: `python -m pytest -q`

| Ciclo | Fase | Teste / mudança | Resultado da suíte |
|---|---|---|---|
| 1 | Red | `calcular_frete(500) == 10` | 1 failed (`NotImplementedError`) |
| 1 | Green | `return 10` (retorno constante) | 1 passed |
| 2 | Red | `calcular_frete(2000) == 20` | 1 failed, 1 passed (`assert 10 == 20`) |
| 2 | Green | `if peso <= 1000: return 10` / `return 20` | 2 passed |
| 3 | Red | `calcular_frete(6000) == 30` | 1 failed, 2 passed (`assert 20 == 30`) |
| 3 | Green | nova condição `if peso <= 5000: return 20` / `return 30` | 3 passed |
| 4 | Fronteiras | parametrização com 1, 1000, 1001, 5000, 5001 | 8 passed (sem alterar o código) |
| 5 | Red | `ValueError` para 0 e -1 | 2 failed, 8 passed (`DID NOT RAISE ValueError`) |
| 5 | Green | guarda `if peso <= 0: raise ValueError` | 10 passed |
| 6 | Red (desafio) | 10.000 g → 30; 10.001 g → `ValueError` | 1 failed, 11 passed (`DID NOT RAISE`) |
| 6 | Green + Refactor | guarda de peso máximo; faixas em tabela | 12 passed |

## Explicação das falhas

- **Ciclo 1:** a função ainda não existia de verdade (`NotImplementedError`), então a falha confirma que o teste foi descoberto e executado.
- **Ciclos 2 e 3:** a falha foi de comportamento, não de ambiente: o código retornava o valor da faixa anterior (10 em vez de 20, depois 20 em vez de 30).
- **Ciclo 5:** a função calculava frete até para peso zero ou negativo; o `pytest.raises` acusou que nenhuma exceção foi lançada.

## Observação sobre o ciclo 4

Os testes de fronteira passaram de primeira. Como orienta a aula, um teste novo que passa sem exigir mudança deve ser investigado. Conferi que as condições usavam `<=` (inclusivo), por isso 1.000 g e 5.000 g já ficavam na faixa correta. Os testes foram mantidos porque protegem contra regressões, por exemplo se alguém trocar `<=` por `<`.

## Decisões de implementação e refatoração

1. **Uso de `<=` em vez de intervalos completos** (`1001 <= peso <= 5000`): como as condições são avaliadas em ordem, basta comparar com o limite superior de cada faixa. Isso evita repetir os limites e reduz o risco de "buracos" entre faixas.
2. **Refatoração final (ciclo 6):** os limites e valores foram extraídos para constantes (`PESO_MINIMO`, `PESO_MAXIMO`, `FAIXAS`). Foi uma refatoração e não uma mudança de regra, porque os 10 testes anteriores continuaram passando sem alteração. A vantagem é que mudar um valor de frete (como no exemplo da regressão, R$ 10 → R$ 12) passa a ser editar um único número na tabela, sem mexer na lógica.
3. **Guardas antes das faixas:** as validações de peso mínimo e máximo ficam no início da função, então nenhum peso inválido chega a ser classificado.
