// Auto-generated. Do not edit!

// (in-package mars_robot_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class sensor_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.auger_depth = null;
      this.auger_accel_z = null;
      this.auger_accel_x = null;
    }
    else {
      if (initObj.hasOwnProperty('auger_depth')) {
        this.auger_depth = initObj.auger_depth
      }
      else {
        this.auger_depth = 0;
      }
      if (initObj.hasOwnProperty('auger_accel_z')) {
        this.auger_accel_z = initObj.auger_accel_z
      }
      else {
        this.auger_accel_z = 0.0;
      }
      if (initObj.hasOwnProperty('auger_accel_x')) {
        this.auger_accel_x = initObj.auger_accel_x
      }
      else {
        this.auger_accel_x = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type sensor_msg
    // Serialize message field [auger_depth]
    bufferOffset = _serializer.uint16(obj.auger_depth, buffer, bufferOffset);
    // Serialize message field [auger_accel_z]
    bufferOffset = _serializer.float32(obj.auger_accel_z, buffer, bufferOffset);
    // Serialize message field [auger_accel_x]
    bufferOffset = _serializer.float32(obj.auger_accel_x, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type sensor_msg
    let len;
    let data = new sensor_msg(null);
    // Deserialize message field [auger_depth]
    data.auger_depth = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [auger_accel_z]
    data.auger_accel_z = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [auger_accel_x]
    data.auger_accel_x = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 10;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mars_robot_msgs/sensor_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ce384a3455ea54b3bf3d0b088d180fe5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint16 auger_depth
    float32 auger_accel_z
    float32 auger_accel_x
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new sensor_msg(null);
    if (msg.auger_depth !== undefined) {
      resolved.auger_depth = msg.auger_depth;
    }
    else {
      resolved.auger_depth = 0
    }

    if (msg.auger_accel_z !== undefined) {
      resolved.auger_accel_z = msg.auger_accel_z;
    }
    else {
      resolved.auger_accel_z = 0.0
    }

    if (msg.auger_accel_x !== undefined) {
      resolved.auger_accel_x = msg.auger_accel_x;
    }
    else {
      resolved.auger_accel_x = 0.0
    }

    return resolved;
    }
};

module.exports = sensor_msg;
