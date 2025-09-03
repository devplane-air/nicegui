from nicegui import ui

ui.label('Hello NiceGUI!')

audio = ui.audio('https://cdn.pixabay.com/download/audio/2022/02/22/audio_d1718ab41b.mp3', 
                 controls=True, autoplay=False, muted=False).style('width: 300px; margin: 10px 0;')

def play_sound():
    ui.notify('Button 2 was pressed - attempting to play sound!')
    try:
        audio.play()
        ui.notify('Audio play() method called successfully', type='positive')
    except Exception as e:
        ui.notify(f'Audio play failed: {str(e)}', type='negative')

ui.button('BUTTON 1', on_click=lambda: ui.notify('Button 1 was pressed'))
ui.button('BUTTON 2 (SOUND)', on_click=play_sound)
ui.button('BUTTON 3', on_click=lambda: ui.notify('Button 3 was pressed'))

ui.run()
