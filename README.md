# Projeto QA Swag Labs com Selenium e Python

Automacao de testes end-to-end para o site Swag Labs, usando Selenium WebDriver,
Pytest e Page Object Model.

## Objetivo

Validar os principais fluxos do Swag Labs:

- Login com dados validos e invalidos.
- Adicao de produtos ao carrinho.
- Validacao de produtos no carrinho.
- Remocao de produtos.
- Acesso ao checkout.
- Validacao de campos obrigatorios no checkout.
- Validacao de calculo no resumo da compra.
- Finalizacao da compra.
- Retorno para a loja apos compra concluida.

## Tecnologias

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- Chrome WebDriver gerenciado pelo Selenium

## Estrutura do projeto

```text
.
|-- conftest.py
|-- pages/
|   |-- __init__.py
|   |-- cart_page.py
|   |-- checkout_page.py
|   |-- complete_page.py
|   |-- finish_page.py
|   |-- login_page.py
|   `-- products_page.py
|-- tests/
|   |-- test_cart.py
|   |-- test_checkout.py
|   |-- test_complete.py
|   |-- test_finish.py
|   |-- test_login.py
|   `-- test_products.py
|-- requirements.txt
|-- README.md
`-- LICENSE
```

## Organizacao

### `conftest.py`

Arquivo responsavel pela configuracao do navegador e pelos fixtures usados nos
testes.

Principais fixtures:

- `driver`: abre o Chrome, acessa `https://www.saucedemo.com/`, maximiza a tela
  e fecha o navegador ao final do teste.
- `usuario_login`: realiza login com `standard_user` e `secret_sauce`.
- `usuario_products`: reutiliza o usuario logado na pagina de produtos.
- `usuario_cart`: abre o carrinho.
- `usuario_checkout`: acessa o checkout step one.
- `usuario_finish`: monta o fluxo com todos os produtos ate o checkout overview.
- `usuario_finish_produto`: monta o fluxo com um produto parametrizado.
- `usuario_complete`: finaliza a compra e acessa a pagina de conclusao.

### `pages/`

Camada Page Object Model. Cada arquivo concentra acoes e validacoes de uma tela:

- `login_page.py`: login e mensagens de erro.
- `products_page.py`: produtos, botao Add to Cart, retorno para listagem,
  contador do carrinho e acesso ao carrinho.
- `cart_page.py`: validacao de itens, remocao, checkout e continue shopping.
- `checkout_page.py`: preenchimento do formulario e validacao de erros.
- `finish_page.py`: subtotal, taxa, total e finalizacao da compra.
- `complete_page.py`: titulo da pagina final e botao Back Home.

### `tests/`

Camada de testes automatizados:

- `test_login.py`: cenarios de login valido e invalido.
- `test_products.py`: adicao de produtos pela pagina de produtos.
- `test_cart.py`: validacao, remocao e navegacao pelo carrinho.
- `test_checkout.py`: formulario de checkout e campos obrigatorios.
- `test_finish.py`: validacao de subtotal, taxa e total.
- `test_complete.py`: pagina de compra concluida.

## Como executar

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Execute todos os testes:

```bash
python -m pytest
```

Liste os testes coletados:

```bash
python -m pytest --collect-only -q
```

## Total de testes

O projeto possui **43 casos de teste documentados**, seguindo a mesma coleta do
Pytest.

## Produtos usados nos testes

- Sauce Labs Backpack
- Sauce Labs Bike Light
- Sauce Labs Bolt T-Shirt
- Sauce Labs Fleece Jacket
- Sauce Labs Onesie
- Test.allTheThings() T-Shirt (Red)

## Casos de teste

### CT-01: Validar Sauce Labs Backpack no carrinho

**Arquivo:** `tests/test_cart.py::test_cart_one_product[Sauce Labs Backpack]`

**Descricao:** Confirmar que o produto Sauce Labs Backpack aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Backpack ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** Sauce Labs Backpack aparece no carrinho.

### CT-02: Validar Sauce Labs Bike Light no carrinho

