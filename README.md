# Projeto QA Swag Labs com Selenium e Python

Automacao de testes end-to-end para o site Swag Labs, usando Selenium WebDriver,
Pytest e o padrao Page Object Model.

## Casos de teste

O projeto possui 43 testes coletados pelo Pytest, considerando os cenarios
parametrizados.

### CT-01: Login valido

**Descricao:** Validar login com credenciais corretas.

**Passos:**
1. Acessar a pagina de login.
2. Inserir usuario `standard_user`.
3. Inserir senha `secret_sauce`.
4. Clicar em Login.

**Resultado esperado:** Usuario e direcionado para `inventory.html`.

### CT-02: Login invalido com usuario errado

**Descricao:** Validar mensagem de erro ao informar usuario invalido.

**Passos:**
1. Acessar a pagina de login.
2. Inserir usuario invalido.
3. Inserir senha valida.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Username and password do not match any user in this service`.

### CT-03: Login invalido com senha errada

**Descricao:** Validar mensagem de erro ao informar senha invalida.

**Passos:**
1. Acessar a pagina de login.
2. Inserir usuario valido.
3. Inserir senha invalida.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Username and password do not match any user in this service`.

### CT-04: Login com usuario e senha vazios

**Descricao:** Validar obrigatoriedade do campo usuario.

**Passos:**
1. Acessar a pagina de login.
2. Deixar usuario vazio.
3. Deixar senha vazia.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Username is required`.

### CT-05: Login com senha vazia

**Descricao:** Validar obrigatoriedade do campo senha.

**Passos:**
1. Acessar a pagina de login.
2. Inserir usuario valido.
3. Deixar senha vazia.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Password is required`.

### CT-06: Login com usuario vazio

**Descricao:** Validar obrigatoriedade do campo usuario quando a senha foi preenchida.

**Passos:**
1. Acessar a pagina de login.
2. Deixar usuario vazio.
3. Inserir senha valida.
4. Clicar em Login.

**Resultado esperado:** Sistema exibe `Epic sadface: Username is required`.

### CT-07: Adicionar um produto ao carrinho pela pagina de produtos

**Descricao:** Validar a adicao individual de cada produto ao carrinho.

**Passos:**
1. Fazer login.
2. Adicionar um produto ao carrinho.
3. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

**Cenarios parametrizados:**
- Sauce Labs Backpack
- Sauce Labs Bike Light
- Sauce Labs Bolt T-Shirt
- Sauce Labs Fleece Jacket
- Sauce Labs Onesie
- Test.allTheThings() T-Shirt (Red)

### CT-08: Adicionar todos os produtos ao carrinho

**Descricao:** Validar a adicao de todos os produtos disponiveis.

**Passos:**
1. Fazer login.
2. Adicionar todos os produtos ao carrinho.
3. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `6`.

### CT-09: Validar um produto no carrinho

**Descricao:** Confirmar que cada produto adicionado aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar um produto ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** O produto adicionado e exibido no carrinho.

**Cenarios parametrizados:** mesmos produtos do CT-07.

### CT-10: Validar todos os produtos no carrinho

**Descricao:** Confirmar que todos os produtos adicionados aparecem no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar todos os produtos ao carrinho.
3. Acessar o carrinho.
4. Validar os produtos exibidos.

**Resultado esperado:** Todos os produtos adicionados aparecem no carrinho.

### CT-11: Remover um produto do carrinho

**Descricao:** Validar remocao individual de produtos no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar um produto ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

**Cenarios parametrizados:** mesmos produtos do CT-07.

### CT-12: Remover todos os produtos do carrinho

**Descricao:** Validar remocao de todos os produtos no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar todos os produtos ao carrinho.
3. Acessar o carrinho.
4. Remover todos os produtos.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-13: Voltar do carrinho para a loja

**Descricao:** Validar o botao de retorno para a pagina de produtos.

**Passos:**
1. Fazer login.
2. Acessar o carrinho.
3. Clicar no botao de voltar/continuar comprando.

**Resultado esperado:** Usuario retorna para `inventory.html`.

### CT-14: Acessar checkout pelo carrinho

**Descricao:** Validar que o fluxo do carrinho permite acessar o checkout.

**Passos:**
1. Fazer login.
2. Acessar o carrinho.
3. Clicar no botao de checkout.

**Resultado esperado:** Usuario e direcionado para `checkout-step-one.html`.

