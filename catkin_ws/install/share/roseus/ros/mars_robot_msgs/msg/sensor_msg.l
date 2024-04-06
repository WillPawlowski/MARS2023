;; Auto-generated. Do not edit!


(when (boundp 'mars_robot_msgs::sensor_msg)
  (if (not (find-package "MARS_ROBOT_MSGS"))
    (make-package "MARS_ROBOT_MSGS"))
  (shadow 'sensor_msg (find-package "MARS_ROBOT_MSGS")))
(unless (find-package "MARS_ROBOT_MSGS::SENSOR_MSG")
  (make-package "MARS_ROBOT_MSGS::SENSOR_MSG"))

(in-package "ROS")
;;//! \htmlinclude sensor_msg.msg.html


(defclass mars_robot_msgs::sensor_msg
  :super ros::object
  :slots (_auger_depth _auger_accel_z _auger_accel_x ))

(defmethod mars_robot_msgs::sensor_msg
  (:init
   (&key
    ((:auger_depth __auger_depth) 0)
    ((:auger_accel_z __auger_accel_z) 0.0)
    ((:auger_accel_x __auger_accel_x) 0.0)
    )
   (send-super :init)
   (setq _auger_depth (round __auger_depth))
   (setq _auger_accel_z (float __auger_accel_z))
   (setq _auger_accel_x (float __auger_accel_x))
   self)
  (:auger_depth
   (&optional __auger_depth)
   (if __auger_depth (setq _auger_depth __auger_depth)) _auger_depth)
  (:auger_accel_z
   (&optional __auger_accel_z)
   (if __auger_accel_z (setq _auger_accel_z __auger_accel_z)) _auger_accel_z)
  (:auger_accel_x
   (&optional __auger_accel_x)
   (if __auger_accel_x (setq _auger_accel_x __auger_accel_x)) _auger_accel_x)
  (:serialization-length
   ()
   (+
    ;; uint16 _auger_depth
    2
    ;; float32 _auger_accel_z
    4
    ;; float32 _auger_accel_x
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _auger_depth
       (write-word _auger_depth s)
     ;; float32 _auger_accel_z
       (sys::poke _auger_accel_z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _auger_accel_x
       (sys::poke _auger_accel_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _auger_depth
     (setq _auger_depth (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _auger_accel_z
     (setq _auger_accel_z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _auger_accel_x
     (setq _auger_accel_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get mars_robot_msgs::sensor_msg :md5sum-) "ce384a3455ea54b3bf3d0b088d180fe5")
(setf (get mars_robot_msgs::sensor_msg :datatype-) "mars_robot_msgs/sensor_msg")
(setf (get mars_robot_msgs::sensor_msg :definition-)
      "uint16 auger_depth
float32 auger_accel_z
float32 auger_accel_x

")



(provide :mars_robot_msgs/sensor_msg "ce384a3455ea54b3bf3d0b088d180fe5")


