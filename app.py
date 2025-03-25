from flask import Flask, jsonify
import time
import keyboard
import mouse
from screeninfo import get_monitors
from pynput.mouse import Controller

app = Flask(__name__)

@app.route('/run_script', methods=['GET'])
def run_script():
    def setup():
        global monitor
        monitors = get_monitors()
        mouse_controller = Controller()
        mouse_x, mouse_y = mouse_controller.position

        def is_mouse_on_monitor(monitor, mouse_x, mouse_y):
            return (monitor.x <= mouse_x < monitor.x + monitor.width) and (monitor.y <= mouse_y < monitor.y + monitor.height)
        
        screenWidth = 0
        screenHeight = 0

        for monitor in monitors:
            if is_mouse_on_monitor(monitor, mouse_x, mouse_y):
                screenWidth = monitor.width
                screenHeight = monitor.height
                print(f"Mouse is currently on monitor: {monitor.name}")
                print(f"Monitor Resolution - Width: {screenWidth} px, Height: {screenHeight} px")
                break

    def moveMouse(x, y):
        mouse.move(monitor.x + ((x*monitor.width) // 100), monitor.y + ((y*monitor.height) // 100), absolute=True, duration=0.001)

    def dragMouse(x, y):
        mouse.drag(0, 0, monitor.x + ((x*monitor.width) // 100), monitor.y + ((y*monitor.height) // 100), absolute=False, duration=0)

    setup()

    keyboard.wait('f')
    moveMouse(15, 7)
    mouse.click('left')
    keyboard.press_and_release('g, m, a, i, l, ., c, o, m')
    keyboard.press_and_release('enter')
    time.sleep(4)
    moveMouse(5, 30)
    mouse.click('left')
    time.sleep(5)
    moveMouse(70, 42)
    mouse.click('left')
    keyboard.press_and_release('w,i,l,s,o,n')
    keyboard.press_and_release('enter')
    moveMouse(70, 45)
    mouse.click('left')

    keyboard.press_and_release('shift+i, space, a, m, space, d, u, m, b')
    moveMouse(70, 60)
    mouse.click('left')
    keyboard.press_and_release('y, o, u, space, r, space, a, w, e, s, o, m, e')

    moveMouse(62, 93)
    mouse.click('left')

    time.sleep(2)

    keyboard.press('ctrl')
    keyboard.press('shift')
    keyboard.press_and_release('q')
    keyboard.press_and_release('q')
    keyboard.release('ctrl')
    keyboard.release('shift')

    return jsonify({"status": "success", "message": "Script executed successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
