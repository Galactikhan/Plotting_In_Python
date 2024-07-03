# Import pyplot as plt from matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
########################################

##############################################
################################### File Input
File_Name = ''
##############
File = File_Name + '.dat'
Data_File = np.loadtxt(File, dtype=float)


# Load Time
Time = Data_File[:,0]

# Load State Vector Position for 
# 3D plot
State_Vec_X = Data_File[:,6]
State_Vec_Y = Data_File[:,7]
State_Vec_Z = Data_File[:,8]



# Set 5 Figures for Orbital Elements
f1 = plt.figure()
f2 = plt.figure()
f3 = plt.figure()
f4 = plt.figure()
f5 = plt.figure()

# 1st Orbital Element
ax1 = f1.add_subplot(111)
ax1.plot(Time, Data_File[:,1])

# 2nd Orbital Element
ax2 = f2.add_subplot(111)
ax2.plot(Time, Data_File[:,2])

# 3rd Orbital Element
ax3 = f3.add_subplot(111)
ax3.plot(Time, Data_File[:,3])

# 4th Orbital Element
ax2 = f2.add_subplot(111)
ax2.plot(Time, Data_File[:,4])

# 5th Orbital Element
ax2 = f2.add_subplot(111)
ax2.plot(Time, Data_File[:,5])

# Show each plot
plt.show()



###############################################
###################################### 3D Orbit 
# Set plot                              
fig = plt.figure('Orbit')               
# Set axis                              
axis = plt.axes(projection='3d')           
#########################################
# Plot State Vector in 3D
axis.plot3D(State_Vec_X,
            State_Vec_Y, 
            State_Vec_Z,        
            )              
# Axis Labels                           
axis.set_xlabel('x (km)')                 
axis.set_ylabel('y (km)')                  
axis.set_zlabel('z (km)')                   
#########################################
plt.tight_layout()
plt.show()