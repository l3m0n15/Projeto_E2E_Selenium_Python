from pages.complete_page import title_complete, go_to_home

#Teste para validar o titulo da pagina complete
def test_title_complete(usuario_complete):
    assert title_complete(usuario_complete) == "Checkout: Complete!"

#Teste para validar botao back home
def test_back_home(usuario_complete):
    go_to_home(usuario_complete)
    assert "inventory.html" in usuario_complete.current_url
