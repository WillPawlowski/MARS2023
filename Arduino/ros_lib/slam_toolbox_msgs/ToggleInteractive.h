#ifndef _ROS_SERVICE_ToggleInteractive_h
#define _ROS_SERVICE_ToggleInteractive_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace slam_toolbox_msgs
{

static const char TOGGLEINTERACTIVE[] = "slam_toolbox_msgs/ToggleInteractive";

  class ToggleInteractiveRequest : public ros::Msg
  {
    public:

    ToggleInteractiveRequest()
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

    const char * getType(){ return TOGGLEINTERACTIVE; };
    const char * getMD5(){ return "d41d8cd98f00b204e9800998ecf8427e"; };

  };

  class ToggleInteractiveResponse : public ros::Msg
  {
    public:

    ToggleInteractiveResponse()
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

    const char * getType(){ return TOGGLEINTERACTIVE; };
    const char * getMD5(){ return "d41d8cd98f00b204e9800998ecf8427e"; };

  };

  class ToggleInteractive {
    public:
    typedef ToggleInteractiveRequest Request;
    typedef ToggleInteractiveResponse Response;
  };

}
#endif
