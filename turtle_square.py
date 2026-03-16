import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.move_turtle)
        self.get_logger().info('Turtle Square Node has started!')

    def move_turtle(self):
        msg = Twist()
        # Move Forward
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        time.sleep(1)
        
        # Turn 90 degrees
        msg.linear.x = 0.0
        msg.angular.z = 1.57 # Roughly 90 degrees in radians
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSquare()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
