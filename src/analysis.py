import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



dataset_single_userB32 = pd.read_csv('../Datasets/singleUserB3.2')
dataset_remote_userB32 = pd.read_csv('../Datasets/remoteUserB3.2')



dataset_single_userB31 = pd.read_csv('../Datasets/singleUserB3.1')
dataset_remote_userB31 = pd.read_csv('../Datasets/remoteUserB3.1')




dataset_single_userML = pd.read_csv('../Datasets/singleML')
dataset_remote_userML = pd.read_csv('../Datasets/remoteML')




plt.figure(1)


plt.subplot(221)
plt.plot(dataset_single_userB32['Interval start'], dataset_single_userB32['Client_Server'], marker='1', label='Single User -CS')
plt.plot(dataset_remote_userB32['Interval start'], dataset_remote_userB32['Client_Server'], marker='+', label='Collab. -CS')
plt.plot(dataset_remote_userB32['Interval start'], dataset_remote_userB32['Client_Client'], marker='.', label='Collab. -CC')
#plt.yscale('log')
plt.grid(True)
plt.title('W. 4095 - message passing stats.', fontsize=14)
plt.xlabel('Time(s)', fontsize=14)
plt.ylabel('Packets/10 sec', fontsize=14)
plt.legend(loc="upper right", fontsize=13)






plt.subplot(222)
plt.plot(dataset_single_userB31['Interval start'], dataset_single_userB31['Client_Server'], marker='1', label='Single User -CS')
plt.plot(dataset_remote_userB31['Interval start'], dataset_remote_userB31['Client_Server'], marker='+', label='Collab. -CS')
plt.plot(dataset_remote_userB31['Interval start'], dataset_remote_userB31['Client_Client'], marker='.', label='Collab. -CC')
#plt.yscale('log')
plt.grid(True)
plt.title('W. 4094 - Network Overhead stats.', fontsize=14)
plt.xlabel('Time(s)', fontsize=14)
plt.ylabel('Packets/10 sec', fontsize=14)
plt.legend(loc="upper right", fontsize=13)






plt.subplot(223)
plt.plot(dataset_single_userML['Interval start'], dataset_single_userML['Client_Server'], marker='1', label='Single User -CS')
plt.plot(dataset_remote_userML['Interval start'], dataset_remote_userML['Client_Server'], marker='+', label='Collab. -CS')
plt.plot(dataset_remote_userML['Interval start'], dataset_remote_userML['Client_Client'], marker='.', label='Collab. -CC')
#plt.yscale('log')
plt.grid(True)
plt.title('W. ML - message passing stats.', fontsize=14)
plt.xlabel('Time(s)', fontsize=14)
plt.ylabel('Packets/10 sec', fontsize=14)
plt.legend(loc="upper right", fontsize=13)







avg_single_client_server= (dataset_single_userML['Client_Server'] + dataset_single_userB31['Client_Server'] + dataset_single_userB32['Client_Server'] ) / 3
avg_remote_client_server = (dataset_remote_userML['Client_Server'] + dataset_remote_userB31['Client_Server'] + dataset_remote_userB32['Client_Server'] ) / 3
avg_remote_client_client = (dataset_remote_userML['Client_Client'] + dataset_remote_userB31['Client_Client'] + dataset_remote_userB32['Client_Client'] ) / 3



avg_single_client_server = avg_single_client_server.dropna()
avg_remote_client_server = avg_remote_client_server.dropna()
avg_remote_client_client = avg_remote_client_client.dropna()


print(avg_remote_client_server)
print(np.arange(0, len(avg_remote_client_server)*10, 10))




plt.subplot(224)
plt.plot(np.arange(0, len(avg_single_client_server)*10, 10), avg_single_client_server, marker='1', label='Single User -CS')
plt.plot(np.arange(0, len(avg_remote_client_server)*10, 10), avg_remote_client_server, marker='+', label='Collab. -CS')
plt.plot(np.arange(0, len(avg_remote_client_client)*10, 10), avg_remote_client_client, marker='.', label='Collab. -CC')
#plt.yscale('log')
plt.grid(True)
plt.title('Avg. - message passing stats.', fontsize=14)
plt.xlabel('Time(s)', fontsize=14)
plt.ylabel('Packets/10 sec', fontsize=14)
plt.legend(loc="upper right", fontsize=13)













plt.show()

# print(dataset_single_user)
# print(dataset_remote_user)