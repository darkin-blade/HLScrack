import os
import sys

if __name__ == "__main__":
  # 第一个参数为视频数目
  if (len(sys.argv) >= 2):
    videoNum = int(sys.argv[1])
    videoName = "file '{}.mp4'\n"
    listName = "list"
    fd = open(listName, "w") # 如果文件存在则发生错误
    for i in range(videoNum):
      fd.write(videoName.format(i + 1))
    fd.close()
    cmd = "ffmpeg -f concat -safe 0 -i list -c copy output.mp4"
    os.system(cmd)
  else:
    print('need input video number')