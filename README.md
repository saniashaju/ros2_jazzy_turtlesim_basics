# ROS 2 Jazzy: Turtlesim Teleoperation Basics

## 🎯 Aim
To understand the core concepts of ROS 2 (Nodes, Topics, and Messages) by implementing keyboard-based teleoperation in a simulated environment.

## 🛠️ Technical Stack
* **OS:** Ubuntu 24.04 (Noble Numbat)
* **ROS Version:** ROS 2 Jazzy Jalisco
* **Simulation:** Turtlesim

## ✅ Key Learning Milestones
* **Node Communication:** Successfully initialized the `/turtlesim` node and `/teleop_turtle` node.
* **Topic Subscription:** Observed how the turtle node subscribes to `cmd_vel` to execute movement.
* **Environment Setup:** Configured workspace sourcing and `bashrc` shortcuts for Jazzy development.

## 📺 Simulation Demo
<p align="center">
  <video src="Turtlesim.mp4" width="100%" controls>
  </video>
</p>

## ⚙️ How to Run
```bash
# Terminal 1: Launch the Simulator
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtlesim_node

# Terminal 2: Launch Keyboard Control
source /opt/ros/jazzy/setup.bash
ros2 run turtlesim turtle_teleop_key

📈 Progression
This project served as the foundational step before moving into real-world hardware integration with the Unitree Go2 robot.


---

### **Step 3: Upload the Video**
1.  Take that screen recording from your photo (the one showing the blue Turtlesim window).
2.  In GitHub, click **Add file** -> **Upload files**.
3.  Upload your video and **rename it to `turtlesim_demo.mp4`** (or change the name in the README code above to match your file).
4.  **Commit changes** with the message: `feat: add turtlesim simulation demo and documentation`.

---

### **Step 4: Connect the Two Projects**
On your **Unitree Go2** GitHub (the one we just finished), you can add a small line at the bottom of that README:
> "Started my ROS 2 journey with [Turtlesim Basics](LINK_TO_YOUR_TURTLESIM_REPO)."

### **Why this is professional:**
It shows you didn't just copy-paste code for the robot; it proves you actually studied the **ROS 2 fundamentals** first. It makes your Unitree Go2 project much more believable and impressive.

**Would you like me to help you create a LinkedIn "Project Showcase" that mentions both your simulation and your real robot work?**


