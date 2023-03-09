import datetime
import time
from plyer import notification

notification.notify(
    title = "İngilizce Kelime ezberleme günü {}".format(datetime.date.today()),
    message = "İngilizce '2 gün' kutusundan ezber yapman gerek!!", 
    app_icon = "book.ico",  
    timeout  = 10
    )
  
time.sleep(60 * 60 * 24 * 2)