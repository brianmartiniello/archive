#!/bin/bash
VNC_CMD="/usr/bin/vncserver-virtual"
VNC_OPTS="-localhost -geometry 1280x740"
${VNC_CMD} :1 ${VNC_OPTS}
${VNC_CMD} :2 ${VNC_OPTS}
${VNC_CMD} :3 ${VNC_OPTS}
${VNC_CMD} :4 ${VNC_OPTS}
${VNC_CMD} :5 ${VNC_OPTS}
#ps -ef | grep vncserver
