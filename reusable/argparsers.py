import argparse

def get_args_parser(add_help=True):
    """ Usage: args = get_args_parser()"""
    parser = argparse.ArgumentParser(description='Name of Project', add_help=add_help)
    parser.add_argument('--source', type=str, default='data/videos', help='the destination path, e.g. video-file/dir.')
    parser.add_argument('--max-det', type=int, default=1000, help='maximal inferences per image.')
    parser.add_argument('--device', default='0', help='device to run our model i.e. 0 or 0,1,2,3 or cpu.')
    parser.add_argument('--webcam', action='store_true', help='whether to use webcam.')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args_parser()
    print(args.source, args.max_det, args.device, args.webcam)