### CT-15: Checkout com informacoes validas

**Descricao:** Validar preenchimento correto das informacoes do checkout.

**Passos:**
1. Fazer login.
2. Acessar o carrinho.
3. Acessar o checkout.
4. Preencher First Name, Last Name e Postal Code.
5. Continuar.

**Resultado esperado:** Usuario e direcionado para `checkout-step-two.html`.

### CT-16: Checkout sem First Name

**Descricao:** Validar obrigatoriedade do campo First Name.

**Passos:**
1. Acessar o checkout.
2. Deixar First Name vazio.
3. Preencher Last Name e Postal Code.
4. Continuar.

**Resultado esperado:** Sistema exibe `Error: First Name is required`.

### CT-17: Checkout sem Last Name

**Descricao:** Validar obrigatoriedade do campo Last Name.

**Passos:**
1. Acessar o checkout.
2. Preencher First Name.
3. Deixar Last Name vazio.
4. Preencher Postal Code.
5. Continuar.

**Resultado esperado:** Sistema exibe `Error: Last Name is required`.

### CT-18: Checkout sem Postal Code

**Descricao:** Validar obrigatoriedade do campo Postal Code.

**Passos:**
1. Acessar o checkout.
2. Preencher First Name e Last Name.
3. Deixar Postal Code vazio.
4. Continuar.

**Resultado esperado:** Sistema exibe `Error: Postal Code is required`.

### CT-19: Cancelar checkout

**Descricao:** Validar retorno do checkout para o carrinho.

**Passos:**
1. Acessar o checkout.
2. Clicar no botao de voltar/cancelar.

**Resultado esperado:** Usuario retorna para `cart.html`.

### CT-20: Validar total da compra com um produto

**Descricao:** Validar o calculo do total no checkout overview para cada produto individual.

**Passos:**
1. Fazer login.
2. Adicionar um produto ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

**Cenarios parametrizados:** mesmos produtos do CT-07.

### CT-21: Validar total da compra com todos os produtos

**Descricao:** Validar o calculo do total no checkout overview com todos os produtos.

**Passos:**
1. Fazer login.
2. Adicionar todos os produtos ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Capturar subtotal, taxa e total.
6. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa e igual ao total exibido.

### CT-22: Validar titulo da pagina de compra finalizada

**Descricao:** Validar a tela exibida apos finalizar a compra.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher dados validos.
5. Finalizar compra.
6. Validar o titulo da pagina.

**Resultado esperado:** A pagina exibe `Checkout: Complete!`.

### CT-23: Voltar para home apos compra finalizada

**Descricao:** Validar o botao Back Home na tela de compra concluida.

**Passos:**
1. Finalizar uma compra.
2. Clicar em Back Home.

**Resultado esperado:** Usuario retorna para `inventory.html`.

### CT-24: Adicionar Sauce Labs Backpack ao carrinho (variação)

**Descricao:** Validar a adicao do produto "Sauce Labs Backpack" ao carrinho (variação individual).

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Backpack" ao carrinho.
3. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-25: Adicionar Sauce Labs Bike Light ao carrinho (variação)

**Descricao:** Validar a adicao do produto "Sauce Labs Bike Light" ao carrinho (variação individual).

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Bike Light" ao carrinho.
3. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-26: Adicionar Sauce Labs Bolt T-Shirt ao carrinho (variação)

**Descricao:** Validar a adicao do produto "Sauce Labs Bolt T-Shirt" ao carrinho (variação individual).

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Bolt T-Shirt" ao carrinho.
3. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-27: Adicionar Sauce Labs Fleece Jacket ao carrinho (variação)

**Descricao:** Validar a adicao do produto "Sauce Labs Fleece Jacket" ao carrinho (variação individual).

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Fleece Jacket" ao carrinho.
3. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-28: Adicionar Sauce Labs Onesie ao carrinho (variação)

**Descricao:** Validar a adicao do produto "Sauce Labs Onesie" ao carrinho (variação individual).

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Onesie" ao carrinho.
3. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho exibe `1`.

### CT-29: Validar produto no carrinho - Sauce Labs Backpack

**Descricao:** Confirmar que "Sauce Labs Backpack" aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Backpack" ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** "Sauce Labs Backpack" é exibido no carrinho.

### CT-30: Validar produto no carrinho - Sauce Labs Bike Light

