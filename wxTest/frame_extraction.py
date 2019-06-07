# import os
# import cv2
# import subprocess
# from multiprocessing import Queue
# filename = 'C:\\Users\\g_host\\Desktop\\test.mp4'
# q=Queue()
# def get_frame_types(video_fn):
#     command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
#     out = subprocess.check_output(command + [video_fn]).decode()
#     frame_types = out.replace('pict_type=','').split()
#     return zip(range(len(frame_types)), frame_types)

# def save_i_keyframes(video_fn):
#     frame_types = get_frame_types(video_fn)
#     i_frames = [x[0] for x in frame_types if x[1]=='I']
#     if i_frames:
#         basename = os.path.splitext(os.path.basename(video_fn))[0]
#         cap = cv2.VideoCapture(video_fn)
#         for frame_no in i_frames:
#             cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
#             ret, frame = cap.read()
#             q.put(frame)
#             print(frame)
# #             print("frame no:",frame_no)
#             outname = basename+'i_frame'+str(frame_no)+'.jpg'
#             cv2.imwrite(outname, frame)
#         cap.release()
#     else:
#         print ('No I-frames in '+video_fn)

# if __name__ == '__main__':
# 	save_i_keyframes(filename)


from multiprocessing import Queue
import logging
import cv2

import image2pipe

logging.basicConfig()

q = Queue()
decoder = image2pipe.images_from_url(q, "a.mp4", fps="30", scale=(400, 400))
decoder.start()

for i in range(q.qsize()):
	print(i)
# for pair in yield_from_queue(q):
#         fn, img = pair
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         cv2.imshow("gray", gray)
#         cv2.waitKey()
#         cv2.destroyAllWindows()