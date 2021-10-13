# import pyprog
# from time import sleep
#
# # Create Object
# prog = pyprog.ProgressBar(" ", "", 34)
# # Update Progress Bar
# prog.update()
#
# for i in range(34):
#     # Do something
#     sleep(0.1)
#     # Set current status
#     prog.set_stat(i + 1)
#     # Update Progress Bar again
#     prog.update()
#
# # Make the Progress Bar final
# prog.end()



# import time
# from tqdm import tqdm
# for i in tqdm(range(10)):
#     time.sleep(0.1)


import time
import enlighten

manager = enlighten.Manager()
odds = manager.counter(total=50)
evens = manager.counter(total=50)

for num in range(1, 101):
    time.sleep(0.05)
    if num % 2:
        odds.update()
    else:
        evens.update()