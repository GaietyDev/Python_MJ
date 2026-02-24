import os
import datetime

log_name_list = []
log_number_list = []
largest_int = 0

folder_log = "Log"
parent_dir = os.getcwd()
path_log = os.path.join(parent_dir, folder_log)
log_exists = os.path.exists(path_log)

if log_exists:
    print("Log directory exists")
    os.chdir(path_log)
    log_list = os.listdir()
    print(log_list)

    for file in log_list:
        index = file.find(".log")
        is_file = False
        
        if index > -1:
            print(file)
            is_file = os.path.isfile(file)
        print(is_file)

        if is_file:
            log_name = file[0:index]
            log_name_list.insert(0, log_name)
        print(log_name_list)
    #End of Loop
            
    for log_name in log_name_list:
        is_number = log_name.isnumeric()

        if is_number:
            log_number = int(log_name)
            log_number_list.insert(0, log_number)
    #End of Loop

    for num in log_number_list:
        if num > largest_int:
            largest_int = num
    #End of Loop

    log_file_name = str(largest_int + 1) + ".log"
    current_datetime = str(datetime.datetime.now())
    
    log_file = open(log_file_name, "w")
    log_file.write(current_datetime)
    log_file.close()
    
            
else:
    os.mkdir(path_log)
    