**Arquivo:** `tests/test_cart.py::test_cart_one_product[Sauce Labs Bike Light]`

**Descricao:** Confirmar que o produto Sauce Labs Bike Light aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Bike Light ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** Sauce Labs Bike Light aparece no carrinho.

### CT-03: Validar Sauce Labs Bolt T-Shirt no carrinho

**Arquivo:** `tests/test_cart.py::test_cart_one_product[Sauce Labs Bolt T-Shirt]`

**Descricao:** Confirmar que o produto Sauce Labs Bolt T-Shirt aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Bolt T-Shirt ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** Sauce Labs Bolt T-Shirt aparece no carrinho.

### CT-04: Validar Sauce Labs Fleece Jacket no carrinho

**Arquivo:** `tests/test_cart.py::test_cart_one_product[Sauce Labs Fleece Jacket]`

**Descricao:** Confirmar que o produto Sauce Labs Fleece Jacket aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Fleece Jacket ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** Sauce Labs Fleece Jacket aparece no carrinho.

### CT-05: Validar Sauce Labs Onesie no carrinho

**Arquivo:** `tests/test_cart.py::test_cart_one_product[Sauce Labs Onesie]`

**Descricao:** Confirmar que o produto Sauce Labs Onesie aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Onesie ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** Sauce Labs Onesie aparece no carrinho.

### CT-06: Validar Test.allTheThings() T-Shirt (Red) no carrinho

**Arquivo:** `tests/test_cart.py::test_cart_one_product[Test.allTheThings() T-Shirt (Red)]`

**Descricao:** Confirmar que o produto Test.allTheThings() T-Shirt (Red) aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Test.allTheThings() T-Shirt (Red) ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** Test.allTheThings() T-Shirt (Red) aparece no carrinho.

### CT-07: Validar todos os produtos no carrinho

**Arquivo:** `tests/test_cart.py::test_add_all_products`

**Descricao:** Confirmar que todos os produtos adicionados aparecem no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar todos os produtos ao carrinho.
3. Acessar o carrinho.
4. Validar os produtos exibidos.

**Resultado esperado:** Todos os 6 produtos aparecem no carrinho.

### CT-08: Remover Sauce Labs Backpack do carrinho

**Arquivo:** `tests/test_cart.py::test_remove_one_product[Sauce Labs Backpack]`

**Descricao:** Validar remocao do produto Sauce Labs Backpack no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Backpack ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-09: Remover Sauce Labs Bike Light do carrinho

**Arquivo:** `tests/test_cart.py::test_remove_one_product[Sauce Labs Bike Light]`

**Descricao:** Validar remocao do produto Sauce Labs Bike Light no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Bike Light ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-10: Remover Sauce Labs Bolt T-Shirt do carrinho

**Arquivo:** `tests/test_cart.py::test_remove_one_product[Sauce Labs Bolt T-Shirt]`

**Descricao:** Validar remocao do produto Sauce Labs Bolt T-Shirt no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Bolt T-Shirt ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-11: Remover Sauce Labs Fleece Jacket do carrinho

**Arquivo:** `tests/test_cart.py::test_remove_one_product[Sauce Labs Fleece Jacket]`

**Descricao:** Validar remocao do produto Sauce Labs Fleece Jacket no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Fleece Jacket ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-12: Remover Sauce Labs Onesie do carrinho

**Arquivo:** `tests/test_cart.py::test_remove_one_product[Sauce Labs Onesie]`

**Descricao:** Validar remocao do produto Sauce Labs Onesie no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Onesie ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-13: Remover Test.allTheThings() T-Shirt (Red) do carrinho

**Arquivo:** `tests/test_cart.py::test_remove_one_product[Test.allTheThings() T-Shirt (Red)]`

**Descricao:** Validar remocao do produto Test.allTheThings() T-Shirt (Red) no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar Test.allTheThings() T-Shirt (Red) ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-14: Remover todos os produtos do carrinho

**Arquivo:** `tests/test_cart.py::test_remove_all_products`

