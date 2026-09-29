from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()

options.add_argument('--headless=new') 
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)

# Espera implícita global de 10 segundos #importamte
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/dropdown")

print(f"Sucesso! Título: {driver.title}")

driver.save_screenshot("tela-login.png")

print("Primeiro exercicio ok")

aba_0 = driver.current_window_handle

quantidade_abas = len(driver.window_handles)

driver.execute_script(
    "window.open('https://the-internet.herokuapp.com/dynamic_loading/2', '_blank');"
)

if len(driver.window_handles) > quantidade_abas:
    print("Segunda aba aberta com sucesso!")
else:
    print("Erro: segunda aba não foi aberta.")

abas = driver.window_handles

driver.switch_to.window(abas[1])

print(f"Segunda aba: {driver.title}")

quantidade_abas = len(driver.window_handles)

driver.execute_script(
    "window.open('https://pt.wikipedia.org', '_blank');"
)

if len(driver.window_handles) > quantidade_abas:
    print("Terceira aba aberta com sucesso!")
else:
    print("Erro: terceira aba não foi aberta.")

abas = driver.window_handles

print(f"Quantidade de abas: {len(abas)}")

print("Segundo exercicio ok")


driver.switch_to.window(abas[0])

print("Voltei para a Aba 0")

dropdown = driver.find_element("id", "dropdown")

select = Select(dropdown)
select.select_by_visible_text("Option 1")

opcao_selecionada = select.first_selected_option
print(
    f"Opção selecionada: "
    f"{opcao_selecionada.get_attribute('value')}"
)

print("Terceiro exercicio ok")

driver.switch_to.window(abas[1])

print("Voltei para a Aba 1")

botao_start = driver.find_element("css selector", "#start button")

botao_start.click()

espera = WebDriverWait(driver, 15)

finish = espera.until(
    EC.visibility_of_element_located(("id", "finish"))
)

print(f"Mensagem: {finish.text}")

print("Quarto exercicio ok")

driver.switch_to.window(abas[2])

print("Voltei para a Aba 2 - Wikipédia")

barra_pesquisa = driver.find_element("id", "searchInput")

barra_pesquisa.send_keys("Automação")

print("Palavra Automação digitada com sucesso!")

link_artigo = driver.find_element(
    "css selector",
    "#p-navigation a"
)

texto_link = link_artigo.text

destino_link = link_artigo.get_attribute("href")

print(f"Texto do link: {texto_link}")
print(f"Destino do link: {destino_link}")

driver.save_screenshot("evidencia_wiki.png")

print("Evidência salva como evidencia_wiki.png")

print("Quinto exercicio ok")

driver.quit()
print("Navegador encerrado com sucesso!")
print("Sexto exercicio ok")