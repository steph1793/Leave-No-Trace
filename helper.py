
from gym.wrappers import Monitor
from gym.wrappers.time_limit import TimeLimit

import glob
import io
import base64
from IPython.display import HTML

from IPython import display as ipythondisplay


"""
Utility functions to enable video recording of gym environment and displaying it
To enable video, just do "env = wrap_env(env)""
"""

def show_video(mp4):
  video = io.open(mp4, 'r+b').read()
  encoded = base64.b64encode(video)
  ipythondisplay.display(HTML(data='''<video alt="test" autoplay 
              loop controls style="height: 400px;">
              <source src="data:video/mp4;base64,{0}" type="video/mp4" />
           </video>'''.format(encoded.decode('ascii'))))


def wrap_env(env, max_episode_steps, video_folder, video_callable):
  env = Monitor(TimeLimit(env, max_episode_steps=max_episode_steps), video_folder, force=True, video_callable=video_callable)
  return env