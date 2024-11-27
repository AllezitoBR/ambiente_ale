from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.jogajuntoinstituto.org/#Contato")


@when(u'Insiro meus dados')
def step_impl(context):
    context.driver.find_element(By.ID , "nome").send_keys("Alexandre")
    context.driver.find_element(By.ID , "email").send_keys("ale@teste.com")
    select = context.driver.find_element(By.ID, "assunto") 
    for _ in range(7): 
        select.send_keys(Keys.ARROW_DOWN)
    select.send_keys(Keys.TAB)

@when(u'"Envio a mensagem "Teste - Oi!"')
def step_impl(context):
    context.driver.find_element(By.ID, "mensagem").send_keys("Teste - Oi!")

@when('Clico no botão enviar"{button_id}"') 
def step_impl(context, button_id): 
    wait = WebDriverWait(context.driver, 10) 
    enviar_button = wait.until(EC.element_to_be_clickable((By.ID, button_id)))
