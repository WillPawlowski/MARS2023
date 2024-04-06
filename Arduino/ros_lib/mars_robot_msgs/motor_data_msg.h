#ifndef _ROS_mars_robot_msgs_motor_data_msg_h
#define _ROS_mars_robot_msgs_motor_data_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace mars_robot_msgs
{

  class motor_data_msg : public ros::Msg
  {
    public:
      typedef float _auger_current_type;
      _auger_current_type auger_current;
      typedef float _auger_speed_type;
      _auger_speed_type auger_speed;
      typedef float _right_loco_current_type;
      _right_loco_current_type right_loco_current;
      typedef float _left_loco_current_type;
      _left_loco_current_type left_loco_current;

    motor_data_msg():
      auger_current(0),
      auger_speed(0),
      right_loco_current(0),
      left_loco_current(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_auger_current;
      u_auger_current.real = this->auger_current;
      *(outbuffer + offset + 0) = (u_auger_current.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_auger_current.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_auger_current.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_auger_current.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->auger_current);
      union {
        float real;
        uint32_t base;
      } u_auger_speed;
      u_auger_speed.real = this->auger_speed;
      *(outbuffer + offset + 0) = (u_auger_speed.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_auger_speed.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_auger_speed.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_auger_speed.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->auger_speed);
      union {
        float real;
        uint32_t base;
      } u_right_loco_current;
      u_right_loco_current.real = this->right_loco_current;
      *(outbuffer + offset + 0) = (u_right_loco_current.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_right_loco_current.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_right_loco_current.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_right_loco_current.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->right_loco_current);
      union {
        float real;
        uint32_t base;
      } u_left_loco_current;
      u_left_loco_current.real = this->left_loco_current;
      *(outbuffer + offset + 0) = (u_left_loco_current.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_left_loco_current.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_left_loco_current.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_left_loco_current.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->left_loco_current);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_auger_current;
      u_auger_current.base = 0;
      u_auger_current.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_auger_current.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_auger_current.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_auger_current.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->auger_current = u_auger_current.real;
      offset += sizeof(this->auger_current);
      union {
        float real;
        uint32_t base;
      } u_auger_speed;
      u_auger_speed.base = 0;
      u_auger_speed.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_auger_speed.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_auger_speed.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_auger_speed.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->auger_speed = u_auger_speed.real;
      offset += sizeof(this->auger_speed);
      union {
        float real;
        uint32_t base;
      } u_right_loco_current;
      u_right_loco_current.base = 0;
      u_right_loco_current.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_right_loco_current.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_right_loco_current.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_right_loco_current.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->right_loco_current = u_right_loco_current.real;
      offset += sizeof(this->right_loco_current);
      union {
        float real;
        uint32_t base;
      } u_left_loco_current;
      u_left_loco_current.base = 0;
      u_left_loco_current.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_left_loco_current.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_left_loco_current.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_left_loco_current.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->left_loco_current = u_left_loco_current.real;
      offset += sizeof(this->left_loco_current);
     return offset;
    }

    const char * getType(){ return "mars_robot_msgs/motor_data_msg"; };
    const char * getMD5(){ return "1a39659befe0182ae29a42de47aa67fc"; };

  };

}
#endif