**Descricao:** Validar remocao de todos os produtos no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar todos os produtos ao carrinho.
3. Acessar o carrinho.
4. Remover todos os produtos.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-15: Voltar do carrinho para a loja

**Arquivo:** `tests/test_cart.py::test_back_page`

**Descricao:** Validar o botao Continue Shopping.

**Passos:**
1. Fazer login.
2. Acessar o carrinho.
3. Clicar em Continue Shopping.

**Resultado esperado:** Usuario retorna para `inventory.html`.

### CT-16: Acessar checkout pelo carrinho

**Arquivo:** `tests/test_cart.py::test_continue_with_item`

**Descricao:** Validar que o botao Checkout direciona para o formulario de checkout.

**Passos:**
1. Fazer login.
2. Acessar o carrinho.
3. Clicar em Checkout.

**Resultado esperado:** Usuario e direcionado para `checkout-step-one.html`.

### CT-17: Checkout com informacoes validas

**Arquivo:** `tests/test_checkout.py::test_info_valid`

**Descricao:** Validar preenchimento correto das informacoes do checkout.

**Passos:**
1. Fazer login.
2. Acessar o carrinho.
3. Acessar o checkout.
4. Preencher First Name, Last Name e Postal Code.
5. Clicar em Continue.

**Resultado esperado:** Usuario e direcionado para `checkout-step-two.html`.

### CT-18: Checkout sem First Name

**Arquivo:** `tests/test_checkout.py::test_info_invalid[-valid-valido-Error: First Name is required]`

**Descricao:** Validar obrigatoriedade do campo First Name.

**Passos:**
1. Acessar o checkout.
2. Deixar First Name vazio.
3. Preencher Last Name e Postal Code.
4. Clicar em Continue.

**Resultado esperado:** Sistema exibe `Error: First Name is required`.

### CT-19: Checkout sem Last Name

**Arquivo:** `tests/test_checkout.py::test_info_invalid[valid--valid-Error: Last Name is required]`

**Descricao:** Validar obrigatoriedade do campo Last Name.

**Passos:**
1. Acessar o checkout.
2. Preencher First Name.
3. Deixar Last Name vazio.
4. Preencher Postal Code.
5. Clicar em Continue.

**Resultado esperado:** Sistema exibe `Error: Last Name is required`.

### CT-20: Checkout sem Postal Code

**Arquivo:** `tests/test_checkout.py::test_info_invalid[valid-valid--Error: Postal Code is required]`

**Descricao:** Validar obrigatoriedade do campo Postal Code.

**Passos:**
1. Acessar o checkout.
2. Preencher First Name e Last Name.
3. Deixar Postal Code vazio.
4. Clicar em Continue.

**Resultado esperado:** Sistema exibe `Error: Postal Code is required`.

### CT-21: Cancelar checkout

**Arquivo:** `tests/test_checkout.py::test_back_page`

**Descricao:** Validar retorno do checkout para o carrinho.

**Passos:**
1. Acessar o checkout.
2. Clicar em Cancel.

**Resultado esperado:** Usuario retorna para `cart.html`.

### CT-22: Validar titulo da pagina de compra finalizada

**Arquivo:** `tests/test_complete.py::test_title_complete`

**Descricao:** Validar a tela exibida apos finalizar a compra.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Clicar em Finish.
6. Validar o titulo da pagina.

**Resultado esperado:** A pagina exibe `Checkout: Complete!`.

### CT-23: Voltar para home apos compra finalizada

**Arquivo:** `tests/test_complete.py::test_back_home`

**Descricao:** Validar o botao Back Home na tela de compra concluida.

**Passos:**
1. Finalizar uma compra.
2. Clicar em Back Home.

**Resultado esperado:** Usuario retorna para `inventory.html`.

### CT-24: Validar total da compra com Sauce Labs Backpack

**Arquivo:** `tests/test_finish.py::test_soma_one_products[Sauce Labs Backpack]`

**Descricao:** Validar o calculo do total no checkout overview para Sauce Labs Backpack.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Backpack ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

### CT-25: Validar total da compra com Sauce Labs Bike Light