**Descricao:** Confirmar que "Sauce Labs Bike Light" aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Bike Light" ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** "Sauce Labs Bike Light" é exibido no carrinho.

### CT-31: Validar produto no carrinho - Sauce Labs Bolt T-Shirt

**Descricao:** Confirmar que "Sauce Labs Bolt T-Shirt" aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Bolt T-Shirt" ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** "Sauce Labs Bolt T-Shirt" é exibido no carrinho.

### CT-32: Validar produto no carrinho - Sauce Labs Fleece Jacket

**Descricao:** Confirmar que "Sauce Labs Fleece Jacket" aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Fleece Jacket" ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** "Sauce Labs Fleece Jacket" é exibido no carrinho.

### CT-33: Validar produto no carrinho - Sauce Labs Onesie

**Descricao:** Confirmar que "Sauce Labs Onesie" aparece corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Onesie" ao carrinho.
3. Acessar o carrinho.
4. Validar o produto exibido.

**Resultado esperado:** "Sauce Labs Onesie" é exibido no carrinho.

### CT-34: Remover Sauce Labs Backpack do carrinho

**Descricao:** Validar remoção do produto "Sauce Labs Backpack" do carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Backpack" ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-35: Remover Sauce Labs Bike Light do carrinho

**Descricao:** Validar remoção do produto "Sauce Labs Bike Light" do carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Bike Light" ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-36: Remover Sauce Labs Bolt T-Shirt do carrinho

**Descricao:** Validar remoção do produto "Sauce Labs Bolt T-Shirt" do carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Bolt T-Shirt" ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-37: Remover Sauce Labs Fleece Jacket do carrinho

**Descricao:** Validar remoção do produto "Sauce Labs Fleece Jacket" do carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Fleece Jacket" ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-38: Remover Sauce Labs Onesie do carrinho

**Descricao:** Validar remoção do produto "Sauce Labs Onesie" do carrinho.

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Onesie" ao carrinho.
3. Acessar o carrinho.
4. Remover o produto.
5. Verificar o contador do carrinho.

**Resultado esperado:** O contador do carrinho fica vazio ou `0`.

### CT-39: Validar total - Sauce Labs Backpack (checkout overview)

**Descricao:** Validar o calculo do total no checkout overview para o produto "Sauce Labs Backpack".

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Backpack" ao carrinho.
3. Acessar checkout e preencher dados válidos.
4. Capturar subtotal, taxa e total.
5. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa é igual ao total exibido.

### CT-40: Validar total - Sauce Labs Bike Light (checkout overview)

**Descricao:** Validar o calculo do total no checkout overview para o produto "Sauce Labs Bike Light".

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Bike Light" ao carrinho.
3. Acessar checkout e preencher dados válidos.
4. Capturar subtotal, taxa e total.
5. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa é igual ao total exibido.

### CT-41: Validar total - Sauce Labs Bolt T-Shirt (checkout overview)

**Descricao:** Validar o calculo do total no checkout overview para o produto "Sauce Labs Bolt T-Shirt".

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Bolt T-Shirt" ao carrinho.
3. Acessar checkout e preencher dados válidos.
4. Capturar subtotal, taxa e total.
5. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa é igual ao total exibido.

### CT-42: Validar total - Sauce Labs Fleece Jacket (checkout overview)

**Descricao:** Validar o calculo do total no checkout overview para o produto "Sauce Labs Fleece Jacket".

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Fleece Jacket" ao carrinho.
3. Acessar checkout e preencher dados válidos.
4. Capturar subtotal, taxa e total.
5. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa é igual ao total exibido.

### CT-43: Validar total - Sauce Labs Onesie (checkout overview)

**Descricao:** Validar o calculo do total no checkout overview para o produto "Sauce Labs Onesie".

**Passos:**
1. Fazer login.
2. Adicionar "Sauce Labs Onesie" ao carrinho.
3. Acessar checkout e preencher dados válidos.
4. Capturar subtotal, taxa e total.
5. Comparar subtotal + taxa com o total.

**Resultado esperado:** A soma de subtotal + taxa é igual ao total exibido.

## Estrutura do projeto

```text
.
├── conftest.py
├── pages/
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── complete_page.py
│   ├── finish_page.py
│   ├── login_page.py
│   └── products_page.py
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_complete.py
│   ├── test_finish.py
│   ├── test_login.py
│   └── test_products.py
└── requirements.txt
```
