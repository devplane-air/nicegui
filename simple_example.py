from nicegui import ui

ui.label('Hello NiceGUI!')

audio = ui.audio('https://www.soundjay.com/misc/sounds/beep-07a.wav').style('display: none')

ui.button('BUTTON 1', on_click=lambda: ui.notify('Button 1 was pressed'))
ui.button('BUTTON 2 (SOUND)', on_click=lambda: [ui.notify('Button 2 was pressed - playing sound!'), audio.play()])
ui.button('BUTTON 3', on_click=lambda: ui.notify('Button 3 was pressed'))

ui.run()
