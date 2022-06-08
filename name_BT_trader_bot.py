

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import time
    import iz_func
    import iz_telegram    
    import datetime



    if message_in == 'Русский':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'/start','S',0)

    if message_in == 'English':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'/start','S',0)

        
    if message_in == 'Отмена':
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ""

    if message_in == 'Вывод':
        iz_telegram.save_variable (user_id,namebot,"status",'Ввод BNB')

  
