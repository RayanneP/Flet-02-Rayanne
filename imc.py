import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.theme_mode = ft.ThemeMode.LIGHT  # 🔄 modo claro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 30

    # Campos de entrada
    peso = ft.TextField(
        label="Peso (kg)", 
        width=300, 
        keyboard_type=ft.KeyboardType.NUMBER
    )
    altura = ft.TextField(
        label="Altura (m)", 
        width=300, 
        keyboard_type=ft.KeyboardType.NUMBER
    )

    # Texto de resultado
    resultado = ft.Text(
        "Digite seus dados para calcular o IMC",
        size=18,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREY_500
    )

    # Função para calcular o IMC
    def calcular_imc(e):
        try:
            p = float(peso.value.replace(",", "."))
            a = float(altura.value.replace(",", "."))

            if p <= 0 or a <= 0:
                raise ValueError

            imc = p / (a * a)

            # Classificação (OMS)
            if imc < 18.5:
                classificacao = "Abaixo do peso"
                cor = ft.Colors.ORANGE
            elif imc < 25:
                classificacao = "Peso normal"
                cor = ft.Colors.GREEN
            elif imc < 30:
                classificacao = "Sobrepeso"
                cor = ft.Colors.AMBER
            elif imc < 35:
                classificacao = "Obesidade grau I"
                cor = ft.Colors.RED
            elif imc < 40:
                classificacao = "Obesidade grau II"
                cor = ft.Colors.RED_ACCENT
            else:
                classificacao = "Obesidade grau III"
                cor = ft.Colors.RED_900

            resultado.value = f"💡 Seu IMC é {imc:.2f}\n➡️ {classificacao}"
            resultado.color = cor

        except ValueError:
            resultado.value = "❌ Digite valores numéricos válidos!"
            resultado.color = ft.Colors.RED

        page.update()

    # Função para limpar os campos
    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = "Digite seus dados para calcular o IMC"
        resultado.color = ft.Colors.GREY_500
        page.update()

    # Alternar tema (ícone da lua/sol)
    def toggle_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            tema_btn.icon = ft.Icons.DARK_MODE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            tema_btn.icon = ft.Icons.LIGHT_MODE
        page.update()
    # ----------------- TOPO -----------------
    tema_btn = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        tooltip="Alternar tema",
        on_click=toggle_tema,
    )
    # Título centralizado
    titulo = ft.Text(
        "Calculadora de IMC",
        size=22,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

# Linha apenas para o botão de tema, alinhado à direita
    tema_area = ft.Row(
        [tema_btn],
        alignment=ft.MainAxisAlignment.END,
    )
    subtitulo = ft.Text("Informe seus dados", size=16)
    # ----------------- BOTÕES -----------------
    botoes = ft.Row(
    [
            ft.ElevatedButton(
                "Calcular IMC",
                bgcolor=ft.Colors.DEEP_PURPLE,
                color=ft.Colors.WHITE,
                width=150,
                on_click=calcular_imc,
            ),
            ft.ElevatedButton(
                "Limpar",
                bgcolor=ft.Colors.RED,
                color=ft.Colors.WHITE,
                width=150,
                on_click=limpar,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )

    # Layout
    page.add(
        tema_area,
        titulo,
        subtitulo,
        peso,
        altura,
        botoes,
        ft.Divider(),
        resultado,
    )

                
ft.app(target=main)