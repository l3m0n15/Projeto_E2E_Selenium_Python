# Projeto QA Swag Labs com Playwright

## Casos de Teste

### CT-01: Login válido
**Descrição:** Validar login com credenciais corretas.

**Passos:**
1. Acessar a página de login.
2. Inserir usuário válido.
3. Inserir senha válida.
4. Clicar em Login.

**Resultado esperado:**  
Usuário entra no sistema e é direcionado para a página de inventário.

### CT-02: Login inválido com senha errada
**Descrição:** Validar que o sistema bloqueia login quando a senha está incorreta.

**Passos:**
1. Acessar a página de login.
2. Inserir usuário válido.
3. Inserir senha incorreta.
4. Clicar em Login.
5. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Epic sadface: Username and password do not match any user in this service`.

### CT-03: Login inválido com usuário errado
**Descrição:** Validar que o sistema bloqueia login quando o usuário está incorreto.

**Passos:**
1. Acessar a página de login.
2. Inserir usuário incorreto.
3. Inserir senha válida.
4. Clicar em Login.
5. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Epic sadface: Username and password do not match any user in this service`.

### CT-04: Login inválido com usuário e senha errados
**Descrição:** Validar que o sistema bloqueia login quando usuário e senha estão incorretos.

**Passos:**
1. Acessar a página de login.
2. Inserir usuário incorreto.
3. Inserir senha incorreta.
4. Clicar em Login.
5. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Epic sadface: Username and password do not match any user in this service`.

### CT-05: Login inválido com usuário e senha vazios
**Descrição:** Validar que o sistema exige o preenchimento do usuário antes de autenticar.

**Passos:**
1. Acessar a página de login.
2. Deixar usuário vazio.
3. Deixar senha vazia.
4. Clicar em Login.
5. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Epic sadface: Username is required`.

### CT-06: Login inválido com senha vazia
**Descrição:** Validar que o sistema exige senha quando o usuário foi informado.

**Passos:**
1. Acessar a página de login.
2. Inserir usuário válido.
3. Deixar senha vazia.
4. Clicar em Login.
5. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Epic sadface: Password is required`.

### CT-07: Login inválido com usuário vazio
**Descrição:** Validar que o sistema exige usuário quando a senha foi informada.

**Passos:**
1. Acessar a página de login.
2. Deixar usuário vazio.
3. Inserir senha válida.
4. Clicar em Login.
5. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Epic sadface: Username is required`.

### CT-08: Login inválido com usuário bloqueado
**Descrição:** Validar que o sistema bloqueia acesso para usuário bloqueado.

