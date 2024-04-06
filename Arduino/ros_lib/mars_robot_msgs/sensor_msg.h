#ifndef _ROS_mars_robot_msgs_sensor_msg_h
#define _ROS_mars_robot_msgs_sensor_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace mars_robot_msgs
{

  class sensor_msg : public ros::Msg
  {
    public:
      typedef uint16_t _auger_depth_type;
      _auger_depth_type auger_depth;
      typedef float _auger_accel_z_type;
      _auger_accel_z_type auger_accel_z;
      typedef float _auger_accel_x_type;
      _auger_accel_x_type auger_accel_x;

    sensor_msg():
      auger_depth(0),
      auger_accel_z(0),
      auger_accel_x(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->auger_depth >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->auger_depth >> (8 * 1)) & 0xFF;
      offset += sizeof(this->auger_depth);
      union {
        float real;
        uint32_t base;
      } u_auger_accel_z;
      u_auger_accel_z.real = this->auger_accel_z;
      *(outbuffer + offset + 0) = (u_auger_accel_z.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_auger_accel_z.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_auger_accel_z.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_auger_accel_z.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->auger_accel_z);
      union {
        float real;
        uint32_t base;
      } u_auger_accel_x;
      u_auger_accel_x.real = this->auger_accel_x;
      *(outbuffer + offset + 0) = (u_auger_accel_x.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_auger_accel_x.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_auger_accel_x.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_auger_accel_x.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->auger_accel_x);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->auger_depth =  ((uint16_t) (*(inbuffer + offset)));
      this->auger_depth |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->auger_depth);
      union {
        float real;
        uint32_t base;
      } u_auger_accel_z;
      u_auger_accel_z.base = 0;
      u_auger_accel_z.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_auger_accel_z.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_auger_accel_z.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_auger_accel_z.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->auger_accel_z = u_auger_accel_z.real;
      offset += sizeof(this->auger_accel_z);
      union {
        float real;
        uint32_t base;
      } u_auger_accel_x;
      u_auger_accel_x.base = 0;
      u_auger_accel_x.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_auger_accel_x.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_auger_accel_x.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_auger_accel_x.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->auger_accel_x = u_auger_accel_x.real;
      offset += sizeof(this->auger_accel_x);
     return offset;
    }

    const char * getType(){ return "mars_robot_msgs/sensor_msg"; };
    const char * getMD5(){ return "ce384a3455ea54b3bf3d0b088d180fe5"; };

  };

}
#endif
