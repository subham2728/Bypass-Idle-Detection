import sys
import move_mouse_pt
if sys.platform == 'win32':
    from ctypes import Structure, windll, c_uint, c_int, sizeof, byref
    
    class LASTINPUTINFO(Structure):
        _fields_ = [
            ('cbSize', c_uint),
            ('dwTime', c_int),
        ]
        
    def get_idle_duration():
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
            millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
            return millis / 1000.0
        else:
            return 0
else:
    def get_idle_duration():
        return 0
        
if __name__ == '__main__':
    import time
    count_script_call=0
    while True:
        duration = str(get_idle_duration())
        duration_f=float(duration)
        if(duration_f>=40):
            count_script_call+=1
            print("")
            print("Time for other script")
            move_mouse_pt.random_auto(count_script_call)
        print('User idle for seconds = ' + duration)
        time.sleep(20)