**Passos:**
1. Acessar a página de login.
2. Inserir usuário bloqueado.
3. Inserir senha válida.
4. Clicar em Login.
5. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Epic sadface: Sorry, this user has been locked out.`.

### CT-09: Adicionar produtos pelos nomes
**Descrição:** Validar se o usuário consegue adicionar produtos pela tela de detalhe do produto.

**Passos:**
1. Fazer login.
2. Clicar no nome do produto.
3. Adicionar produto ao carrinho.
4. Voltar para a loja.
5. Repetir o fluxo para todos os produtos.
6. Verificar o badge do carrinho.

**Resultado esperado:**  
Usuário adiciona 6 produtos ao carrinho.

### CT-10: Adicionar produtos pela listagem principal
**Descrição:** Validar a adição de produtos pelo botão Add to Cart da listagem principal.

**Passos:**
1. Fazer login.
2. Adicionar todos os produtos pela listagem.
3. Verificar o badge do carrinho.

**Resultado esperado:**  
Usuário adiciona 6 produtos ao carrinho através do atalho da listagem.

### CT-11: Remover itens pelo inventário
**Descrição:** Validar se o usuário consegue remover produtos adicionados ao carrinho pela página de inventário.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Remover os produtos pelo inventário.
4. Verificar o badge do carrinho.

**Resultado esperado:**  
Todos os produtos são removidos e o badge do carrinho não fica visível.

### CT-12: Filtrar produtos por ordem A-Z
**Descrição:** Validar ordenação de produtos por nome em ordem crescente.

**Passos:**
1. Fazer login.
2. Localizar o seletor de filtros.
3. Selecionar a opção "Name (A to Z)".
4. Capturar os nomes dos produtos exibidos.
5. Verificar a ordem dos produtos.

**Resultado esperado:**  
Produtos são exibidos em ordem alfabética de A-Z.

### CT-13: Filtrar produtos por ordem Z-A
**Descrição:** Validar ordenação de produtos por nome em ordem decrescente.

**Passos:**
1. Fazer login.
2. Localizar o seletor de filtros.
3. Selecionar a opção "Name (Z to A)".
4. Capturar os nomes dos produtos exibidos.
5. Verificar a ordem dos produtos.

**Resultado esperado:**  
Produtos são exibidos em ordem alfabética de Z-A.

### CT-14: Filtrar produtos do menor preço para o maior
**Descrição:** Validar ordenação de produtos por preço crescente.

**Passos:**
1. Fazer login.
2. Localizar o seletor de filtros.
3. Selecionar a opção "Price (low to high)".
4. Capturar os preços dos produtos exibidos.
5. Verificar a ordem dos preços.

**Resultado esperado:**  
Produtos são exibidos do menor preço para o maior.

### CT-15: Filtrar produtos do maior preço para o menor
**Descrição:** Validar ordenação de produtos por preço decrescente.

**Passos:**
1. Fazer login.
2. Localizar o seletor de filtros.
3. Selecionar a opção "Price (high to low)".
4. Capturar os preços dos produtos exibidos.
5. Verificar a ordem dos preços.

**Resultado esperado:**  
Produtos são exibidos do maior preço para o menor.

### CT-16: Verificar produtos no carrinho
**Descrição:** Validar se os produtos adicionados no inventário aparecem corretamente no carrinho.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar o carrinho.
4. Capturar os produtos exibidos no carrinho.
5. Comparar com os produtos adicionados.

**Resultado esperado:**  
O carrinho exibe os mesmos produtos adicionados no inventário.

### CT-17: Remover produtos do carrinho
**Descrição:** Validar a remoção de todos os produtos diretamente pela página do carrinho.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar o carrinho.
4. Remover todos os produtos.
5. Verificar o badge do carrinho.

**Resultado esperado:**  
Todos os produtos são removidos e o badge do carrinho não fica visível.

### CT-18: Acessar checkout pelo carrinho
**Descrição:** Validar se o botão Checkout direciona o usuário para o formulário de checkout.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar o carrinho.
4. Clicar no botão Checkout.

**Resultado esperado:**  
Usuário é direcionado para a página `checkout-step-one.html`.

### CT-19: Voltar do carrinho para a loja
**Descrição:** Validar se o botão Continue Shopping retorna para a página de inventário.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar o carrinho.
4. Clicar no botão Continue Shopping.

**Resultado esperado:**  
Usuário retorna para a página de inventário.

### CT-20: Preencher formulário de checkout
**Descrição:** Validar preenchimento do formulário de checkout com dados aceitos.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar o carrinho.
4. Clicar em Checkout.
5. Preencher First Name, Last Name e Zip/Postal Code.
6. Clicar em Continue.

**Resultado esperado:**  
Usuário avança para a página `checkout-step-two.html`.

### CT-21: Cancelar checkout
**Descrição:** Validar se o botão Cancel interrompe o checkout e retorna para o carrinho.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar o carrinho.
4. Clicar em Checkout.
5. Clicar em Cancel.

**Resultado esperado:**  
Usuário retorna para a página do carrinho.

### CT-22: Checkout com todos os campos vazios
**Descrição:** Validar erro ao tentar continuar checkout sem preencher nenhum campo.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Deixar First Name, Last Name e Zip/Postal Code vazios.
5. Clicar em Continue.
6. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Error: First Name is required`.

### CT-23: Checkout com First Name preenchido
**Descrição:** Validar erro quando apenas First Name é preenchido.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher somente First Name.
5. Clicar em Continue.
6. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Error: Last Name is required`.

### CT-24: Checkout com First Name e Last Name preenchidos
**Descrição:** Validar erro quando o campo Zip/Postal Code fica vazio.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher First Name e Last Name.
5. Deixar Zip/Postal Code vazio.
6. Clicar em Continue.
7. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Error: Postal Code is required`.

### CT-25: Checkout somente com Last Name preenchido
**Descrição:** Validar erro quando apenas Last Name é preenchido.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher somente Last Name.
5. Clicar em Continue.
6. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Error: First Name is required`.

### CT-26: Checkout somente com Zip/Postal Code preenchido
**Descrição:** Validar erro quando apenas Zip/Postal Code é preenchido.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher somente Zip/Postal Code.
5. Clicar em Continue.
6. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Error: First Name is required`.

