; Auto-generated. Do not edit!


(cl:in-package mars_robot_msgs-msg)


;//! \htmlinclude sensor_msg.msg.html

(cl:defclass <sensor_msg> (roslisp-msg-protocol:ros-message)
  ((auger_depth
    :reader auger_depth
    :initarg :auger_depth
    :type cl:fixnum
    :initform 0)
   (auger_accel_z
    :reader auger_accel_z
    :initarg :auger_accel_z
    :type cl:float
    :initform 0.0)
   (auger_accel_x
    :reader auger_accel_x
    :initarg :auger_accel_x
    :type cl:float
    :initform 0.0))
)

(cl:defclass sensor_msg (<sensor_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sensor_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sensor_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mars_robot_msgs-msg:<sensor_msg> is deprecated: use mars_robot_msgs-msg:sensor_msg instead.")))

(cl:ensure-generic-function 'auger_depth-val :lambda-list '(m))
(cl:defmethod auger_depth-val ((m <sensor_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mars_robot_msgs-msg:auger_depth-val is deprecated.  Use mars_robot_msgs-msg:auger_depth instead.")
  (auger_depth m))

(cl:ensure-generic-function 'auger_accel_z-val :lambda-list '(m))
(cl:defmethod auger_accel_z-val ((m <sensor_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mars_robot_msgs-msg:auger_accel_z-val is deprecated.  Use mars_robot_msgs-msg:auger_accel_z instead.")
  (auger_accel_z m))

(cl:ensure-generic-function 'auger_accel_x-val :lambda-list '(m))
(cl:defmethod auger_accel_x-val ((m <sensor_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mars_robot_msgs-msg:auger_accel_x-val is deprecated.  Use mars_robot_msgs-msg:auger_accel_x instead.")
  (auger_accel_x m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sensor_msg>) ostream)
  "Serializes a message object of type '<sensor_msg>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'auger_depth)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'auger_depth)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'auger_accel_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'auger_accel_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sensor_msg>) istream)
  "Deserializes a message object of type '<sensor_msg>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'auger_depth)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'auger_depth)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'auger_accel_z) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'auger_accel_x) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sensor_msg>)))
  "Returns string type for a message object of type '<sensor_msg>"
  "mars_robot_msgs/sensor_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sensor_msg)))
  "Returns string type for a message object of type 'sensor_msg"
  "mars_robot_msgs/sensor_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sensor_msg>)))
  "Returns md5sum for a message object of type '<sensor_msg>"
  "ce384a3455ea54b3bf3d0b088d180fe5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sensor_msg)))
  "Returns md5sum for a message object of type 'sensor_msg"
  "ce384a3455ea54b3bf3d0b088d180fe5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sensor_msg>)))
  "Returns full string definition for message of type '<sensor_msg>"
  (cl:format cl:nil "uint16 auger_depth~%float32 auger_accel_z~%float32 auger_accel_x~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sensor_msg)))
  "Returns full string definition for message of type 'sensor_msg"
  (cl:format cl:nil "uint16 auger_depth~%float32 auger_accel_z~%float32 auger_accel_x~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sensor_msg>))
  (cl:+ 0
     2
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sensor_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'sensor_msg
    (cl:cons ':auger_depth (auger_depth msg))
    (cl:cons ':auger_accel_z (auger_accel_z msg))
    (cl:cons ':auger_accel_x (auger_accel_x msg))
))
