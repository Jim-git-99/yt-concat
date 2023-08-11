from pipeline.steps.get_video_list import GetVideoList
from pipeline.pipeline import Pipeline

CHANNEL_ID = 'UC7o64rkXin-ZS_gU6_pBDvA'

def main():
    inputs = {                    # Initial constant input
        'channel_id' : CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
