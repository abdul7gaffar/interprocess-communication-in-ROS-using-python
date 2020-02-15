name=ABDUL GAFFAR ABDUL KHADEER             student id=190687836
download the folder AR_week4_test in the catkin workspace
create a catkin environment by calling a $catkin_make
make all the files executibel inside the scripts folder to do so-
--- navigate to $roscd AR_week4_test/scripts
---$chmod +x points_generator.py
---$chmod +x cubic_traj_planner.py
---$chmod +x compute_cubic_coeffs.py
---$chmod +x plot_cubic_traj.py
after this call the launch file from catkin worksspace like $ roslaunch AR_week4_test cubic_traj_gen.launch
				-------NOTE------
wait for appx 35-50 seconds for the rdt_graph and rqt_plot to generate the trajectpries on the plot

