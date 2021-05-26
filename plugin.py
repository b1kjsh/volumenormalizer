#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import re
from unmanic.libs.unplugins.settings import PluginSettings


class Settings(PluginSettings):
    settings = {}


def on_worker_process(data):
    """
    Runner function - enables additional configured processing jobs during the worker stages of a task.

    The 'data' object argument includes:
        exec_ffmpeg             - Boolean, should Unmanic run FFMPEG with the data returned from this plugin.
        file_probe              - A dictionary object containing the current file probe state.
        ffmpeg_args             - A list of Unmanic's default FFMPEG args.
        file_in                 - The source file to be processed by the FFMPEG command.
        file_out                - The destination that the FFMPEG command will output.
        original_file_path      - The absolute path to the original library file.

    :param data:
    :return:
    
    """
    p = subprocess.run(['ffmpeg-normalize', data['original_file_path'], '-o', data['original_file_path'], '-f', '-c:a', 'aac'])
    
    
    # p = subprocess.run(['ffmpeg', '-i', data['original_file_path'], '-af', 'volumedetect', '-vn', '-sn', '-dn', '-f', 'null', 'pipe:1'],
    #                    stdout=subprocess.PIPE,
    #                    stderr=subprocess.PIPE,
    #                    bufsize=10**8)
    # rc = p.returncode
    # print(p.stdout, p.stderr)
    # mean_volume = re.search(r"mean_volume: ([0-9.-]{1,})", str(p.stderr)).group(1)
    # max_volume = re.search(r"max_volume: ([0-9.-]{1,})", str(p.stderr)).group(1)
    # if mean_volume:
    #     print("mean_volume = " + mean_volume)
    #     print("max_volume = " + max_volume)
    
    # volume_difference = (max_volume - -2.7) * -1

    # if volume_difference >= -3:
    #     p = subprocess.run(['ffmpeg', '-i', data['original_file_path'], '-af', 'volume='+volume_difference, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', data['file_out'], 'pipe:1'],
    #                        stdout=subprocess.PIPE,
    #                        stderr=subprocess.PIPE,
    #                        bufsize=10**8)
    # else:
    #     data['issues'].append({
    #         'id': 'VolumeNormalizer',
    #         'message': data['original_file_path'] + " Volume Normalization isn't needed already near ideal volume."
    #     })
    
        

    # for line in p.stdout:
    #     print(line)
    
    # stream = ffmpeg.input('file.mp4')
    # ffmpeg.run(stream, kwargs="-af \"volumedetect\" -vn -sn -dn -f null /dev/null")
    # )
    # if err:
    #     data['issues'].append({
    #         'id':      'VolumeNormalizer',
    #         'message': err,
    #     })            
    
    # mean_volume = -32.1
    # max_volume = -3.2
            
    return data

# data = { "original_file_path": "./file.mp4", "file_out": "./file_converted.mp4" }
# on_worker_process(data)