**Arquivo:** `tests/test_finish.py::test_soma_one_products[Sauce Labs Bike Light]`

**Descricao:** Validar o calculo do total no checkout overview para Sauce Labs Bike Light.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Bike Light ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

### CT-26: Validar total da compra com Sauce Labs Bolt T-Shirt

**Arquivo:** `tests/test_finish.py::test_soma_one_products[Sauce Labs Bolt T-Shirt]`

**Descricao:** Validar o calculo do total no checkout overview para Sauce Labs Bolt T-Shirt.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Bolt T-Shirt ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

### CT-27: Validar total da compra com Sauce Labs Fleece Jacket

**Arquivo:** `tests/test_finish.py::test_soma_one_products[Sauce Labs Fleece Jacket]`

**Descricao:** Validar o calculo do total no checkout overview para Sauce Labs Fleece Jacket.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Fleece Jacket ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

### CT-28: Validar total da compra com Sauce Labs Onesie

**Arquivo:** `tests/test_finish.py::test_soma_one_products[Sauce Labs Onesie]`

**Descricao:** Validar o calculo do total no checkout overview para Sauce Labs Onesie.

**Passos:**
1. Fazer login.
2. Adicionar Sauce Labs Onesie ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

### CT-29: Validar total da compra com Test.allTheThings() T-Shirt (Red)

**Arquivo:** `tests/test_finish.py::test_soma_one_products[Test.allTheThings() T-Shirt (Red)]`

**Descricao:** Validar o calculo do total no checkout overview para Test.allTheThings() T-Shirt (Red).

**Passos:**
1. Fazer login.
2. Adicionar Test.allTheThings() T-Shirt (Red) ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

### CT-30: Validar total da compra com todos os produtos

**Arquivo:** `tests/test_finish.py::test_finish_all`

**Descricao:** Validar o calculo do total no checkout overview com todos os produtos.

**Passos:**
1. Fazer login.
2. Adicionar todos os produtos ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

### CT-31: Login valido

**Arquivo:** `tests/test_login.py::test_login_valid`

**Descricao:** Validar login com credenciais corretas.

**Passos:**
1. Acessar a pagina de login.
2. Inserir usuario `standard_user`.
3. Inserir senha `secret_sauce`.
4. Clicar em Login.

**Resultado esperado:** Usuario e direcionado para `inventory.html`.

### CT-32: Login invalido com usuario errado

**Arquivo:** `tests/test_login.py::test_login_error[errado-secret_sauce-Epic sadface: Username and password do not match any user in this service]`

**Descricao:** Validar mensagem de erro ao informar usuario invalido.

**Passos:**
1. Acessar a pagina de login.
2. Inserir usuario invalido.
3. Inserir senha valida.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Username and password do not match any user in this service`.

### CT-33: Login invalido com senha errada

**Arquivo:** `tests/test_login.py::test_login_error[standard_user-errado-Epic sadface: Username and password do not match any user in this service]`

**Descricao:** Validar mensagem de erro ao informar senha invalida.

**Passos:**
1. Acessar a pagina de login.
2. Inserir usuario valido.
3. Inserir senha invalida.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Username and password do not match any user in this service`.

### CT-34: Login com usuario e senha vazios

**Arquivo:** `tests/test_login.py::test_login_error[--Epic sadface: Username is required]`

**Descricao:** Validar obrigatoriedade do campo usuario.

**Passos:**
1. Acessar a pagina de login.
2. Deixar usuario vazio.
3. Deixar senha vazia.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Username is required`.

### CT-35: Login com senha vazia

**Arquivo:** `tests/test_login.py::test_login_error[standard_user--Epic sadface: Password is required]`

**Descricao:** Validar obrigatoriedade do campo senha.

**Passos:**
1. Acessar a pagina de login.
2. Inserir usuario valido.
3. Deixar senha vazia.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Password is required`.

### CT-36: Login com usuario vazio

**Arquivo:** `tests/test_login.py::test_login_error[-secret_sauce-Epic sadface: Username is required]`

