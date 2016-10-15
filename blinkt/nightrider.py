import time

from blinkt import set_clear_on_exit, set_pixel, show, set_brightness


set_clear_on_exit()
set_brightness(0.1)

while True:
    for i in range(8):
        if i == 0 or i == 1:
            set_pixel(i, 255, 0, 0)
        else:
            set_pixel(i, 255, 0, 0)
            set_pixel(i-2, 0, 0, 0)
        show()
        time.sleep(0.1)
        if i == 7:
            set_pixel(i-1, 0, 0, 0)
            show()
            time.sleep(0.1)
            set_pixel(i, 0, 0, 0)
            show()

    time.sleep(0.25)

    for i in range (7, -1, -1):
        if i == 7 or i == 6:
            set_pixel(i, 255, 0, 0)
        else:
            set_pixel(i, 255, 0, 0)
            set_pixel(i+2, 0, 0, 0)
        show()
        time.sleep(0.1)
        if i == 0:
            set_pixel(i+1, 0, 0, 0)
            show()
            time.sleep(0.1)
            set_pixel(i, 0, 0, 0)
            show()

    time.sleep(0.1)

            
            

        
