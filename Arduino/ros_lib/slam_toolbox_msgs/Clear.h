#ifndef _ROS_SERVICE_Clear_h
#define _ROS_SERVICE_Clear_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace slam_toolbox_msgs
{

static const char CLEAR[] = "slam_toolbox_msgs/Clear";

  class ClearRequest : public ros::Msg
  {
    public:

    ClearRequest()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
     return offset;
    }

    const char * getType(){ return CLEAR; };
    const char * getMD5(){ return "d41d8cd98f00b204e9800998ecf8427e"; };

  };

  class ClearResponse : public ros::Msg
  {
    public:

    ClearResponse()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
     return offset;
    }

    const char * getType(){ return CLEAR; };
    const char * getMD5(){ return "d41d8cd98f00b204e9800998ecf8427e"; };

  };

  class Clear {
    public:
    typedef ClearRequest Request;
    typedef ClearResponse Response;
  };

}
#endif