**Descricao:** Validar obrigatoriedade do campo usuario quando a senha foi preenchida.

**Passos:**
1. Acessar a pagina de login.
2. Deixar usuario vazio.
3. Inserir senha valida.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Username is required`.

### CT-37: Adicionar Sauce Labs Backpack ao carrinho pela pagina de produtos

**Arquivo:** `tests/test_products.py::test_add_one_product[Sauce Labs Backpack]`

**Descricao:** Validar a adicao de Sauce Labs Backpack ao carrinho.

**Passos:**
1. Fazer login.
2. Clicar no nome Sauce Labs Backpack.
3. Clicar em Add to Cart na pagina de detalhe.
4. Voltar para a pagina de produtos.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-38: Adicionar Sauce Labs Bike Light ao carrinho pela pagina de produtos

**Arquivo:** `tests/test_products.py::test_add_one_product[Sauce Labs Bike Light]`

**Descricao:** Validar a adicao de Sauce Labs Bike Light ao carrinho.

**Passos:**
1. Fazer login.
2. Clicar no nome Sauce Labs Bike Light.
3. Clicar em Add to Cart na pagina de detalhe.
4. Voltar para a pagina de produtos.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-39: Adicionar Sauce Labs Bolt T-Shirt ao carrinho pela pagina de produtos

**Arquivo:** `tests/test_products.py::test_add_one_product[Sauce Labs Bolt T-Shirt]`

**Descricao:** Validar a adicao de Sauce Labs Bolt T-Shirt ao carrinho.

**Passos:**
1. Fazer login.
2. Clicar no nome Sauce Labs Bolt T-Shirt.
3. Clicar em Add to Cart na pagina de detalhe.
4. Voltar para a pagina de produtos.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-40: Adicionar Sauce Labs Fleece Jacket ao carrinho pela pagina de produtos

**Arquivo:** `tests/test_products.py::test_add_one_product[Sauce Labs Fleece Jacket]`

**Descricao:** Validar a adicao de Sauce Labs Fleece Jacket ao carrinho.

**Passos:**
1. Fazer login.
2. Clicar no nome Sauce Labs Fleece Jacket.
3. Clicar em Add to Cart na pagina de detalhe.
4. Voltar para a pagina de produtos.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-41: Adicionar Sauce Labs Onesie ao carrinho pela pagina de produtos

**Arquivo:** `tests/test_products.py::test_add_one_product[Sauce Labs Onesie]`

**Descricao:** Validar a adicao de Sauce Labs Onesie ao carrinho.

**Passos:**
1. Fazer login.
2. Clicar no nome Sauce Labs Onesie.
3. Clicar em Add to Cart na pagina de detalhe.
4. Voltar para a pagina de produtos.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-42: Adicionar Test.allTheThings() T-Shirt (Red) ao carrinho pela pagina de produtos

**Arquivo:** `tests/test_products.py::test_add_one_product[Test.allTheThings() T-Shirt (Red)]`

**Descricao:** Validar a adicao de Test.allTheThings() T-Shirt (Red) ao carrinho.

**Passos:**
1. Fazer login.
2. Clicar no nome Test.allTheThings() T-Shirt (Red).
3. Clicar em Add to Cart na pagina de detalhe.
4. Voltar para a pagina de produtos.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-43: Adicionar todos os produtos ao carrinho pela pagina de produtos

**Arquivo:** `tests/test_products.py::test_add_list`

**Descricao:** Validar a adicao de todos os produtos disponiveis.

**Passos:**
1. Fazer login.
2. Clicar no nome de cada produto.
3. Clicar em Add to Cart na pagina de detalhe.
4. Voltar para a listagem.
5. Repetir o fluxo para todos os produtos.
6. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `6`.

## Observacoes

- O README documenta o projeto atual em Selenium, Python e Pytest.
- Os 43 casos acima seguem a mesma ordem exibida por `python -m pytest --collect-only -q`.
- Atualmente nao ha testes automatizados para filtros de produtos, usuario
  bloqueado, SQL injection, emojis, texto longo ou caracteres especiais no
  checkout.
