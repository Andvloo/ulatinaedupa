import argparse
import cv2
import time
import torch
import torchvision

import numpy as np
import util
class_names  = util.class_names

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = torchvision.models.video.r3d_18(weights='R3D_18_Weights.DEFAULT')

model = model.eval().to(device)

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help = 'path to input video')

parser.add_argument('-c', '--clip-len', dest = 'clip_len', default = 1, type = int, help = 'number of frames to consider for each prediction')

args = vars(parser.parse_args())

print(f"Number of Frames to Consider for Each Prediction: {args['clip_len']}")

#cell2


cap = cv2.VideoCapture(args['input'])

if (cap.isOpened() == False):
    print('Error while trying to read video. Please Check Path Again')
# get the frame width and height

frame_width = int(cap.get(3))

frame_height = int(cap.get(4))

# cell 3

save_name = f"{args['input'].split('/')[-1].split('.')[0]}"

out = cv2.VideoWriter(f"outputs/{save_name}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))
# cell 4

frame_count = 0

total_fps = 0

clips = []
print(args)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        start_time = time.time()

        image = frame.copy()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame = util.transform(image = frame)['image']

        clips.append(frame)

        if len(clips) == args['clip_len']:
            with torch.no_grad():
                input_frames = np.array(clips)
                print(7)
                input_frames = np.expand_dims(input_frames, axis = 0)

                input_frames = np.transpose(input_frames, (0,4,1,2,3))

                input_frames = torch.tensor(input_frames, dtype = torch.float32)

                input_frames = input_frames.to(device)

                outputs = model(input_frames)

                _, preds = torch.max(outputs.data, 1)

                label = class_names[preds].strip()

            end_time = time.time()

            fps = 1/(end_time - start_time)

            total_fps += fps
            frame_count += 1

            wait_time = max(1, int(fps/4))

            cv2.putText(image, label, (15, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, lineType = cv2.LINE_AA)

            clips.pop(0)

            cv2.imshow('image', image)

            out.write(image)

            if cv2.waitKey(wait_time) & 0xFF == ord('q'):
                break
        else:
            break