### CT-27: Checkout com First Name e Zip/Postal Code preenchidos
**Descrição:** Validar erro quando Last Name fica vazio.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher First Name e Zip/Postal Code.
5. Deixar Last Name vazio.
6. Clicar em Continue.
7. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Error: Last Name is required`.

### CT-28: Checkout com Last Name e Zip/Postal Code preenchidos
**Descrição:** Validar erro quando First Name fica vazio.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher Last Name e Zip/Postal Code.
5. Deixar First Name vazio.
6. Clicar em Continue.
7. Verificar a mensagem de erro.

**Resultado esperado:**  
Sistema exibe a mensagem `Error: First Name is required`.

### CT-29: Checkout com campos numéricos
**Descrição:** Validar comportamento do checkout quando os campos recebem números junto com texto.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher os campos com números junto com texto.
5. Clicar em Continue.

**Resultado esperado:**  
Sistema permite continuar para a página `checkout-step-two.html`.

### CT-30: Checkout com caracteres especiais
**Descrição:** Validar comportamento do checkout quando os campos recebem caracteres especiais.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher os campos com caracteres especiais.
5. Clicar em Continue.

**Resultado esperado:**  
Sistema permite continuar para a página `checkout-step-two.html`.

### CT-31: Checkout com texto muito grande
**Descrição:** Validar comportamento do checkout quando First Name e Last Name recebem textos longos.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher First Name e Last Name com texto muito grande.
5. Preencher Zip/Postal Code.
6. Clicar em Continue.

**Resultado esperado:**  
Sistema permite continuar para a página `checkout-step-two.html`.

### CT-32: Checkout com SQL injection
**Descrição:** Validar se entrada com SQL injection é tratada como texto comum no formulário.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher os campos com uma entrada de SQL injection.
5. Clicar em Continue.

**Resultado esperado:**  
Sistema permite continuar para a página `checkout-step-two.html`.

### CT-33: Checkout com script HTML
**Descrição:** Validar se entrada com script HTML é tratada como texto comum no formulário.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher os campos com tags HTML/script.
5. Clicar em Continue.

**Resultado esperado:**  
Sistema permite continuar para a página `checkout-step-two.html`.

### CT-34: Checkout com emojis
**Descrição:** Validar comportamento do checkout quando os campos recebem emojis.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher os campos com emojis.
5. Clicar em Continue.

**Resultado esperado:**  
Sistema permite continuar para a página `checkout-step-two.html`.

### CT-35: Checkout com quebra de linha
**Descrição:** Validar comportamento do checkout quando os campos recebem quebra de linha.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher os campos com quebra de linha.
5. Clicar em Continue.

**Resultado esperado:**  
Sistema permite continuar para a página `checkout-step-two.html`.

### CT-36: Checkout com CEP com letras e números
**Descrição:** Documentar possível bug onde o sistema aceita CEP com letras e números.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher First Name e Last Name.
5. Preencher Zip/Postal Code com letras e números.
6. Clicar em Continue.

**Resultado esperado:**  
Sistema deveria exibir mensagem de erro, mas atualmente permite continuar.

### CT-37: Checkout com CEP inválido
**Descrição:** Documentar possível bug onde o sistema aceita CEP inválido.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher First Name e Last Name.
5. Preencher Zip/Postal Code com CEP inválido.
6. Clicar em Continue.

**Resultado esperado:**  
Sistema deveria exibir mensagem de erro, mas atualmente permite continuar.

### CT-38: Checkout com todos os campos preenchidos apenas com espaços
**Descrição:** Documentar possível bug onde o sistema aceita campos preenchidos somente com espaços.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher First Name, Last Name e Zip/Postal Code apenas com espaços.
5. Clicar em Continue.

**Resultado esperado:**  
Sistema deveria exibir mensagem de erro, mas atualmente permite continuar.

### CT-39: Validar cálculo do resumo da compra
**Descrição:** Validar se o total do overview corresponde à soma do subtotal com a taxa.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher o formulário.
5. Capturar subtotal, taxa e total.
6. Somar subtotal + taxa.

**Resultado esperado:**  
O valor calculado deve ser igual ao total exibido na tela.

### CT-40: Finalizar compra
**Descrição:** Validar se o botão Finish conclui a compra.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher o formulário.
5. Clicar em Finish no overview.

**Resultado esperado:**  
Usuário é direcionado para a página `checkout-complete.html`.

### CT-41: Cancelar compra no overview
**Descrição:** Validar se o botão Cancel no overview retorna para a página de inventário.

**Passos:**
1. Fazer login.
2. Adicionar produtos ao carrinho.
3. Acessar checkout.
4. Preencher o formulário.
5. Clicar em Cancel no overview.

**Resultado esperado:**  
Usuário retorna para a página de inventário.

**Total documentado:** 41 casos de teste, equivalentes aos 41 testes automatizados listados pelo Playwright.
