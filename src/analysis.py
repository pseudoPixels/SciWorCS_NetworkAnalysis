import numpy
import pandas as pd
import matplotlib.pyplot as plt



dataset_single_user = pd.read_csv('../Datasets/singleUserB3.2')
dataset_remote_user = pd.read_csv('../Datasets/remoteUserB3.2')


plt.figure(1)


plt.subplot(221)
plt.plot(dataset_single_user['Interval start'], dataset_single_user['Client_Server'], marker='1', label='Single User -CS')
plt.plot(dataset_remote_user['Interval start'], dataset_remote_user['Client_Server'], marker='+', label='Collab. -CS')
plt.plot(dataset_remote_user['Interval start'], dataset_remote_user['Client_Client'], marker='.', label='Collab. -CC')
#plt.yscale('log')
plt.grid(True)
plt.title('W 4095 - Network Overhead', fontsize=14)
plt.xlabel('Time(s)', fontsize=14)
plt.ylabel('Packets/10 sec', fontsize=14)
plt.legend(loc="upper right", fontsize=13)


plt.show()

# print(dataset_single_user)
# print(dataset_remote_user)