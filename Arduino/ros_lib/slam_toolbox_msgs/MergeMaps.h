#ifndef _ROS_SERVICE_MergeMaps_h
#define _ROS_SERVICE_MergeMaps_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace slam_toolbox_msgs
{

static const char MERGEMAPS[] = "slam_toolbox_msgs/MergeMaps";

  class MergeMapsRequest : public ros::Msg
  {
    public:

    MergeMapsRequest()
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

    const char * getType(){ return MERGEMAPS; };
    const char * getMD5(){ return "d41d8cd98f00b204e9800998ecf8427e"; };

  };

  class MergeMapsResponse : public ros::Msg
  {
    public:

    MergeMapsResponse()
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

    const char * getType(){ return MERGEMAPS; };
    const char * getMD5(){ return "d41d8cd98f00b204e9800998ecf8427e"; };

  };

  class MergeMaps {
    public:
    typedef MergeMapsRequest Request;
    typedef MergeMapsResponse Response;
  };

}
#endif
