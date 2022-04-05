
'''
Target Manager Application
'''

from guizero import App, Text
import view.TimerTick as tt
import client.KeepAlive as ka
import server.TargetSimulator as ts
from threading import Thread

# Utility methods
def update_time_ticks(app):
    time1_label = Text(app, text="Timer Ticks: ", grid=[0,1])
    time1 = Text(app, text="1", grid=[1,1])
    tm = tt.TimerTick(time1)
    time1.repeat(100, lambda: tm.ticker()) # run timer every 100ms

# MAIN
if __name__ == "__main__":

    # main view
    app = App(title="TargetManager", width=600, height=500, layout="grid")
    app.icon = "view/wow.gif" 

    main_view_label = Text(app, text="MAIN VIEW", grid=[10,0])

    update_time_ticks(app)

    ping = ka.KeepAlive("localhost", 5005, "Hello Worldlings!" )
    t0 = Thread(target=lambda: ping.hello()()) # run keep alive thread
    t0.start()
 
    # init and start thread for target simulator
    sim = ts.TargetSimulator("localhost", 5005)
    t1 = Thread(target=lambda: sim.receiver())
    t1.start()
    
    # display any receive counts from the target
    sim_rx_cnt_label = Text(app, text="Target Receive: ", grid=[0, 2])
    sim_rx_cnt = Text(app, text="0", grid=[1,2])
    sim_rx_cnt.value = "33"
    sim_rx_cnt.value.rjust(40)

    app.display() # display loop
    